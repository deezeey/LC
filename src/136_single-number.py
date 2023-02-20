from typing import List

# 没做过bit manipulation，不知道有 ^ 这个operator也不知道 XOR (异或）是啥
# n ^ n = 0, 0 ^ n = n
# 关于XOR只要记住，相同的数XOR等于0，
# Google Python Bitwise Operators
# neetcode的正解
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 # n ^ 0 = n
        for n in nums:
            res = res ^ n
        return res