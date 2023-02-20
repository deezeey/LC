from typing import List

# 10.05 first try, 自己思路和neetcode完全一样但是stackoverflow. 百思不得其解以后发现是两个if导致的问题，
# 因为假设mid <= b, pivot is in left half, 但是我们要搜的target在right half里，
# 这时候进入right half搜索，整个right half是well sorted，就不会再有pivot了，那么两个if条件句都进不去，while loop就会被挂起
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        b, e  = 0, len(nums) - 1
        while b <= e:
            mid = (b + e) // 2
            if nums[mid] == target:
                return mid
                
            if nums[mid] <= nums[b]: # <--- pivot in left half
                if target > nums[e] or target < nums[mid]:
                    e = mid - 1
                else:
                    b = mid + 1
            if nums[mid] >= nums[e]: # <--- pivot in right half, 这样写过不了，把整行删掉换成else就能过
                if target < nums[b] or target > nums[mid]:
                    b = mid + 1
                else:
                    e = mid - 1
        return -1


# neetcode写法
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


# 11.05 复习，又没写出来
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [4,5,6,7,0,1,2] 0
        # [4,5,6,7][0,1,2]
        # break the array into two sub arrays
        # if l > r then pivot is in this sub array
        # sub array is either sorted or pivoted
        # if sorted then do binary search
        # if not sorted then do recursion
        def binarySearch(l, r):
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if nums[r] > nums[l]:
                while l <= r:
                    mid = (r + l)//2
                    if nums[mid] == target:
                        return mid
                    if nums[mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
            else:
                mid = (r + l)//2
                if nums[mid] == target:
                    return mid
                binarySearch(l, mid)
                binarySearch(mid + 1, r)
            return -1

        return binarySearch(0, len(nums) - 1)

# 看答案又默了一遍 T O(logn) M O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[r]: # <--- pivot in right half, left half must be sorted
                if nums[l] > target or nums[mid] < target: 
                    # if target is not in the sorted part, next search the other part
                    l = mid + 1
                else:
                    r = mid - 1
            else: # <--- pivot in left half, or both left & right are sorted
                if nums[mid] > target or nums[r] < target:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
        

# 12.12 复习，自己记得算法但是写出来的这个代码碰到[5, 1, 3] target=0时候 stackoverflow
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[l]:
                # right is sorted, pivot in left
                if nums[mid] < target and nums[r] >= target:
                    r = mid + 1  # <--- 第二天脑子清醒点了检查一下发现就是这行写错了，这里应该是 l = mid + 1
                else:
                    l = mid - 1
            elif nums[mid] > nums[r]:
                # left is sorted, pivot in right
                if nums[l] <= target and nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # entire array is sorted
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

# 第二天脑子清醒了点，调整了一下，过了
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[l]:
                # right is sorted, pivot in left
                if nums[mid] < target and nums[r] >= target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # left is sorted, pivot in right, or entire thing is sorted
                if nums[l] <= target and nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

# 12.15 复习，很快写出来了
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] > nums[mid]:
                # pivot in left, right is sorted
                if nums[mid] < target <= nums[r]: #一开始忘了这里 target可以 = num[r]， 写target < nums[r]是过不了的
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # pivot in right or no pivot, either way left should be sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1