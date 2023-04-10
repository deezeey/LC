from typing import List

# # 04/10 first try自己用prefix sum 30min做出来的
# def minSubArrLen(nums: List[int], target: int) -> int:
#     # if sum of nums < target: return 0
#     # if any element of nums >= target: return 1
#     # [2, 3, 3, 4, 2, 1]
#     # [0, 2, 5, 8, 12, 14, 15]
#     # [-7, -5, -2, 1, 5, 7, 8] search
#     # [0, 0, 0, 3, 2,  ]
#     if not nums or sum(nums) < target: return 0
    
#     # calc prefix sum and store in original list
#     cur_sum = 0
#     for i, v in enumerate(nums):
#         if v >= target:
#             return 1
#         else:
#             cur_sum += v
#             nums[i] = cur_sum
#     nums = [0] + nums

#     ptr, max_len = 0, float("inf")
#     for j, prefix_sum in enumerate(nums):
#         search = prefix_sum - target
#         while ptr < len(nums) and nums[ptr] <= search:
#             ptr += 1
#         if ptr:
#             max_len = min(max_len, j - ptr + 1)

#     return max_len if max_len != float("inf") else 0

# 正解也差不多的思路但是用2pointers更简单
def minSubArrLen(nums: List[int], target: int) -> int:
    l, r = 0, 0
    cur_sum, max_len = 0, float("inf")
    while r < len(nums):
        cur_sum += nums[r]
        while cur_sum >= target:
            max_len = min(max_len, r - l + 1)
            cur_sum -= nums[l]
            l += 1
        r += 1
    return max_len if max_len != float("inf") else 0

def test_Empty():
    nums = []
    target = 0
    assert minSubArrLen(nums, target) == 0

def test_Normal():
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    assert minSubArrLen(nums, target) == 2

def test_Normal2():
    nums = [2, 3, 1, 2, 4, 7]
    target = 7
    assert minSubArrLen(nums, target) == 1

def test_NoRes():
    nums = [1, 2, 3]
    target = 8
    assert minSubArrLen(nums, target) == 0
