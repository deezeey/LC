from typing import List

# 1.26 first try，刚刚做完 90 subsetii, 代码几乎可以照搬
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # candidates can contain dupes
        candidates.sort()
        res = []

        def backtrack(i, subset, total):
            # base case
            if total >= target or i == len(candidates):
                if total == target:
                    res.append(subset[::])
                return
            # recursive case
            # include candidates[i]
            subset.append(candidates[i])
            total += candidates[i]
            backtrack(i+1, subset, total)
            # backtrack(i+1, subset + [candidates[i]], total + candidates[i]) #不要加到subset再pop，直接修改recursive function里的parameter可以把T从beat 5.2%提升到beat 40%
            subset.pop()
            total -= candidates[i]
            # exclude candidates[i]
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            backtrack(i+1, subset, total)

        backtrack(0, [], 0)
        return res

# neetcode解法用的for loop
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
                return
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return res