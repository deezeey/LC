from typing import List
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        s, e = 0, len(nums)-1
        while s <= e: # <=不是<,这很重要因为当只剩一个数，s会=e，mid=s=e
            mid = (s + e) // 2 # 5//2 = 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                s = mid + 1
            else:
                e = mid - 1
        return -1


# 9.25 复习自己写，粗心导致没pass
def search(self, nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (r - l) // 2 # <---- 想了半天为什么infinite loop，原来这里用的减号
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1


print (5//2)
print (-5//2)

# 11.03 复习自己写 T O(log(n)) M O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums) - 1

        while s <= e:
            mid = (s + e) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                s = mid + 1
            else:
                e = mid - 1

        return -1
