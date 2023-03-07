from typing import List

# 2.27 first try自己根本没想到如果nums有n个数字，答案最多=n+1这一层
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # positive int 1 ~ inf
        # we don't care about negative at all
        # [7, 8, 9, 11, 12] ---> 7 is the smallest int
        # [3, 4, 1, -1] ---> gap between 1 and 3
        # we're essentially looking for the gap between max of left interval and min of right interval
        # default left interval to be -inf to 0, default right interval to be the smallest pos num in arr that can not be merged into left interval
        # left_max, right_min = 0, inf
        pass

# 假设nums = [2, 4, 5, 1, 3, -1],那么结果max只能是 len（pos nums in arr) + 1. 结果min是1。所以我们可以把每个数放在对应的idx上，然后再iterate thru一遍，如果idx位置上的数字不对，即是答案
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            j = nums[i] - 1
            # put num[i] to the correct place if nums[i] in the range [1, n]
            if 0 <= j < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        # so far, all the integers that could find their own correct place 
        # have been put to the correct place, next thing is to find out the
        # place that occupied wrongly
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
    
# 自己重写一遍
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n: # 这个cycle sort怎么写是个套路要记住
            target_idx = nums[i] - 1
            if 0 <= target_idx < n and nums[target_idx] != nums[i]:
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
            else:
                i += 1

        for j in range(n):
            if nums[j] != j + 1: return j + 1
        return n + 1

# 嗯其实用set也可以只是要用额外的memory
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        new = set(nums)
        i = 1
        while i in new:
            i += 1
        return i