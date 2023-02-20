from typing import List

#  1.26 first try, 不太记得backtracking了直接看了neetcode的解法
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # sort方便后面skip相同的数字

        def backtrack(i, subset):
            #  base case
            if i == len(nums):
                res.append(subset[::]) #记住要append copy
                return
            # iterative case
            # include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            # skip nums[i]
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            backtrack(i + 1, subset)
        
        backtrack(0, [])
        return res