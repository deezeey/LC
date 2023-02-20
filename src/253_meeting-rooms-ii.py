from typing import List
import heapq

# 12. 09 first try自己用heap做出来了
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = 1
        end_time_heap = []

        for i in range(len(intervals)):
            s, e = intervals[i][0], intervals[i][1]
            if not end_time_heap:
                heapq.heappush(end_time_heap, e)
            elif s >= end_time_heap[0]:
                heapq.heappop(end_time_heap)
                heapq.heappush(end_time_heap, e)
            else:
                rooms += 1
                heapq.heappush(end_time_heap, e)
        
        return rooms


# neetcode有更优的解法
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def minMeetingRooms(self, intervals):
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res
        
# 自己按neet code 思路写了一下
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start, end = [], []
        for s, e in intervals:
            start.append(s)
            end.append(e)
        start.sort()
        end.sort()

        s_i, e_i = 0, 0
        rooms, max_count = 0, 0

        while s_i < len(intervals):
            if start[s_i] < end[e_i]:
                rooms += 1
                s_i += 1
            else:
                rooms -= 1 #这里为啥要-1是有点难想明白的
                e_i += 1

            max_count = max(max_count, rooms)
            
        return max_count

# 1.2 复习，自己第一反应仍然是用heap
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = 0
        heap = [] # use a min heap to record end time of all the meeting rooms
        
        for s, e in intervals:
            if heap and heap[0] <= s:
                heapq.heappop(heap)
                heapq.heappush(heap, e)
                continue
            heapq.heappush(heap, e)
            rooms += 1
        
        return rooms
        
# 复习一下另一个解法
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([s for s, _ in intervals])
        end = sorted([e for _, e in intervals])
        rooms, max_cnt = 0, 0

        s, e = 0, 0
        while s < len(start):
            if start[s] < end[e]:
                rooms += 1
                s += 1
            else:
                rooms -= 1
                e += 1
            max_cnt = max(max_cnt, rooms)

        return max_cnt