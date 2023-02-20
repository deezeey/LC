from typing import List
# 1.31 first try 自己15min写出来的，能过但不是很efficient
class Solution:
    def jump(self, nums: List[int]) -> int:
        min_steps = [float("inf")] * len(nums)
        min_steps[-1] = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == 0:
                continue
            if i + nums[i] >= len(nums) - 1:
                min_steps[i] = 1
                continue
            j = 0
            min_at_i = min_steps[i]
            while j <= nums[i] and i + j < len(nums):
                min_at_i = min(min_at_i, min_steps[i + j] + 1)
                j += 1
            min_steps[i] = min_at_i

        return min_steps[0]

# greedy 解法 O(n), 上面自己写的DP是O(n^2)
# 把它可以想成level order traversal BFS
# [2,3,1,1,4] ， 0 step可以reach第一层[2], 1 step 可以reach第二层[3, 1], 2 steps 可以reach第三层[1, 4]
class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < (len(nums) - 1):     # 一旦这层interval的right bound超过了最后一位即代表我们已经可以到达end，loop停止
            maxJump = 0                # 用第二层来举例
            for i in range(l, r + 1):  # for i in range(1, 3)
                maxJump = max(maxJump, i + nums[i])  # maxJump = max(1, 1+3), maxJump = max(2, 2+1), so maxJump = 4
            l = r + 1 
            r = maxJump
            res += 1
        return res
# 可能会好奇如果有一位num是0怎么办。比如[2,3,0,1,4]，第二层是[3, 0], l,r 分别是1，2。maxJump会是max(0, 1+3) 和 max(4, 2+0), 还会是4。
# 题目guarantee能走到结尾的，所以不可能出现整层都是0的情况，下一层一定至少比这一层move 1位，最多下一层l = r = cur_l + 1而已