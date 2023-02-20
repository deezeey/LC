from typing import List

# 12.14 first try自己做出来了，我觉得我那个min用的很灵性哈哈哈
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # rotate -> last to first
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[l] < nums[mid] < nums[r]:
                return nums[l]
            elif r - l <= 2:
                return min(nums[l], nums[mid], nums[r])
            elif nums[mid] < nums[l]:
                # pivot in left half
                r = mid
            else:
                # pivot in right half
                l = mid


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start , end = 0 ,len(nums) - 1 
        curr_min = float("inf")
        
        while start  <  end :
            mid = (start + end ) // 2
            curr_min = min(curr_min,nums[mid])
            
            # right has the min 
            if nums[mid] > nums[end]:
                start = mid + 1
                
            # left has the  min 
            else:
                end = mid - 1 
                
        return min(curr_min,nums[start])

# 1.5 复习自己写
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[l] <= nums[mid] <= nums[r]:
                # array is not rotated
                return nums[l]
            elif nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif nums[l] > nums[mid]:
                # pivot in left
                r = mid - 1
            else:
                l = mid + 1