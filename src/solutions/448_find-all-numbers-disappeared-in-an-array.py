from typing import List

def findDisappearedNums(nums: List[int]) -> List[int]:
    for n in nums:
        n = abs(n)
        if nums[n - 1] > 0:
            nums[n - 1] = -nums[n - 1]
    return [i + 1 for i, v in enumerate(nums) if v > 0 ]


def testNormal():
    nums = [4,3,2,7,8,2,3,1]
    assert findDisappearedNums(nums) == [5, 6]

def testEmpty():
    nums = []
    assert findDisappearedNums(nums) == []

def testNoMissing():
    nums = [4,3,6,7,8,2,5,1]
    assert findDisappearedNums(nums) == []