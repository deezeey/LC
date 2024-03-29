from typing import List

# 2.6 first try 15 min 写出来了，感觉思路是对的？
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return 1
#         res = 1
#         i, fill = 1, 1
#         while i < len(nums):
#             if nums[i] != nums[i - 1]:
#                 res += 1
#                 nums[fill] = nums[i]
#                 fill += 1
#             i += 1
#         return res

# # neetcode写的
# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         k = 0
#         i = 0
#         while i < len(nums):
#             val = nums[i]
#             while i + 1 < len(nums) and nums[i + 1] == val:
#                 nums.remove(val)
#                 k += 1
#             i += 1
#         return len(nums)

def removeDupes(nums: List[int]) -> int:
    # non decreasing order
    # remove dupes in-place
    if len(nums) <= 1:
        return len(nums)
    i, fill = 1, 1
    while i < len(nums):
        if nums[i] != nums[i-1]:
            nums[fill] = nums[i]
            fill += 1
        i += 1
    return fill

def test1():
    nums = [0, 0, 1, 1, 1, 2, 3, 3, 4]
    assert removeDupes(nums) == 5
    assert nums[:5] == [0, 1, 2, 3, 4]

def test2():
    nums = [1, 1, 1, 1, 1]
    assert removeDupes(nums) == 1
    assert nums[:1] == [1]

def test3():
    nums = []
    assert removeDupes(nums) == 0