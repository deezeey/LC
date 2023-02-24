from typing import List
# 2.21 first try自己能想到思路但是关于如何实现O(1) space不太想得出来
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        left_min, right_max = nums[0], nums[-1]
        left_min_arr = [left_min] * len(nums)
        right_max_arr = [right_max] * len(nums)
        for i in range(1, len(nums)-1):
            left_min_arr[i] = left_min
            left_min = min(left_min, nums[i])
        for j in range(len(nums)-1, -1, -1):
            right_max_arr[j] = right_max
            right_max = max(right_max, nums[j])
        for k, v in enumerate(nums):
            if left_min_arr[k] < v < right_max_arr[k]:
                return True
        return False
    
# 正解写起来非常简单，想起来有点绕
# 举例【20，100，10，12，5， 13】
# 1st = 20, 2nd = 100, 1st = 10, 2nd = 12, first = 5, 13 > 12也 > 5， return True
# 注意虽然5在12右边，但是first = 5， second = 12 也是可以接受的，因为后面的数字要求是比second大。而我们知道因为12是second所以它的左边一定有个数字比他小
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num = float("inf")
        second_num = float("inf")
        for n in nums:
            if n <= first_num: #等号非常重要，因为要handle[1, 1, 1, 1, 1]的情况，那种情况1 = 1会进到else statement里面return True的
                first_num = n
            elif n <= second_num:
                second_num = n
            else: # 当前比first second都大，当然return true
                return True
        return False