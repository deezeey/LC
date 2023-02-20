from typing import List

# 10.22 first try 自己毫无思路，看了neet code的思路也理解了半天才找到规律自己写出这个解
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]

        max_area = 0
        stack = [] # [(index, height)...]

        def checkAreaForCurStack(cur_index):
            nonlocal max_area
            bar_to_check = stack.pop()
            bar_index, bar_height = bar_to_check[0], bar_to_check[1]
            area_at_bar_height = (cur_index - bar_index) * bar_height
            if area_at_bar_height > max_area:
                max_area = area_at_bar_height
            return bar_index

        for i in range(len(heights)):
            cur_index = i
            cur_height = heights[i]
            prev_height = stack[-1][1] if stack else 0

            if cur_height >= prev_height:
                stack.append((cur_index, cur_height))
            else:
                while stack and stack[-1][1] > cur_height:
                    bar_index = checkAreaForCurStack(cur_index)
                stack.append((bar_index, cur_height))

        while stack:
            cur_index = len(heights)
            checkAreaForCurStack(cur_index)

        return max_area


# 相同思路neet code写的非常简洁
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights): #首先我又忘记用enumerate
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index)) # 然后用max可以省一行if statement
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea


# retouch了一下自己的代码，简洁一些了
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]

        max_area = 0
        stack = [] # [(index, height)...]

        def checkAreaForCurStack(cur_index):
            nonlocal max_area
            bar_to_check = stack.pop()
            bar_index, bar_height = bar_to_check[0], bar_to_check[1]
            area_at_bar_height = (cur_index - bar_index) * bar_height
            max_area = max(area_at_bar_height, max_area)
            return bar_index

        for cur_index, cur_height in enumerate(heights):
            bar_index = cur_index
            while stack and stack[-1][1] > cur_height:
                bar_index = checkAreaForCurStack(cur_index)
            stack.append((bar_index, cur_height))

        while stack:
            cur_index = len(heights)
            checkAreaForCurStack(cur_index)

        return max_area
        

# 11.03 复习自己写，这回自己写的很简洁 T O(n) M O(n)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]

        records = [(0, heights[0])] # stores (i, height), i is the leftmost index this height can go to
        maxVolume = heights[0]

        for i in range(len(heights))[1:]:
            leftmost_index = i
            while records and heights[i] <= records[-1][1]:
                cur = records.pop()
                maxVolume = max(maxVolume, (i-cur[0]) * cur[1])
                leftmost_index = cur[0]
            records.append((leftmost_index, heights[i]))
        
        cur_index = len(heights) - 1
        while records:
            cur = records.pop() #对比一下neet code发现此处已经没有必要从后往前pop，从前往后每个element都算+比较一遍maxVolume就行了
            maxVolume = max(maxVolume, (cur_index-cur[0]+1) * cur[1])
        
        return maxVolume