from typing import List
# 1.26 first try, 跑回去看了下70 climbing stairs就在10分钟内做出来了
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        min_cost = [0] * len(cost)
        min_cost[-1], min_cost[-2] = cost[-1], cost[-2]
        for i in range(N-2)[::-1]:
            min_cost[i] = min([min_cost[i+1] + cost[i], min_cost[i+2] + cost[i]])
        return min([min_cost[0], min_cost[1]])