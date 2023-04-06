from typing import List
import math

# 12.13 first try, 自己感觉摸到了数学方法的一点边但是20分钟没写出来就放弃了，就是说 h / len(piles)这个平均每堆吃几次很重要
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:        
        if len(piles) == h:
            return max(piles)
        
        piles.sort()
        x = h // len(piles)
        remainder = h % len(piles)

        tmp_k = [-(p / -x) for p in piles]

        if remainder:
            k = min(tmp_k[remainder], max())

# 看了neetcode讲解后自己做出来了
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:        
        if len(piles) == h:
            return max(piles)
        
        res = max(piles)
        l, r = 1, max(piles)
        while l <= r:
            m = (l + r) // 2
            h_sum = 0
            for p in piles:
                h_sum += math.ceil(p / m)
            if h_sum <= h:
                res = m
                r = m - 1
            else:
                l = m + 1

        return res

# 1.5 复习自己不记得了，自己写的解法在106/122 TLE了
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = len(piles)
        avg_h = h / l
        k = math.ceil(max(piles) / avg_h)

        while True:
            k -= 1
            if k == 0 or sum([math.ceil(p / k) for p in piles]) > h:
                k += 1
                break

        return k

# 1.9 复习，这回记得是binary search了但是一开始逻辑还写反了
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2
            s = sum([math.ceil(p / m) for p in piles])
            if s <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res