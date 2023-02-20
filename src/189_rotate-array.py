from typing import List

# 2. 10 first try。第一个解肯定过不了， 第二个解只能过len为奇数的情况，然后时间就到了，干脆看正解了
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1) slice & put together
        k = len(nums) - k
        nums[:] = nums[k:] + nums[:k]
        # 2) use idx
        i, cur = 0, nums[0]
        while True:
            to_idx = i + k
            if to_idx >= len(nums):
                to_idx = i - (len(nums) - k)
            tmp = nums[to_idx]
            nums[to_idx] = cur
            cur = tmp
            i = to_idx
            if i == 0:
                break

# T On M O1的解，先reverse整个arr然后reverse first k elements，再reverse the rest
class Solution:
    def reverse(self, nums: List[int], l: int, r: int) -> None:
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1 
            r -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums) # 千万不能漏了这行，corner case nums只有2长，但我们需要rotate 5次怎么办？
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums)-1)   