from typing import List

# 10.19 first try自己40 min以内写的，pass了87 out of 322 cases
# failed on [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
# 还是自己总结的规律不正确
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 1, len(height) - 2
        l_bound = r_bound = min(height[l-1], height[r+1])
        res = 0

        if l == r:
            if height[l] < l_bound:
                res += l_bound - height[l]
        
        while l < r:
            if l == r - 1:
                l_bound = r_bound = min(l_bound, r_bound)

            if height[l] >= l_bound:
                l_bound = height[l]
            else:
                res += (l_bound - height[l])
                print("l", l, l_bound - height[l])
            
            if height[r] >= r_bound:
                r_bound = height[r]
            else:
                res += (r_bound - height[r])
                print("r", r, r_bound - height[r])

            l += 1
            r -= 1

        return res

# r 24 2
# l 2 2
# l 3 4
# r 22 2
# l 4 1
# r 21 4
# l 5 2
# r 20 5
# l 6 4
# r 19 7
# l 7 1
# r 18 6
# l 8 3
# r 17 7
# r 16 8
# r 15 5
# l 11 2
# r 14 3
# l 12 3


# I almost got it, neet code做的唯一不同之处就是，他每轮只移动一个指针，l和r哪个boundary小他就移动哪个指针
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax: #因为我们的公式是min(max(left bars), max(right bars)) - height[i]
                # 所以如果一开始左是高度0，右是高度1，右边的max(right bars)至少是1，怎样也不可能比0小，我们就完全不用check右边
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res


# 11.06 复习自己写，pass不了[1,7,5]的case，感觉自己总结的逻辑总是有漏洞
class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,1,0,2,1,0,1,3,2,1,2,1]
        #  0   1   1 2 1     1   0
        # index 0 & len(height) - 1 definitely can trap only 0 water
        # water can be trapped at index i is min between left & right boundary - its own height
        # the definition of left & right boundary is highest to its left & highest to its right
        if len(height) <= 2:
            return 0

        max_vol = 0
        l, i, r = 0, 0, 0
        while i < len(height):
            while l < len(height) - 1 and height[l + 1] > height[l]:
                l += 1
                r = l + 1
            while r < len(height) - 1 and height[r] < height[l]:
                r += 1
            vol_i = max(min(height[l], height[r]) - height[i], 0)
            max_vol += vol_i
            # when next height[i] is greated then height[l] we know we need to conclude this pit at current i
            if height[i] >= height[l]:
                cur_vol = 0
                l = i
                r = i + 1
            i += 1

        return max_vol

# 不用双指针的方法，这个方法也是 T O(n), 因为就是iterate thru 3遍，缺点是 M也是 O(n)因为要存两个等长数列
class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,1,0,2,1,0,1,3,2,1,2,1]
        #  0   1   1 2 1     1   0
        # index 0 & len(height) - 1 definitely can trap only 0 water
        # water can be trapped at index i is min between left & right boundary - its own height
        # the definition of left & right boundary is highest to its left & highest to its right
        if len(height) <= 2:
            return 0 
        
        leftMax, rightMax = [0, height[0]], [0, height[-1]]
        curLeftmax, curRightmax = height[0], height[-1]
        maxVol = 0

        for i in range(2, len(height)):
            curLeftmax = height[i - 1] if height[i - 1] > curLeftmax else curLeftmax
            leftMax.append(curLeftmax)
        
        for i in range(len(height) - 3, -1, -1):
            curRightmax = height[i + 1] if height[i + 1] > curRightmax else curRightmax
            rightMax.append(curRightmax)
        rightMax = rightMax[::-1]

        for i in range(len(height)):
            maxVol += max(min(leftMax[i], rightMax[i]) - height[i], 0)

        return maxVol

# 自己看答案以后终于想通了逻辑，T O(n) M O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,1,0,2,1,0,1,3,2,1,2,1]
        #  0   1   1 2 1     1   0
        # index 0 & len(height) - 1 definitely can trap only 0 water
        # water can be trapped at index i is min between left & right boundary - its own height
        # the definition of left & right boundary is highest to its left & highest to its right
        #  min(max(left bars), max(right bars)) - height[i]
        l, r = 0, len(height) - 1
        max_left, max_right = height[0], height[-1]
        max_vol = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                max_left = max(height[l], max_left)
                max_vol += max_left - height[l]
            else:
                r -= 1
                max_right = max(height[r], max_right)
                max_vol += max_right - height[r]
        
        return max_vol


# 12.13 复习，自己还记得，但是写的这个解需要额外space所以不是最优的，还是上面那个解好点。但是思路清晰就够了
class Solution:
    def trap(self, height: List[int]) -> int:
        # max(min(left_max, right_max) - self, 0)
        left_max = [0] * len(height)
        right_max = [0] * len(height)

        for i in range(1, len(height)):
            left_max[i] = max(height[i - 1], left_max[i - 1])
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(height[i + 1], right_max[i + 1])
        
        res = 0
        for i in range(len(height)):
            res += max(min(left_max[i], right_max[i]) - height[i], 0)
        
        return res