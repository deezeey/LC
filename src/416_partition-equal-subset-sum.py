from typing import List, Tuple
from functools import lru_cache

# 10.07 first try, 一开始test case跑过了以为自己是个天才...结果碰到[3, 3, 3, 4, 5]挂了
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # can it be broken into 2 parts such that each part sum up to be sum(nums)/2
        # 11 == 11 so check if sum(rest) = 11
        # [1, 2, 3, 5] sum up to be an odd number so return false
        if len(nums) == 1:
            return False
        TOTAL = sum(nums)
        if TOTAL % 2 != 0:
            return False
        PARTS_TOTAL = TOTAL / 2
        nums.sort()
        biggest = nums[-1]
        if biggest == PARTS_TOTAL:
            return sum(nums[:-1]) == PARTS_TOTAL  # <--- 根本没必要return这个，因为parts_total本来就是sum的一半，如果有一个数等于sum的一半剩下的所有数字之和一定也等于一半
        else:
            goal = PARTS_TOTAL - biggest
            remaining = goal
            for i in range(len(nums)):
                    remaining - nums[i]
                    if remaining < 0:
                        return False
                    elif remaining == 0:
                        return nums[i+1:-1] == PARTS_TOTAL
                    else:
                        i += 1


# 10.09看了一下neet code的solution，
# 他是计算了整个nums list所有的combination sum，如果其中某个combination sum等于nums sum的一半，那么就可以return true了
# 一开始百思不得其解为什么set里有一个数等于一半就可以了，后来恍然大悟确实只要有任意组合加起来等于一半，剩下的数加起来自然也等于一半了
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # can it be broken into 2 parts such that each part sum up to be sum(nums)/2
        # 11 == 11 so check if sum(rest) = 11
        # [1, 2, 3, 5] sum up to be an odd number so return false
        if len(nums) == 1:
            return False
        TOTAL = sum(nums)
        if TOTAL % 2 != 0:
            return False
        PARTS_TOTAL = TOTAL / 2
        combination_sum = set()
        combination_sum.add(0)
        
        for num in nums:
            if num == PARTS_TOTAL:
                return True
            new_combination_sum = set()
            for prev_sum in combination_sum:
                if prev_sum + num == PARTS_TOTAL:
                    return True
                # new_combination_sum.add(num) # <--- 因为combination_sum里头有0，所以其实没必要add num，这行可以去掉
                new_combination_sum.add(prev_sum + num)
            combination_sum.update(new_combination_sum)

        return False


# 11.27 复习自己写，自己只能想到一开始就能想到的那些，但是想不到怎么计算所有的combo sum
# 被comment out掉的部分是看了答案以后才想起来写的
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # sum of nums need to be even
        TOTAL = sum(nums)
        if TOTAL % 2 != 0:
            return False
        
        TARGET = TOTAL / 2
        # comb_sum = set([0])
        
        for num in nums:
            if num == TARGET:
                return True
        #     new_sums = set()
        #     for prev_sum in comb_sum:
        #         if prev_sum + num == TARGET:
        #             return True
        #         new_sums.add(prev_sum + num)
        #     comb_sum.update(new_sums)
        
        # return False


# neetcode 官方DFS dp solution
# Let n be the length of array and m be the subset_sum
# T 和 M 都是 O(m * n)。因为dfs func有n和subset_sum两个变动params。所以相当于我们要call 这个func recursively m * n times
# We are using a 2 dimensional array of size (m⋅n) and O(n) space to store the recursive call stack. 
# This gives us the space complexity as O(n) + O(m⋅n) = O(m⋅n)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)  # <--- DP的memoization在这一步一步搞定
        def dfs(nums: Tuple[int], n: int, subset_sum: int) -> bool:
            # Base cases
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False
            result = (dfs(nums, n - 1, subset_sum - nums[n - 1])
                    or dfs(nums, n - 1, subset_sum))
            return result

        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2
        n = len(nums)
        return dfs(tuple(nums), n - 1, subset_sum)

# 自己重写一遍这个跑的比官方慢很多。感觉就是因为没有加 n 这个parameter，所以instead of 存储新常量，我需要在recursion stack里store new tuple
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dfs(target: int, nums: Tuple[int]) -> bool:  # nums必须转成tuple因为list可以被修改所以无法用@cache decorater. 会收到unhashable type: 'list'错误
            if target == 0:
                return True
            if target < 0 or len(nums) == 0:
                return False
            n = len(nums) - 1
            res = dfs(target, nums[:n]) or dfs(target-nums[n], nums[:n])  # 必须这样写，不能直接return dfs(xxxx) or dfs(xxxx)那样memoization无法完成
            return res
        
        if sum(nums) % 2 != 0:
            return False
        TARGET = sum(nums) / 2
        return dfs(TARGET, tuple(nums))

# 改了一下，nums不pass进去dfs func。这个比刚才好但是T还是不如leet code官方答案
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(maxsize = None)
        def dfs(target: int, n: int) -> bool:
            if target == 0:
                return True
            if target < 0 or n == 0:
                return False
            res = dfs(target, n - 1) or dfs(target-nums[n], n - 1)  #神奇的是把num[n]换成n-1就要效率非常多因为树高少了一层
            # 看了讨论区的讨论。这个地方可能是leet code故意写错也有可能是efficiency move
            # Thats looks like an efficiency move to me. It reduces the tree depth by one and hence reduces the lookups to half, 
            # and as you have already pointed out : missing one element doesn't break this solution as it would find the other subset. 
            # So all good here.
            return res
        
        if sum(nums) % 2 != 0:
            return False
        TARGET = sum(nums) / 2
        return dfs(TARGET, len(nums) - 1)