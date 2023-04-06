from typing import List
# 10.02 first try, 自己做出来了
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        incre_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            if incre_sum < 0:
                incre_sum = nums[i]
            else:
                incre_sum = incre_sum + nums[i]
            max_sum = max(max_sum, incre_sum)
        return max_sum


# 11.01 复习居然又写不出来了，这个碰见[-2,1] output 0，不对
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        cur = nums[0]
        maxSum = nums[0]
        for num in nums[1:]:
            if num < 0 and maxSum < 0:
                maxSum = max(num, maxSum)
            else:
                cur += num
                if cur < 0:
                    cur = 0
                maxSum = max(maxSum, cur)
        return maxSum

# 改了一下，可能是太晚了脑子不清醒了吧居然这题都没做出来 T O(n) M O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = maxSum = nums[0]
        for num in nums[1:]:
            if cur < 0:
                cur = num
            else:
                cur += num
            maxSum = max(maxSum, cur)
        return maxSum


# 12.02 复习，自己写出来了但是也花了二十分钟大概
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        max_sum = cur = nums[0] 

        for i in range(1, len(nums)):
            if cur < 0 and nums[i] > cur:
                cur = nums[i]
            else:
                cur += nums[i]
            max_sum = max(max_sum, cur)
            
        return max_sum