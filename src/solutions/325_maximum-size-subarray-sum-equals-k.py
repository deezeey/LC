from typing import List

def maxSubArrLen(nums: List[int], k: int) -> int:
    # calc prefix sum and build a hashmap of {prefix sum: indices}
    prefix_sum_hash = {}
    prefix_sum_hash[0] = -1
    cur_sum = 0
    for i, v in enumerate(nums):
        cur_sum += v
        nums[i] = cur_sum
        if cur_sum not in prefix_sum_hash: # we just need to remember the earliest occurance
            prefix_sum_hash[cur_sum] = i

    # iterate through the prefix sum array and search if k - prefix sum exist in hashmap
    # if exist, then 1 + cur prefix sum index - index popped from min_heap of key: k - prefix sum, would be the maxLen to compare
    maxLen = 0
    for i, prefix_sum in enumerate(nums):
        search = prefix_sum - k
        if search in prefix_sum_hash:
            maxLen = max(maxLen, i - prefix_sum_hash[search])
    return maxLen

def testEmpty():
    nums = []
    assert maxSubArrLen(nums, 8) == 0
    
def testNoRes():
    nums = [2, 3, 2, 9, 10]
    assert maxSubArrLen(nums, 8) == 0

def testNegative():
    nums = [-2, -1, 2, 1]
    assert maxSubArrLen(nums, 1) == 2

def testNormal2():
    nums = [2, 3, 4, 9, 10]
    assert maxSubArrLen(nums, 9) == 3

def test0():
    nums = [2, -2, 0, 0, 0]
    assert maxSubArrLen(nums, 0) == 5
