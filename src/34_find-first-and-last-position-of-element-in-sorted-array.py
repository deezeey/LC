from typing import List

# 2.8 first try. 只做了一半binary search但是后半部分那两个while loop不是很efficient technically还是可以到O(n)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s, e = -1, -1
        # binary search
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                s, e = mid, mid
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        while s - 1 >= 0 and nums[s - 1] == target:
            s -= 1
        while e + 1 < len(nums) and nums[e + 1] == target:
            e += 1
        return [s, e]

# 正确的做法是做2遍binary search，找到=target的中点之后，一个往左找到leftmost index，一个往右找到rightmost index然后整合起来
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, target, left):
            l, r, i = 0, len(nums) - 1, -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    i = mid
                    if left:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return i

        left = binarySearch(nums, target, True)
        right = binarySearch(nums, target, False)
        return [left, right]