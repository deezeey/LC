from typing import List
# my initial solution, hash map
def majorityElement(nums: list[int]) -> int:
    count = {}
    for v in nums:
        if v in count:
            count[v] += 1
        else:
            count[v] = 1
    return max(count, key=count.get)


# sort
# 因为众数的数量一定大于一半所以sort中间的那个数一定是众数
def majorityElement(nums: list[int]) -> int:
    nums.sort()
    return nums[len(nums)//2]


# boyer-moore voting algo
# [4, 6,| 7, 4,| 3, 7,| 7, 7]
# [3, 2,| 2, 2, 3, 3,| 2]
# [7, 6,| 7, 7, 5, 6,| 6, 7] <---n 7的数量没有过半不符合题目条件
def majorityElement(nums: list[int]) -> int:
    mode = nums[0]
    mode_count = 1
    for i in range(1, len(nums)):
        if mode_count == 0:
            mode = nums[i]
        if nums[i] == mode:
            mode_count += 1
        else:
            mode_count -= 1
    return mode

# 9.24 复习自己写
def majorityElement(nums: list[int]) -> int:
    mode = nums[0]
    count = 1
    for num in nums[1:]:
        if num == mode:
            count += 1
        else:
            count -= 1
        if count == 0:
            mode = num
            count = 1
    return mode


# test
num_list = [3, 2, 3]
print(majorityElement(num_list))

num_list = [4, 6, 7, 4, 3, 7, 7, 7]
print(majorityElement(num_list))

num_list = [3, 2, 2, 2, 3, 3, 2]
print(majorityElement(num_list))

num_list = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(num_list))

num_list = [7, 6, 7, 7, 5, 6, 6, 7]
print(majorityElement(num_list))


# 11.01复习自己写 Boyer's Moore Algorithm --> O(1) Space O(n) Time
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mode_count = 0
        mode = nums[0]
        for num in nums:
            if mode_count == 0:
                mode = num
            if num == mode:
                mode_count += 1
            else:
                mode_count -= 1
                
        return mode