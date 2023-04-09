from typing import List

def concatenateArrays(nums: List[int]) -> List[int]:
    return nums + nums

def test1():
    nums = [1, 2, 1]
    assert concatenateArrays(nums) == [1, 2, 1, 1, 2, 1]