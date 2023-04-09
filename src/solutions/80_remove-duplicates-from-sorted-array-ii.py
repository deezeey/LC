from typing import List
from collections import defaultdict

# 04.07 first try没记住题目要保持顺序
# def removeDuplicatesii(nums: List[int]) -> int:
#     # need a hash to store element freq
#     # swap with last element if hash[num] == 2
#     if not nums:
#         return 0
#     l, r = 0, len(nums) - 1
#     freq_hash = defaultdict(int)
#     while l <= r:
#         if freq_hash[nums[l]] == 2:
#             nums[l], nums[r] = nums[r], nums[l]
#             r -= 1
#         else:
#             freq_hash[nums[l]] += 1
#             l += 1
#     return l

# 2nd try, 需要额外空间给hash，不是最优解
# def removeDuplicatesii(nums: List[int]) -> int:
#     if len(nums) <= 1:
#         return len(nums)
    
#     i, fill = 1, 1
#     freq_hash = defaultdict(int)
#     freq_hash[nums[0]] = 1
#     while i < len(nums):
#         if freq_hash[nums[fill]] == 2:
#             while i < len(nums) and freq_hash[nums[i]] == 2:
#                 i += 1
#             if i == len(nums):
#                 break
#             nums[i], nums[fill] = nums[fill], nums[i]
#             freq_hash[nums[fill]] += 1
#         else:
#             freq_hash[nums[fill]] += 1
#         i += 1
#         fill += 1
#     return fill

# 官方最优解O(1)
def removeDuplicatesii(nums: List[int]) -> int:
    if len(nums) <= 1:
        return len(nums)
    fill, count = 1, 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            count += 1
        else:
            count = 1
        if count <= 2:
            nums[fill] = nums[i]
            fill += 1
    return fill

def testEmpty():
    nums = []
    res = removeDuplicatesii(nums)
    assert res == 0
    assert nums == []
def testAllDupes():
    nums = [1, 1, 1, 1]
    res = removeDuplicatesii(nums)
    assert res == 2
    assert nums[:2] == [1, 1]
def testNormal():
    nums = [1, 2, 2, 2, 3, 3]
    res = removeDuplicatesii(nums)
    assert res == 5
    assert nums[:res].count(2) == 2
def testNormal2():
    nums = [0,0,1,1,1,1,2,3,3]
    res = removeDuplicatesii(nums)
    assert res == 7
    assert nums[:res].count(1) == 2