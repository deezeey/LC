from typing import List

# 2.9 first try, 买卖股票的题，2比1简单？
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            day_profit = prices[i] - prices[i-1]
            if day_profit > 0:
                res += day_profit
        return res