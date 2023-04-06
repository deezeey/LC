from typing import List

# 2.7 first try
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, fill = 0, 0
        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[fill] = nums[fill], nums[i]
                fill += 1
            i += 1
        return nums