from typing import List
from collections import defaultdict
from functools import lru_cache

# # 3.10 first try TLE
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         # [1, 1, 2, 2, 1, 1, 3], k = 4
#         # recursion + memoization
#         @lru_cache(maxsize=None)
#         def _arrSumAnyStart(s, target) -> int:
#             if s == len(nums):
#                 return 0
#             cur_res = 1 if nums[s] == target else 0
#             return cur_res + _arrSumStartFromLeft(s+1, target-nums[s]) + _arrSumAnyStart(s+1, target)

#         @lru_cache(maxsize=None)
#         def _arrSumStartFromLeft(s, target) -> int:
#             if s == len(nums):
#                 return 0
#             if nums[s] == target:
#                 return 1 + _arrSumStartFromLeft(s+1, 0)
#             else:
#                 return _arrSumStartFromLeft(s+1, target-nums[s])

#         return _arrSumAnyStart(0, k)
    
# # 正解，prefix sum + hash map， T O(n), M O(n)
# # 如果第3位的prefix sum = 3， 第8位的prefix sum = 8， 而k = 5， 那代表第4位到第7位的和一定是等于k的
# # 所以我们每前进一位找到新的prefix sum时候，就回去看一眼hashmap里有没有prefix sum = cur prefix sum - k的，有几个这样的prefix sum，就代表，会有几个以当前位为截止位的解
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         # [1, 1, 2, 2, 1, 1, 3], k = 4
#         # prefix sum?
#         # iterate from left to right to get prefixes, and maintain a hashmap of {prefix_sum: time this sum appeared in arr}
#         # if cur prefix_sum - k is already in hashmap, it means using cur prefix sum - some prev prefix sum would get us an interval sum equals k, res += 1
#         prefix_sum_hash = defaultdict(int)
#         prefix_sum_hash[0] = 1
#         prefix_sum, res = 0, 0
#         for n in nums:
#             prefix_sum += n
#             search_sum = prefix_sum - k
#             if search_sum in prefix_sum_hash:
#                 res += prefix_sum_hash[search_sum]
#             prefix_sum_hash[prefix_sum] += 1
#         return res

def subarraySum(nums: List[int], k:int) -> int:
    # we can not jump over numbers
    # prefix sum
    prefix_sum_hash = defaultdict(int) # prefix_sum : way to form this prefix_sum
    prefix_sum_hash[0] = 1 # there's one way to form 0 by not choosing anything
    cur_prefix_sum, res = 0, 0
    for n in nums:
        cur_prefix_sum += n
        search = cur_prefix_sum - k
        if search in prefix_sum_hash:
            res += prefix_sum_hash[search]
        prefix_sum_hash[cur_prefix_sum] += 1
    return res

def test1():
    assert subarraySum([1, 2, 3], 3) == 2

def test2():
    assert subarraySum([], 0) == 0

def test3():
    assert subarraySum([1], 1) == 1

def test4():
    assert subarraySum([-1, 1, 0, 1, -1], 0) == 6