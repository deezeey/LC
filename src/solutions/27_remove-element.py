from typing import List
"""
Given an integer array nums and an integer val, 
remove all occurrences of val in nums in-place. 
The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
"""
# 4.07 first try two pointers
# def removeElements(nums: List[int], val:int) -> int:
#     i, fill = 0, 0
#     while i < len(nums):
#         if nums[fill] != val:
#             fill += 1
#         else:
#             while i < len(nums) and nums[i] == val:
#                 i += 1
#             if i == len(nums):
#                 break
#             nums[i], nums[fill] = nums[fill], nums[i]
#             fill += 1
#         i += 1
#     return fill

def removeElements(nums: List[int], val:int) -> int:
    i, n = 0, len(nums) - 1
    while i <= n:
        if nums[i] == val:
            nums[i], nums[n] = nums[n], nums[i]
            n -= 1
        if nums[i] != val:
            i += 1
    return i

def testEmpty():
    arr = []
    val = 0
    assert removeElements(arr, val) == 0
    assert arr == []
def testNormal():
    arr = [1, 2, 3, 3, 2, 4]
    val = 3
    assert removeElements(arr, val) == 4
    assert 3 not in arr[:4] 
def testAllDupes():
    arr = [1, 1, 1, 1]
    val = 1
    assert removeElements(arr, val) == 0
    assert arr == [1, 1, 1, 1]