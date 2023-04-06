from typing import List
# 最简单直观的解法
# 先找到左边和右边固定part，再计算中间要merge的part，最后拼起来
def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    s, e = newInterval
    left = []
    right = []
    for i in intervals:
        if i[1] < s:
            left.append(i)
        elif i[0] > e:
            right.append(i) 
        else:
            s = min(s, i[0])
            e = max(e, i[1])
    return left + [[s, e]] + right


# merge intervals
# 先把new interval按start排序放进去，再merge有必要merge的部分放到新list里
def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    if not intervals:
        return [newInterval]
    intervals.append(newInterval)
    res = []
    for interval in sorted(intervals, key=lambda ls:ls[0]):
        if res and res[-1][1] >= interval[0]:
            res[-1][1] = max(res[-1][1], interval[1]) 
        else: 
            res.append(interval)
    return res

# 9.24 复习自己做
def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    s, e = newInterval[0], newInterval[1]
    left = []
    right = []
    mid = [s, e]
    for interval in intervals:
        if interval[1] < s:
            left.append(interval)
            continue # <----一开始这里没有continue是不行的，具体看leetcode自己提交的wrong answer
        if interval[0] > e:
            right.append(interval)
            continue
        mid[0] = min(interval[0], mid[0])
        mid[1] = max(interval[1], mid[1])
    return left + [mid] + right


# test
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert(intervals, newInterval))


intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(insert(intervals, newInterval))

intervals = [[1,3],[6,9],[23, 56]]
newInterval = [12,15]
print(insert(intervals, newInterval))

# 11.02 复习自己做  T O(n) M O(n)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []
        mid_s, mid_e = newInterval[0], newInterval[1]

        for interval in intervals:
                if interval[1] < newInterval[0]:
                    left.append(interval)
                elif interval[0] > newInterval[1]:
                    right.append(interval)
                else:
                    mid_s = min(interval[0], mid_s)
                    mid_e = max(interval[1], mid_e)
        
        return left + [[mid_s, mid_e]] + right

# 12.07 复习自己写
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ns, ne = newInterval[0], newInterval[1]
        left, right = [], []
        for s, e in intervals:
            if e < ns:
                left.append([s, e])
            elif s > ne:
                right.append([s, e])
            else:
                ns = min(ns, s)
                ne = max(ne, e)
        
        return left + [[ns, ne]] + right