from typing import List
# 2.1 first try这题好像比较intuitive，更像interval
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # same letter can appear in one substring multi times
        # set of the substrings should be mutually exclusive
        # get the first & last idx of a letter's appearance
        # intervals overlapping with each other needs to be merged
        intervals = {}
        for i, c in enumerate(s):
            if c not in intervals:
                intervals[c] = [i, i]
            intervals[c][1] = i
        intervals = sorted(intervals.values()) # 可能都不用sort
        res = []
        for s, e in intervals:
            if not res or res[-1][1] < s:
                res.append([s, e])
            res[-1][1] = max(res[-1][1], e)
        return [e - s + 1 for s, e in res]

# neetcode写的，我觉得我的interval解法更容易理解？
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        count = {}
        res = []
        i, length = 0, len(S)
        for j in range(length):
            c = S[j]
            count[c] = j

        curLen = 0
        goal = 0
        while i < length:
            c = S[i]
            goal = max(goal, count[c])
            curLen += 1

            if goal == i:
                res.append(curLen)
                curLen = 0
            i += 1
        return res