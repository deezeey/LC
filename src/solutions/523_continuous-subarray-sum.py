from typing import List
from collections import defaultdict

# 04.07 first try 用prefix sum做的，过不了test2
# def checkSubarraySum(nums: List[int], k: int) -> bool:
#     """
#     subarray length >= 2, continuous
#     sum of subarray elements is multiple of k, including 0
#     """
#     # build hash map of prefix sum
#     # check hash[n] - hash[n-2....0] is a mutiple of k
#     if len(nums) <= 1:
#         return False
#     prefix_sum_hash = defaultdict(int)
#     prefix_sum = 0
#     for i, v in enumerate(nums):
#         prefix_sum += v
#         if i == 1:
#             if prefix_sum % k == 0:
#                 return True
#         elif i > 1:
#             for j in range(i-1):
#                 interval_sum = prefix_sum - prefix_sum_hash[j]
#                 if interval_sum % k == 0:
#                     return True
#         prefix_sum_hash[i] = prefix_sum
#     return False

# M O(n) T O(n)
def checkSubarraySum(nums: List[int], k: int) -> bool:
    modulo_hash = {}
    modulo_hash[0] = 0
    prefix_sum = 0
    for i, v in enumerate(nums):
        prefix_sum += v
        modulo = prefix_sum % k
        if modulo not in modulo_hash:
            modulo_hash[modulo] = i + 1
        else:
            j = modulo_hash[modulo]
            if i - j:
                return True
    return False

def test1():
    assert checkSubarraySum([23, 2, 4, 6, 7], 6) == True
def test2():
    assert checkSubarraySum([23, 2, 4, 6, 6], 7) == True
def test3():
    assert checkSubarraySum([23, 2, 6, 4, 7], 13) == False
def test4():
    assert checkSubarraySum([5, 0, 0, 0], 5) == True
