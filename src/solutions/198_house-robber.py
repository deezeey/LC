from typing import List

# 1.26 first try, 有前面70和746的基础这题20min写出来了
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        N = len(nums)
        max_money = [0] * N # the all time max of itself and all the houses from right
        max_money[-1] = nums[-1]
        max_money[-2] = max(nums[-1], nums[-2])
        for i in range(N-2)[::-1]:
            max_money[i] = max(max_money[i + 2] + nums[i], max_money[i + 1])
        return max(max_money)

# 看了下neetcode写的，简直令人汗颜的简短，而且他从左往右iterate的
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2