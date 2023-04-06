from typing import List
# 1.30 first try自己半小时内想出来了brute force dfs
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # each num can only be used once and order can't be changed
        # num can be 0 or positive
        # target can be negative
        # decision tree height = n, total leaf nodes = 2 ** n
        # if there're same num in nums, we will encounter same problem
        count = 0
        def dfs(i, a):
            nonlocal count
            if i == len(nums):
                if a == target:
                    count += 1
                return
            dfs(i + 1, a + nums[i])
            dfs(i + 1, a - nums[i])
        dfs(0, 0)
        return count
    
# 中午烧了好吃的腐竹烧牛腩，可能吃开心了所以吃完饭自己20分钟就写出来了？
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # f([1,2,1,1], t=3)  =  f([1,2,1], t=2) + f([1,2,1], t=4)
        # f([1,2,1], t=2) = f([1,2], t=1) + f([1,2], t=3) 
        # f([1,2,1], t=4) = f([1,2], t=3) + f([1,2], t=5)
        # ...
        # f([1], t=-1) = 1, f([1], t=3) = 0 etc...
        dp = {}
        def dfs(i, t):
            if (i, t) in dp:
                return dp[(i, t)]
            if i == 0:
                # if t == 0 and nums[i] == 0: #一开始漏了这个edge case。这很重要！
                #     return 2
                if nums[i] == abs(t):
                    dp[(i, t)] = 1
                    return 1
                else:
                    dp[(i, t)] = 0
                    return 0
            dp[(i, t)] = dfs(i-1, t-nums[i]) + dfs(i-1, t+nums[i])
            return dp[(i, t)]

        return dfs(len(nums)-1, target)

# neetcode写的，思路和我相同但是他的base case是最后一位而不是第一位，这样他不需要handle 0
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}  # (index, total) -> # of ways

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(
                i + 1, total - nums[i]
            )
            return dp[(i, total)]

        return backtrack(0, 0)
