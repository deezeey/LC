from typing import List

def replaceElements(nums: List[int]) -> List[int]:
    if not nums:
        return nums
    cur_max = -1
    for i in range(len(nums) - 1, -1, -1):
        tmp = nums[i]
        nums[i] = cur_max
        cur_max = max(cur_max, tmp)
    return nums

def test1():
    nums = [17,18,5,4,6,1]
    replaceElements(nums)
    assert nums == [18,6,6,6,1,-1]

def testEmpty():
    nums = []
    replaceElements(nums)
    assert nums == []