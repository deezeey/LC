from typing import List

# 12.13 first try自己用binary search做出来的
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i1 in range(len(numbers)):
            remain = target - numbers[i1]
            l, r = i1 + 1, len(numbers) - 1
            while l <= r:
                i2 = (l + r) // 2
                if numbers[i2] == remain:
                    return [1 + i1, 1 + i2]
                if numbers[i2] > remain:
                    r = i2 - 1
                else:
                    l = i2 + 1

# neetcode解法，其实双指针移动就行
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]

# 1.4复习，单纯双指针移动
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            res = numbers[l] + numbers[r] 
            if res == target:
                return [l+1, r+1]
            elif res > target:
                r -= 1
            else:
                l += 1