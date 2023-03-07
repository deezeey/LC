from typing import List
import heapq
# 3.2 first try，自己的解法类似官方的brute force II，能过但是在 39/41 TLE了
# T O(n^2) M O(n)
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # [15,20,10],[19,24,8] overlapped in [19, 20], so [19, 20] takes the higher height 10
        # gap covered by no buildings will be 0
        # 0 will be the last height for sure
        # how to handle the overlap?
        # [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
        # what if we find the max of x axis and try to find the highest num from intervals covers this x val
        # we can sort buildings by start x
        # 1 pass find the max of right
        # 2 pass sort buildings by left <--- this is already done
        # 3 pass check the left and right one by one and get the max from intervals containing left
        # [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]] ---> x:[2, 3, 5, 7, 9, 12, 15, 19, 20, 24]
        #  l <= x < r is considered within interval
        # need a var prev_height
        # [2, 10], [3, max(10, 15)], [5, max(10, 15, 12)] <--- 15 was prev_height so pass 5, [7, max(10, 12)]....[24 == max x, 0]

        # 1 pass find the max of right and record the uniq l & r
        max_x, x_arr = 0, set()
        for l, r, h in buildings:
            max_x = max(max_x, r)
            x_arr.update({l, r})
        x_arr = list(x_arr)
        x_arr.sort()

        # 2 pass check the left and right one by one and get the max from intervals containing left
        prev_h, res = 0, []
        for x in x_arr:
            i, max_h = 0, 0
            while i < len(buildings) and buildings[i][0] <= x:
                if buildings[i][1] <= x:
                # skipping the intervals doesn't contain x
                    i += 1
                else:
                # update max_h if interval contains x
                    max_h = max(max_h, buildings[i][2])
                    i += 1
            if max_h == prev_h:
            # skip recording this x if it's the same heigh as prev horizontal line
                continue
            else:
            # record this new horizontal line
                res.append([x, max_h])
                prev_h = max_h

        return res


# 加上heap来存一个priority queue就能过。T O(nlogn)
# 生成x arr长度n， while loop iterates thru it, worst case we need to heappush and heappop at every x, so 2 * logn, so T can be summarized to n * logn
# M O(n), x_arr长度 2 * n, cur_buildings和res长度也不可能超过n。所以是n
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # find the max of right and record the uniq l & r
        x_arr = []
        for i, v in enumerate(buildings):
            l, r, _ = v
            x_arr.extend([[l, i], [r, i]])
        x_arr.sort()

        # max heap to store cur buildings
        i, prev_h, cur_buildings, res = 0, 0, [], []
        while i < len(x_arr):
            x = x_arr[i][0]
            # we may have multiple buildings with edges at the same x
            while i < len(x_arr) and x_arr[i][0] == x: # 不要忘了里面也有一个while loop，这可以保证我们一批一批的处理当前x的所有building edge
                b_idx = x_arr[i][1]
                # if left edge add building to cur_buildings
                l, r, h = buildings[b_idx]
                if x == l:
                    heapq.heappush(cur_buildings, [-1 * h, r])
                # keep popping the buildings from max heap if we've passed the right edges
                while cur_buildings and cur_buildings[0][1] <= x:
                    heapq.heappop(cur_buildings)
                i += 1 # 这个while loop+1了外层的while loop就不需要
            # get the max height at cur x and push to res
            cur_h = -1 * cur_buildings[0][0] if cur_buildings else 0
            if cur_h != prev_h: 
                res.append([x, cur_h])
                prev_h = cur_h
        return res
    
# 还有一个类似merge sort的办法，但是要想清楚如何merge 2 skylines。
# 要点是keep l_prev_h, r_prev_h来记录前面的高度，然后当前l_h要和r_prev_h比，当前r_h要和l_prev_h比
# TM和上面解法一样
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # merge sort, keep dividing into 2 halves and merge their result skylines
        N = len(buildings)
        if N == 0:
            return []
        if N == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        
        mid = N // 2
        l_skyline, r_skyline = self.getSkyline(buildings[:mid]), self.getSkyline(buildings[mid:])
        return self.mergeSkylines(l_skyline, r_skyline)
    
    def mergeSkylines(self, l_sky, r_sky):
        # Initalize l_idx=0, r_idx=0 as the pointer of l_sky and r_sky.
        # Since we start from the l ground, thus the previous h from 
        # l_sky and r_sky are 0.
        res = []
        l_idx, r_idx = 0, 0
        l_prev_h, r_prev_h = 0, 0

        # Now we start to iterate over both skylines.
        while l_idx < len(l_sky) and r_idx < len(r_sky):
            next_l_x = l_sky[l_idx][0]
            next_r_x = r_sky[r_idx][0]
            
            # If we meet l_sky key point first, our current h changes to the
            # larger one between h on l skyline and the previous h on r
            # skyline. Update the previous h from l_sky and increment l_idx by 1.
            if next_l_x < next_r_x:
                l_prev_h = l_sky[l_idx][1]
                cur_x = next_l_x
                cur_y = max(l_prev_h, r_prev_h)
                l_idx += 1
           
            # If we meet r_sky key point first, our current h changes to the
            # larger one between h on r skyline and the previous h on l
            # skyline. Update the previous h from r_sky and increment r_idx by 1.
            elif next_l_x > next_r_x:
                r_prev_h = r_sky[r_idx][1]
                cur_x = next_r_x
                cur_y = max(l_prev_h, r_prev_h)
                r_idx += 1

            # If both skyline key points has same x:
            # Our current h is the larger one, update the previous h
            # from l_sky and r_sky. Increment both l_idx and r_idx by 1.
            else:
                l_prev_h = l_sky[l_idx][1]
                r_prev_h = r_sky[r_idx][1]
                cur_x = next_l_x
                cur_y = max(l_prev_h, r_prev_h)
                l_idx += 1
                r_idx += 1
            
            # Discard those key points that has the same h as the previous one.
            if not res or res[-1][1] != cur_y:
                res.append([cur_x, cur_y])
        
        # If we finish iterating over any skyline, just append the rest of the other
        # skyline to the merged skyline.
        while l_idx < len(l_sky):
            res.append(l_sky[l_idx])
            l_idx += 1
        while r_idx < len(r_sky):
            res.append(r_sky[r_idx])
            r_idx += 1
        return res