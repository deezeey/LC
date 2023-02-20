from typing import List

# 1.26 first try自己的解能pass168/189 test cases，碰到nums =[-1,-2,-3,0] 跪了
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l_to_r_product = [[float("-inf"), float("-inf")] for _ in range(len(nums))] # [accumulated_product, cur_max_product]
        r_to_l_product = [[float("-inf"), float("-inf")] for _ in range(len(nums))]
        l_to_r_product[0] = [nums[0], nums[0]]
        r_to_l_product[-1] = [nums[-1], nums[-1]]

        for i in range(1, len(nums)):
            accu_product = nums[i] * l_to_r_product[i - 1][0]
            cur_max_product = max(accu_product, nums[i])
            l_to_r_product[i] = [accu_product, cur_max_product]
        
        for i in range(len(nums)-1)[::-1]:
            accu_product = nums[i] * r_to_l_product[i + 1][0]
            cur_max_product = max(accu_product, nums[i])
            r_to_l_product[i] = [accu_product, cur_max_product]

        max_l_to_r = max([mp for _, mp in l_to_r_product])
        max_r_to_l = max([mp for _, mp in r_to_l_product])

        return max(max_l_to_r, max_r_to_l)

# 正解是在每个位置同时记住当前最大和当前最小，因为有负数的存在，之前的最小可能可以乘以当前负数变成最大
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min, cur_max = 1, 1
        res = nums[0]
        for n in nums:
            tmp_cur_max = max(cur_max * n, cur_min * n, n) # 注意这里1）要和n自身的值比较 2）不要直接覆盖cur_max原var，因为下面算min还要用
            tmp_cur_min = min(cur_max * n, cur_min * n, n)
            cur_max = tmp_cur_max
            cur_min = tmp_cur_min
            res = max(cur_max, res)
        return res