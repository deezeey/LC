from typing import List
# my initial solution
# hashmap
def containsDuplicate(nums: list[int]) -> bool:
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    if all([v == 1 for v in count.values()]):
        return False
    else:
        return True


# one line solution with set
# Time O(n) Space O(n)
def containsDuplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))

# 9.24 复习自己写 刻意没有用set捷径
def containsDuplicate(nums: list[int]) -> bool:
    hash = {}
    for num in nums:
        if num in hash:
            return True
        else:
            hash[num] = 1
    return False

# test
nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums))


nums = [1,3,7,4,8,21,24,32]
print(containsDuplicate(nums))

# 11.01 复习自己写，这个不work，因为set然后再变list可能element的顺序会变的
# 用set也没有那么高效，因为sets are implemented using hashtables, iterating thru the list是O(n)但是如果有hash collision worst case会是O(n^2)
# 具体可以google一下python set function time complexity
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return list(set(nums)) != nums

# 复习自己写第二种，hashmap Time O(n) Space O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for num in nums:
            if num in hash:
                return True
            else:
                hash[num] = 1
        return False