from typing import List
from collections import deque

# 12.14 first try 在40/51 TLE了。我觉得如果是这个解法那这个题应该不至于是hard呀？
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]: 
        l, r = 0, k - 1
        res = []
        prev_max = (max(nums[l:r+1]), nums.index(max(nums[l:r+1])))
        res.append(prev_max[0])

        while r < len(nums) - 1:
            l += 1
            r += 1
            if nums[r] >= prev_max[0]:
                res.append(nums[r])
                prev_max = (nums[r], r)
            elif nums[r] < prev_max[0] and l <= prev_max[1]:
                res.append(prev_max[0])
            else:
                prev_max = (max(nums[l:r+1]), nums.index(max(nums[l:r+1])))
                res.append(prev_max[0])
        
        return res

# neetcode解法
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # index
        l = r = 0
        # O(n) O(n)
        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output

# 重新默了一遍，算法理解起来中等难度但是代码有点难理顺 O(n) O(n)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        deq = deque() #index
        l = r = 0

        while r < len(nums):
            if deq and l > deq[0]:
            # if leftmost(greatest) element is out of left bound, it has to be poped
                deq.popleft()

            while deq and nums[r] > nums[deq[-1]]:
            # we want our deque to maintain a decreasing state
                deq.pop()
            deq.append(r)

            if r - k + 1 >= 0:
            # since window length becomes >= k, we start to move l and append result
                l += 1
                res.append(nums[deq[0]])
                # leftmost element from the q will always be the greatest
            r += 1
        
        return res

# 1.6 复习不记得算法了，又看了一遍neetcode才看明白，而且这个代码是有点难写的。逻辑比较绕。
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        deq = deque()
        res = []

        while r < len(nums):
            if deq and l > deq[0]:
                deq.popleft()
            while deq and nums[deq[-1]] <= nums[r]:
                deq.pop()
            deq.append(r)
            if r + 1 >= k:
                res.append(nums[deq[0]])
                l += 1
            r += 1

        return res