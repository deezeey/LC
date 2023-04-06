from typing import List
# ## my initial solution
# # 有问题，第4 test case会return不正确答案
# def maxProfit(prices: list[int]) -> int:
#     buy_day = cur_buy_day = 0
#     sell_day = cur_sell_day = len(prices) - 1
#     while cur_buy_day < len(prices) - 1 and cur_sell_day > 0:
#         cur_buy_day += 1
#         cur_sell_day -= 1
#         if prices[cur_buy_day] <= prices[buy_day]:
#             buy_day = cur_buy_day
#         else:
#             continue
#         if prices[cur_sell_day] >= prices[sell_day]:
#             sell_day = cur_sell_day
#         else:
#             continue
#     if buy_day < sell_day:
#         print(buy_day, sell_day)
#         return prices[sell_day] - prices[buy_day]
#     else:
#         return 0
#
#
# # 2nd try
# # 有问题，第1 test case会return不正确答案
# def maxProfit(prices: list[int]) -> int:
#     peak = max(prices)
#     peak_day = prices.index(peak)
#
#     if peak_day == 0:
#         return 0
#     else:
#         buy = min(prices[:peak_day])
#         return peak - buy
#
#
# # 3rd try 尝试找peak和bottom做一半放弃了
# def maxProfit(prices: list[int]) -> int:
#     i = 1
#     peaks = {}
#     bottoms = {}
#     for i in range(1, len(prices) - 1):
#         if prices[i - 1] >= prices[i] and prices[i + 1] >= prices[i]:
#             bottoms[i] = prices[i]
#         if prices[i - 1] <= prices[i] and prices[i + 1] <= prices[i]:
#             peaks[i] = prices[i]

# 看答案DP第一解
#  we check the new stock price every day, and calculate how much profit we can get if we sell out today.
#  If it’s larger than our previous calculated profit, then we update Total.
#  Otherwise if today’s price dropped below our buy-in price, then we buy in today (so today’s profit is counted as 0).
# def maxProfit(prices: list[int]) -> int:
#     accumulated_profit, max_profit = 0, 0
#     for i in range(len(prices) - 1):
#         accumulated_profit = max(accumulated_profit + (prices[i + 1] - prices[i]), 0)
#         if accumulated_profit > max_profit:
#             max_profit = accumulated_profit
#     return max_profit

# 更易理解的方案
def maxProfit(prices: list[int]) -> int:
    min_price = prices[0]
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
        elif prices[i] < min_price:
            min_price = prices[i]
    return max_profit

# 9.24 复习自己写
def maxProfit(prices: list[int]) -> int:
    low = prices[0]
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] - low > max_profit:
            max_profit = prices[i] - low
        elif prices[i] < low:
            low = prices[i]
    return max_profit


# test
stock = [7, 1, 5, 3, 6, 4]
print(maxProfit(stock))

stock = [7, 6, 4, 3, 1]
print(maxProfit(stock))

stock = [1, 2, 3, 4, 5, 6]
print(maxProfit(stock))

stock = [7, 5, 3, 7, 18, 7, 2, 5, 6, 9]
print(maxProfit(stock))


# 11.03复习自己写, T O(n) M O(1)
class Solution: 
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        max_profit = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                max_profit = max(prices[r] - prices[l], max_profit)
            r += 1
            
        return max_profit