from typing import List
"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, 
return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant extra space.
"""
def findDuplicates(nums: List[int]) -> List[int]:
    # use the array itself to record which ones has been visited
    res = []
    for n in nums:
        n = abs(n)
        if nums[n - 1] < 0:
            res.append(n)
        nums[n - 1] = -nums[n - 1]
    return res

def testEmpty():
    nums = []
    res = findDuplicates(nums)
    assert res == []
def testNoRes():
    nums = [1, 2, 3]
    res = findDuplicates(nums)
    assert res == []
def testNormal():
    nums = [1, 1, 3]
    res = findDuplicates(nums)
    assert res == [1]
def testNormal2():
    nums = [1, 3, 4, 4, 1]
    res = findDuplicates(nums)
    assert set(res) == {1, 4}
