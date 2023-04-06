from typing import List

# 2.7 first try写出来了
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if not nums:
            return [str(lower) + "->" + str(upper)] if lower != upper else [str(lower)]
        res = []
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i + 1] - nums[i] > 1:
                res.append((nums[i]+1, nums[i+1]-1))
        if nums[0] != lower:
            res = [(lower, nums[0]-1)] + res
        if nums[-1] != upper:
            res = res + [(nums[-1] + 1, upper)]
        for i in range(len(res)):
            s, e = res[i]
            if s == e:
                res[i] = str(s)
            else:
                res[i] = str(s) + "->" + str(e)
        return res

# 官方解法也是一样
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # formats range in the requested format
        def formatRange(lower, upper):
            if lower == upper:
                return str(lower)
            return str(lower) + "->" + str(upper)

        result = []
        prev = lower - 1
        for i in range(len(nums) + 1):
            curr = nums[i] if i < len(nums) else upper + 1
            if prev + 1 <= curr - 1:
                result.append(formatRange(prev + 1, curr - 1))
            prev = curr
        return result