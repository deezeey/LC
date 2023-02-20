from typing import List

# 10.06 first try自己写出来了
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn)
        intervals.sort(key=lambda l: l[0])
        stack = []
        for i in range(len(intervals)):
            if not stack:
                stack.append(intervals[i])
            else:
                tail = stack[-1]
                if intervals[i][0] <= tail[1]:
                    new_tail = [tail[0], max(intervals[i][1], tail[1])]
                    stack.pop()
                    stack.append(new_tail)
                else:
                    stack.append(intervals[i])
            i += 1
        return stack
        

# 11.02 复习自己写，好像比之前简单些，因为有sort所以 T O(nlog(n)) M O(n)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0]) #sort by starting points
        res = [intervals[0]]

        for i in range(len(intervals))[1:]:
            prev_s, prev_e = res[-1]
            cur_s, cur_e = intervals[i]
            if cur_s <= prev_e:
                res.pop()
                res.append([min(prev_s, cur_s), max(prev_e, cur_e)])
            else:
                res.append(intervals[i])
        
        return res