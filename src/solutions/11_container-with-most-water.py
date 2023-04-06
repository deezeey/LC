from typing import List

# 10.11 first try, 自己想出了最优解
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_volume = 0

        while l < r:
            width = r - l
            min_height = min(height[l], height[r])
            if width * min_height > max_volume:
                max_volume = width * min_height
            if height[l] < height[r]: # Say height[0] < height[5], area of (0, 4), (0, 3), (0, 2), (0, 1) will be smaller than (0, 5), so no need to try them
                l += 1
            else:
                r -= 1
        
        return max_volume

# 11.06 复习 T O(n) M O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_vol = 0

        while l < r:
            cur_vol = (r - l) * min(height[l], height[r])
            max_vol = max(cur_vol, max_vol)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_vol

# 12.13 复习自己还记得
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0
        l, r = 0, len(height) - 1
        while l < r:
            if height[l] < height[r]:
                max_vol = max(max_vol, height[l] * (r - l))
                l += 1
            else:
                max_vol = max(max_vol, height[r] * (r - l))
                r -= 1
        return max_vol
