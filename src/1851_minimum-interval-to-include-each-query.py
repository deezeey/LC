from typing import List
from collections import defaultdict
import heapq

# 12.10 first try自己想用binary search没想明白，20分钟以后决定不浪费时间了
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = [(i[1] - i[0] + 1, i[0], i[1]) for i in intervals]
        intervals.sort() # sort by length
        intervals.sort(key = lambda x: x[1]) # sort by start

        # binary search to find interval idx i with start <= queries[j] & attach length to res
        res = [-1] * len(queries)

        for j in len(queries):
            l, r = 0, len(intervals)
            while l <= r:
                mid = (l + r) // 2
                if intervals[mid][1] > queries[j]:
                # everything to the right can't contain queries[j]
                    r = mid - 1
                # else:
                # everything to the left still can contain queries[j] unless ends before queries[j]


# 看了neet code讲解自己写了一遍， TLE了
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = [(i[0], i[1], i[1] - i[0] + 1) for i in intervals]
        intervals.sort() # sort by start point
        res = {}

        for num in sorted(queries):
            i = 0
            length_min_heap = []
            while i < len(intervals) and intervals[i][0] <= num:
                if intervals[i][1] >= num:
                    length_min_heap.append(intervals[i][2])
                i += 1
            if length_min_heap:
                heapq.heapify(length_min_heap)
                res[num] = heapq.heappop(length_min_heap)
            else:
                res[num] = -1
        
        res_ls = []
        for num in queries:
            res_ls.append(res[num])

        return res_ls


# neetcode的写法不会TLE，非常效率。O nlogn + qlogq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []
        res = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))  # <--- somehow在这个案例里heappush更加高效
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]
 
# 写heappush能beat90%但是写heapifyTLE。神了奇了
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort() # sort by start point
        res = {}
        i = 0  # i 和 heap 都是 universal的并不是每个num initiate一次
        length_min_heap = []

        for num in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= num: #一开始对end没要求，只要s满足条件全部push进heap
                s, e = intervals[i]
                # length_min_heap.append((e - s + 1, e))
                heapq.heappush(length_min_heap, (e - s + 1, e)) #push进heap里的东西是(len, end)
                i += 1
            # heapq.heapify(length_min_heap)            # 但是一旦把上面的heappush换成heapify就会TLE，真是奇了怪了
            while length_min_heap and length_min_heap[0][1] < num: # 如果heap len最小的end不满足条件，pop掉它
                heapq.heappop(length_min_heap)
            res[num] = length_min_heap[0][0] if length_min_heap else -1 #取len最小的数

        return [res[num] for num in queries]

# 12.15 复习自己写，33/42 又TLE了
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        new_q = sorted(queries)
        res = {}

        for q in new_q:
            min_hp = [] # 这个慢的原因首先是min_hp不是universal
            for i in intervals: # i也不是universal，这样要iterate 很多遍，另外in general for就是比while要慢
                if i[0] <= q and i[1] >= q:
                    heapq.heappush(min_hp, i[1] - i[0] + 1)
            if min_hp:
                res[q] = heapq.heappop(min_hp)
            else:
                res[q] = -1

        return [res[q] for q in queries]

# 重写一遍
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        new_q = sorted(queries)
        res = {}
        min_hp = []
        i = 0


        for q in new_q:
            while i < len(intervals) and intervals[i][0] <= q:
                s, e = intervals[i]
                heapq.heappush(min_hp, (e - s + 1, e))
                i += 1
            while min_hp and min_hp[0][1] < q:
                heapq.heappop(min_hp)
            res[q] = min_hp[0][0] if min_hp else -1

        return [res[q] for q in queries]

# 1.3 复习还是扫到一眼笔记上的中文提示才记起来怎么做
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        hp = [] # min heap storing (size, s, e)
        i = 0
        res = defaultdict(int)

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                s, e = intervals[i]
                heapq.heappush(hp, [e - s + 1, s, e])
                i += 1
            while hp and hp[0][2] < q:
            # if interval end < query number, pop
            # ex: [4, 4] does not work for query 5
                heapq.heappop(hp)
            res[q] = -1 if not hp else hp[0][0]
        
        return [res[q] for q in queries]