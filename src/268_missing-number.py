from typing import List
# 2.2 自己的解是M O(n)的
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = 0
        n_set = set(nums)
        while n <= len(nums):
            if n not in n_set:
                return n
            n += 1

# 有一个非bit manipulation的O(1)解。 即 0 + 1 + 2 + 3 - sum(nums)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = 0
        for n in range(len(nums) + 1):
            expected += n
        return expected - sum(nums)

# 异或运算满足交换律和结合律，也就是说：2 ^ 3 ^ 2 = 3 ^ (2 ^ 2) = 3 ^ 0 = 3
# 所以[3,0,1]做不停的异或运算的话。0 ^ 3 ^ 1 ^ 0 ^ 2 ^ 1 ^ 3 = 0 ^ 0 ^ 1 ^ 1 ^ 2 ^ 3 ^ 3。其他数字都俩俩抵消成0了，最后剩下 0 ^ 2
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res