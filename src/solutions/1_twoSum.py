from typing import List

# my initial solution
def twoSum(nums: list, target: int) -> list:
    i = 0
    while i < len(nums):
        otherNum = target - nums[i]
        try:
            j = nums.index(otherNum, i + 1, len(nums))
        except ValueError:
            j = -1
        if j == -1:
            i += 1
        else:
            return [i, j]
    return []


# my solution with hashmap hint
def twoSum(nums: list, target: int) -> list:
    seen = {}
    for i in range(len(nums)):
        number = nums[i]
        remaining = target - number
        if remaining in seen.keys():
            return [seen[remaining], i]
        else:
            seen[number] = i
    return []


# fastest solution online with hashmap
def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}
    # 用了enumerate instead of iterating indices manually
    for i, v in enumerate(nums):
        remaining = target - v
        # 没有用seen.keys() which instantiate a new var
        if remaining in seen:
            return [seen[remaining], i]
        else:
            seen[v] = i
    return []


# another solution online with hashmap, harder to understand but looks memory wise it's better
def twoSum(nums: list[int], target: int) -> list[int]:
    number_bonds = {}
    for index, value in enumerate(nums):
        print(index, value)
        if value in number_bonds:
            return [number_bonds[value], index]
        # 相当于存remaining和number的index，然后等for loop到number = old remaining时候，
        # 就可以return number的index和old remaining在nums里的index
        number_bonds[target - value] = index
        print(number_bonds)
    return None


#################################
# 8.1 复习
def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, v in enumerate(nums):
        remaining = target - v
        if remaining in seen:
            return [seen[remaining], i]
        else:
            seen[v] = i
    return []

#################################
# 9.24 复习自己写的错误答案
# [3,2,4], target = 6 return了[0,0], 应该要return [1，2]
def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i in range(len(nums)):
        if nums[i] not in seen:
            seen[nums[i]] = i  # <------- 错在在检查remaining return res之前先append了nums[i]
            remaining = target - nums[i]
            if remaining in seen:
                return [i, seen[remaining]]
    return []


# test
nums = [-1, -2, -3, -4, -5]
target = -8
print(twoSum(nums, target))

nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))

nums = [3, 3]
target = 6
print(twoSum(nums, target))

nums = [3, 4, 5]
target = 6
print(twoSum(nums, target))


# 11.01 复习自己写的, T O(n) M O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in seen:
                return [seen[remaining], i]
            else:
                seen[nums[i]] = i
        return []
