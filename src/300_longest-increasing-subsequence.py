from typing import List
import heapq

# 1.27 first try，自己30min写的碰到nums = [0,1,0,3,2,3] case 跪了
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_len = 1
        max_hp = [-1 * nums[0]]
        cur_min = nums[0]
        for n in nums[1:]:
            while max_hp and -1 * max_hp[0] >= n:
                heapq.heappop(max_hp)
            heapq.heappush(max_hp, -1 * n)
            cur_min = min(cur_min, n)
            max_len = max(max_len, len(max_hp))
        return max_len

# neetcode的方法是bottom up DP, 类似登台阶，最后一格max_len是1，倒数第二格如果<最后一格那么就是1 + 最后一格max_len, 要么=最后一格max_len
# T O(n^2)因为每一格都要和它后面所有格子比较大小
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cur_max = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    cur_max[i] = max(cur_max[i], 1 + cur_max[j])
        return max(cur_max)