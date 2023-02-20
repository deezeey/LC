from typing import List

# 1.26 first try自己没想出来如何解决循环问题
# 看了neetcode的解法，基本上把house robber 1的答案做成helper function，然后分别在exclude第一个数字和exclude最后一个数字的array上run一遍，最后比较
# 因为如果rob了第一个房子，就不能rob最后一个房子，如果rob了最后一个，就不能rob第一个，所以得run两遍，看看rob第一个房子和rob最后一个房子分别的max money
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 这个nums[0]存在的意义是为了handle len==1的情况
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            tmp = max(rob2, rob1 + n)
            rob1 = rob2
            rob2 = tmp
        return rob2