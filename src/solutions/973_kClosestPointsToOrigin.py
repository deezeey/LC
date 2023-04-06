import heapq
from typing import List
# 10.03 first try，自己的解，能跑过test 
# # case但是submit超时，因为太多重复iteration了，属实没有必要
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distance = {}
        for i in range(len(points)):
            point = points[i]
            if len(distance) < k:
                distance[i] = point[0]**2 + point[1]**2
            else:
                cur_max_distance = max(distance.values())
                if point[0]**2 + point[1]**2 < cur_max_distance:
                    del distance[max(distance, key = distance.get)]
                    distance[i] = point[0]**2 + point[1]**2
                else:
                    pass
        res_keys = distance.keys()
        res = [points[i] for i in res_keys]
        return res


# 其实全部算一遍然后sort就好了，for loop O(n), sort O(nlog(n))
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        res = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            res.append([dist, x, y])
        res.sort(key = lambda e: e[0])
        res = [[x, y] for d, x, y in res[0:k]]
        return res


# neetcode 用的heap应该会比sort稍微efficient一点点
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        pts = []
        for x, y in points:
            dist = (abs(x - 0) ** 2) + (abs(y - 0) ** 2)
            pts.append([dist, x, y])

        res = []
        heapq.heapify(pts)
        for _ in range(k):
            dist, x, y = heapq.heappop(pts)
            res.append([x, y])
        return res

# 11.10 复习自己写，min heap是O(nlogn),因为heap长度等于 points length，但是如果用长度为k的max heap，T会被缩减为 O(nlogk). 在k比n小很多的情况下会更优
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for point in points:
            x, y = point[0], point[1]
            heapq.heappush(heap, (x**2 + y**2, point)) #像neet code那样全部保存起来然后heapify更好，因为heapify一次只要O(n)但是push n次需要n * logn（每次push的花费）
        
        while k:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res

# 用max heap重写了一遍
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] # max heap with max len = k

        for x, y in points:
            dist = x ** 2 + y ** 2
            if len(heap) == k:
                if -1 * heap[0][0] > dist:
                    heapq.heappop(heap)
                else:
                    continue
            heapq.heappush(heap, (-dist, [x, y]))
        
        return [point[1] for point in heap]

# 去做215之后用quick select重写了一遍。这个答案能pass 86 out of 87 cases，在最后k = 5k的时候TLE了。但是知道有这个解法还是很重要的
#   - Best Case: O(n)
#   - Average Case: O(n)
#   - Worst Case: O(n^2)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def partition(ls, left, right):
            fill, pivot = left, ls[right]
            for i in range(left, right):
                ls_distance = ls[i][0] ** 2 + ls[i][1] ** 2
                pivot_distance = pivot[0] ** 2 + pivot[1] ** 2
                if ls_distance <= pivot_distance:
                    ls[i], ls[fill] = ls[fill], ls[i]
                    fill += 1
            ls[fill], ls[right] = ls[right], ls[fill]
            return fill
        
        l, r = 0, len(points) - 1
        while l < r:
            fill = partition(points, l, r)
            if fill > k:
                r = fill - 1
            elif fill < k:
                l = fill + 1
            else:
                break
        
        return [[x, y] for x, y in points[:k]]


# 1.9 复习，不明白为啥这题是medium，好像很简单？
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []
        res = []

        for x, y in points:
            d = x ** 2 + y ** 2
            hp.append([d, x, y])
        heapq.heapify(hp)
        while k > 0:
            _, x, y = heapq.heappop(hp)
            res.append([x, y])
            k -= 1
        return res
        
        