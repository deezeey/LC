from typing import List
from collections import defaultdict

# 12.06 first try 自己写的这个碰到[0,1,2,4,8,5,6,7,9,3,55,88,77,99,999999999]时候memory limit exceeded
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        d_hash = defaultdict(int)
        for val in range(min(nums), max(nums) + 1):
            d_hash[val] = 0

        for d in nums:
            d_hash[d] = 1
        
        max_length, cur_length = 0, 0
        for k, v in d_hash.items():
            if not v: 
                cur_length = 0
            else:
                cur_length += 1
                max_length = max(max_length, cur_length)
        
        return max_length


# 看了neet code讲解。我一开始想到了look up d - 1和 d + 1但是我以为这个不会是O(n) time
# 后来发现，只要转化成set，lookup / insert / delete都是O(1)的操作
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinct = set(nums)
        max_length = 0

        for d in distinct:
            if d - 1 not in distinct:
                cur_length = 1
                while d + 1 in distinct:
                    cur_length += 1
                    d += 1
                max_length = max(max_length, cur_length)
        
        return max_length


# 复习自己写，忘记可以用set，看了提示以后写出来这个，还是TLE。就是说忘了 if num - 1 not in nums这个条件来check是不是begin of the seq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums = set(nums)
        max_res = 1
        for num in nums:
            res = 1
            while num + 1 in nums:
                res += 1
                num = num + 1
            max_res = max(max_res, res)
        
        return max_res

# 12.15 复习还记得
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for n in nums:
            cur_len = 1
            if n - 1 in nums:
                continue
            while n + 1 in nums:
                cur_len += 1
                n += 1 #一开始漏了这个stack over flow
            res = max(res, cur_len)
        
        return res

# 1.2 复习
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        cur, max_length = 0, 0
        for num in nums:
            if num - 1 in nums:
                continue
            else:
                cur += 1
                while num + 1 in nums:
                    num += 1 # 这行一开始漏了stackoverflow
                    cur += 1
                max_length = max(max_length, cur)
                cur = 0 #这行一开始也漏了会产生错误结果
                
        return max_length