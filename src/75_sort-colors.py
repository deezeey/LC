from typing import List


# 因为只有3个数所以我们可以用双指针，实现O(n) T和O(1) M, 因为swapping happens in place
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, i, right = 0, 0, len(nums) - 1
        while i <= right: # <--- 相当于从头到尾遍历n
            if nums[i] == 2: # <--- 如果是2，和最右边的num换位置
                # 但是因为我们不知道最右边的num是几，所以i在这里不+1，我们下个loop还是check index0
                # 并且因为我们已经知道最后一位是2了，right可以-1
                nums[i], nums[right] = nums[right], nums[i] 
                right -= 1
            elif nums[i] == 0: # <--- 如果是0，和最左边的num换位置
                # 因为我们已经知道最左边是0了，所以left可以+1
                # 因为我们是从左往右便历的，i也得+1，这样我们可以check下一位
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            else:
                # 如果是1，leave it in place，check下一位。同时这时候，left和i开始脱节，变得一慢一快
                i += 1


# 11.05 复习，没记得这题要用3指针，自己就没写出来
# 12.13 复习还是没写出来 stack over flow了
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] == 0:
                l += 1
            elif nums[r] == 2:
                r -= 1
            elif nums[l] == 2:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            elif nums[r] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            else:
                l += 1
        return nums

# 12.15 复习自己写出来了
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, i = 0, 0
        r = len(nums) - 1

        while i <= r:
            if nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            elif nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            else:
                i += 1

        return nums