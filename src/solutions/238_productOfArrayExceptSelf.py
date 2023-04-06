from typing import List
def solution(nums:list[int]) -> list[int]:
    answer = [1] * len(nums)
    N = len(nums)
    prefix = 1
    for i in range(N):
        answer[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(N-1, -1, -1):
        answer *= postfix
        postfix *= nums[i]
    return answer

# 9.25 复习自己的解
def productExceptSelf(nums: list[int]) -> list[int]:
    N = len(nums)
    pre = [1] * N
    post = [1] * N
    for i in range(N):
        if i > 0:
            pre[i] = pre[i-1] * nums[i-1]
    for j in range(N-1, -1, -1):
        if j < N-1:
            post[j] = post[j+1] * nums[j+1]
    res = [a * b for a, b in zip(pre, post)]
    return res

# 11.01 复习自己一开始没想出来，看了一眼答案写出来了。T O(N) M O(1)
# 一开始就是没想出来怎样可以O(1)，后来发现result不算占memory
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        for i in range(len(nums))[1:]:
            # res[i] stores the product of everything to its left
            res[i] = nums[i-1] * res[i-1]

        tmp = 1
        for j in range(len(nums) - 2, -1, -1):
            # tmp is the product of everything to its right
            # we don't need to do *= for the last element in nums b/c the res for it should be everything to its left
            tmp *= nums[j+1]
            res[j] *= tmp

        return res


# 12.02 复习自己记得算法
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,3,4]
        # [1,1,2,6] left to right
        # [24,23,4,1] right to left
        # iterate thru nums from left to right then right to left
        res = [1]
        cur = 1
        for i in range(1, len(nums)):
            cur = cur * nums[i - 1]
            res.append(cur)

        cur = 1
        for i in range(len(res) - 2, -1, -1):
            cur = cur * nums[i + 1]
            res[i] = res[i] * cur
            
        return res