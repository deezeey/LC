from typing import List

# 12.09 first try 非常简单
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1, len(intervals)):
            s2, e2 = intervals[i][0], intervals[i][1]
            s1, e1 = intervals[i - 1][0], intervals[i-1][1]
            if e1 > s2:
                return False
        
        return True

# 1.2 复习，这题没啥好说的
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1, len(intervals)):
            s1, e1 = intervals[i - 1]
            s2, e2 = intervals[i]
            if s2 < e1:
                return False
        return True