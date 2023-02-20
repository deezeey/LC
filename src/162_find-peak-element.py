from typing import List

# 2.9 first try看到题目要求logn time就知道一定是binary search
# 但是自己怎么也没想明白为啥这题可以用binary search
# 大概可能就是因为只要找到其中一个peak，并且一直上坡的话，找到最右边的终点也可以。所以才可以用binary search的
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
        return r #这里return l或者r都无所谓因为跳出while loop时候l，r是重和的