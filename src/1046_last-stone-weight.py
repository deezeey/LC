from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -1 * heapq.heappop(stones)
            y = -1 * heapq.heappop(stones)
            if x == y:
                continue
            else:
                heapq.heappush(stones, - abs(x - y))
        
        return abs(stones[0]) if stones else 0

# neetcode写法其实差不多
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            y, x = -1 * heapq.heappop(stones), -1 * heapq.heappop(stones)
            if x == y:
                continue
            else:
                heapq.heappush(stones, - 1 * (y - x))
        return -1 * stones[0] if stones else 0