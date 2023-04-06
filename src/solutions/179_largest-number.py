from typing import List
import functools

# 2.9 first try自己的思路是对比[3, 34, 302]时候在短的数字后面全部加上第一个数字，就对比[333, 343, 302]这样
# 能过221 / 230 cases 碰见[432,43243]挂了

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        idx_arr = [[] for _ in range(10)] # idx of num in nums that start with digit 1-9
        for i in range(len(nums)):
            num = nums[i]
            idx_arr[int(str(num)[0])].append(i)
        res = ""
        for i, idx_ls in enumerate(idx_arr[::-1]):
            i = len(idx_arr) - i
            if not idx_ls:
                continue
            if len(idx_ls) == 1:
                res += str(nums[idx_ls[0]])
            else:
                comparables = [[nums[j], str(nums[j])] for j in idx_ls]
                max_len = max([len(str(comp[0])) for comp in comparables])
                for comp in comparables:
                    comp_str = str(comp[0])
                    if len(comp_str) < max_len:
                        for _ in range(max_len - len(comp_str)):
                            comp[0] = comp[0] * 10 + i
                comparables.sort()
                while comparables:
                    res += comparables.pop()[1]
        return res

# neetcode写的就是很暴力的两两比较, 但是这个cmp_to_key func很冷门
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)
        
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        nums = sorted(nums, key=functools.cmp_to_key(compare))

        return str(int("".join(nums)))

# 改进版本，不需要cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums[:] = map(str, nums)
        nums.sort(key=NumCompare, reverse=True)
        return ''.join(nums).lstrip('0') or '0'

class NumCompare:
    def __init__(self, s: str):
        self.s = s
    def __lt__(self, other: str) -> bool:
        return self.s + other.s < other.s + self.s