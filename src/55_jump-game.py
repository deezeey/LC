from typing import List

# 1.31 first try自己20分钟写出来的DP会在75/170 TLE
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True
        for i in range(len(nums) - 2, -1, -1):
            num = nums[i]
            j = 0
            while j <= num and i + j < len(dp):
                if dp[i + j] == True or (i + j == len(nums) - 1):
                    dp[i] = True
                    break
                j += 1
        return dp[0]

# keep moving the goal to the left比DP更加高效，因为
# [2,3,1,1,4]，我们知道，到达倒数第二个1等同于到达最后一个4，更重要的是，如果左边的任何数字，能够直接到达4，那么它一定可以到达1，所以我们没有必要再看4了
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0