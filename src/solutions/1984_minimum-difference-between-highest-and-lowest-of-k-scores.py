from typing import List
import heapq

# 04/08 first try 太晚了脑子不太清醒了能过35 cases
# def minimumDifference(nums: List[int], k: int) -> int:
#     if len(nums) <= 1 or k == 1:
#         return 0
#     nums.sort()
#     gap_heap = []
#     for i in range(1, len(nums)):
#         gap_heap.append(nums[i] - nums[i-1])
#     heapq.heapify(gap_heap)
#     res = 0
#     k = k - 1
#     while k > 0:
#         res += heapq.heappop(gap_heap)
#         k -= 1
#     return res

def minimumDifference(nums: List[int], k: int) -> int:
    nums.sort()    
    k -= 1
    min_diff = float('inf')
    for i in range(len(nums)-k):
        min_diff = min(min_diff, nums[i+k]-nums[i])
    
    return min_diff

def test1():
    nums = [90]
    k = 1
    assert minimumDifference(nums, k) == 0

def test2():
    nums = [9,4,1,7]
    k = 2
    assert minimumDifference(nums, k) == 2

