from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return mid + 1 if nums[mid] < target else max(mid, 0)