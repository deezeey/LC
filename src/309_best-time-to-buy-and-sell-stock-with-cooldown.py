from typing import List

# 1.27 first try自己是有思路的但是在grid search部分如何实现有点脑子懵
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy/idle | sell | idle
        # sell/idle | buy | sell/idle
        # build profit grid
        N = len(prices)
        prof_grid = [[0] * N for _ in range(N)]
        for sell in range(N):
            for buy in range(N):
                if sell > buy:
                    prof_grid[sell][buy] = prices[sell] - prices[buy]
        
        # if I take the prof from grid[i][j], next search from [i+2][j+1]
        max_prof, cur_prof = 0, 0
        available_day = 0
        for r in range(1, N):
            for c in range(N - 1):
                if prof_grid[r][c] <= 0 or r < available_day or c < available_day:
                    continue
                cur_prof += prof_grid[r][c]
                max_prof = max(max_prof, cur_prof)
                available_day = r + 2
                if r >= N or c >= N - 1:
                    break
        return max_prof

# neetcode的dfs + dp 没太看明白
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: Buying or Selling?
        # If Buy -> i + 1
        # If Sell -> i + 2

        dp = {}  # key=(i, buying) val=max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)

# 官方解法state machine，详情看pic。
# 3个array里存储的都是当天([i])做出此选择（sold,held,reset)的accumulated最大利润（比较所有前一天可能的选择情况—）。
# 要注意额是没有今天什么都没做但手里有票的情况，这个算在held里，然后今天手里没票的情况分成今天什么都没做和今天卖了。
# 这个之所以是STATE MACHINE而不是ACTION MACHINE是有讲究的。action lead to state。我们initiate array是根据state来initiate而不是action。
# 最重要的是下面的公式总结：
# sold[i]=hold[i−1]+price[i] sold即今天卖掉了手里没票，今天的利润只能是前一天手里有票（held）情况的最大利润加上今天卖掉赚的钱，注意买进成本已经包括在hold【i-1】里所以直接加上今天的price就好
# held[i]=max(held[i−1],reset[i−1]−price[i]) 今天手里有票，可能前一天手里有票今天啥都没干，也可能前一天手里就没票了今天才买，即reset【i-1】- price【i】，在cooldown。所以最大利润是这两个取max
# reset[i]=max(reset[i−1],sold[i−1]) reset代表今天什么都没做且手里没票,可能前一天是刚卖掉，或者前一天也在cooldown，注意reset不可能前一天是买，因为如果前一天买了今天手里一定有票
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sold, held, reset = float('-inf'), float('-inf'), 0

        for price in prices:
            # Alternative: the calculation is done in parallel.
            # Therefore no need to keep temporary variables
            #sold, held, reset = held + price, max(held, reset-price), max(reset, sold)

            pre_sold = sold
            sold = held + price
            held = max(held, reset - price)
            reset = max(reset, pre_sold)

        return max(sold, reset)
