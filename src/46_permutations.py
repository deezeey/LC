from typing import List

# 10.30 first try，自己7分钟写出来的。。。不枉费我花了一个周末理解回溯。。。
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, cur):
            # base case
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            for i in range(len(nums)):
                if nums[i] in cur:
                    continue
                else:
                    cur.append(nums[i])
                    dfs(i+1, cur)
                    del cur[-1]
        
        dfs(0, [])
        return res

# neet code写的
# 他是[1, 2, 3]的permutation等于[2, 3]的permutaion append上1，这样不断往下拆解直到nums只剩1个element那就只有一种permutation
# 具体代码没太看懂，太困了要睡了
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # base case
        if len(nums) == 1: 
            return [nums[:]]  # nums[:] is a deep copy

        for _ in range(len(nums)):
            n = nums.pop(0)  # <---- pop 1 from [1, 2, 3], pop 2 from [2, 3], etc...
            perms = self.permute(nums) # <--- perms = permute([2, 3]), permute([3]), etc...

            for perm in perms: # for [3]:
                perm.append(n) # append 2, so it become [3, 2]
            res.extend(perms)
            nums.append(n)
        return res


# 11.29 复习自己写。一开始除了append res每个地方都没用copy就跑不过。折腾了一会儿才想明白
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(cur, subset):
            if len(subset) == 1:
                res.append(cur + subset)
                return

            for num in subset[:]:
                cur.append(num)
                subset.remove(num)
                backtrack(cur[:], subset[:])
                del cur[-1]
                subset.append(num)
        
        backtrack([], nums)
        return res