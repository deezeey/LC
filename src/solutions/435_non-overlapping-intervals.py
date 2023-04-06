from typing import List
from collections import defaultdict

# 12.08 自己做，自己想到的居然是图，太晚了没有写出来，而且我感觉肯定不是图
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        graph = defaultdict(set)

        for i in range(len(intervals)):
            s1, e1 = intervals[i][0], intervals[i][1]
            for j in range(len(intervals)):
                s2, e2 = intervals[j][0], intervals[j][1]
                if e1 > s2:
                    graph[i].add[j]
                    graph[j].add[i]
        
        count = [(len(v), k) for k, v in graph.items()]
        count.sort(reverse = True)

        res = 0
        # for overlap_count, interval_idx in count:
            # while 


# 看了neet code讲解的算法自己写的。 Onlogn
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0

        for i in range(len(intervals) - 1):
            if i == 0:
                end = intervals[i][1]
            if end > intervals[i + 1][0]:
                res += 1
                end = min(end, intervals[i + 1][1])
            else:
                end = intervals[i + 1][1]
        
        return res


# neet code写的
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res

# 12.15 复习，记得算法不记得写法，自己想了个用stack写的办法
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort() # sort by s
        res = 0
        stack = [intervals[0]]
        
        for i in range(1, len(intervals)):
            s1, e1 = stack[-1]
            s2, e2 = intervals[i]
            if s2 < e1:
                # if overlap, remove the one with greater end
                res += 1
                if e1 > e2:
                    stack.pop()
                    stack.append(intervals[i])
                else:
                    continue
            else:
                stack.append(intervals[i])
            
        return res

# 1.2 复习，记得算法，解法还是自己用stack写。就没想到设一个prev_end variable
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        stack = []
        res = 0

        for i in range(len(intervals)):
            if stack:
                s1, e1 = stack[-1]
                s2, e2 = intervals[i]
                if s2 < e1:
                    res += 1
                    if e1 <= e2:
                        continue
                    else:
                        stack.pop()
            stack.append(intervals[i])
        
        return res