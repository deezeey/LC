from typing import List
# 自己有思路但是不清晰所以随便写一下recursion，当然time limit exceeded。。
# 自己的思路是，先在coins array里找到小于amount的最大面值coin然后amount减去coin面值然后往下找，kinda dfs
# 但是如果是【1， 3， 4，5】要凑成7, 答案不会是 5，1，1,会是4，3, 只要2个硬币
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)     
        selected_coin_count = 0

        def countCoins(coins, amount):
            nonlocal selected_coin_count
            if amount == 0:
                return 0
            while amount >= 0:
                for coin in coins:
                    if coin == amount:
                        return 1
                    if coin > amount:
                        pass
                    if coin < amount:
                        selected_coin_count += 1
                        selected_coin_count += countCoins(coins, amount-coin)
        
        countCoins(coins, amount)

        return selected_coin_count


# neetcode的解法，自己看完能默出来，但是一开始加了comment out那几行就不对
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 假设 coins[1, 3, 4, 5], amount = 7
        dp = [amount + 1] * (amount + 1) # <--- instantiate一个数列来记录从0-7的每个amount至少需要几个coins里的硬币，init的值设为amount + 1是因为我们知道to form amount，最多就是take amount个1元硬币，即amount + 1不可能为最小值
        dp[0] = 0 # <----已知base case。没有amount则不需要硬币

        for a in range(1, amount + 1): # <----- 非常重要，需要从最小amount 1开始bottom up算而不是top down，此刻amount = 1
            for c in coins: # <--- 此刻c为面值1
                if a >= c: # <--- 1 >= 1
                    dp[a] = min(dp[a], 1 + dp[a - c]) # <--- dp[1] = min(cur dp[1], 1 + dp[0]) = 1。同理当c = 4的循环里，dp[7] = min(cur dp[7], 1 + dp[7 - 4])。看懂这行至关重要
                # else: # 为什么这个else不用写呢，因为假设amount是7，第一个coin为8，这并不代表amount 7 就没有解，万一第2个coin是2呢？那么当进入coin=2，amount=7的循环时候，dp[7]还会stay at -1而不是根据使用coin 2算出来的结果
                #     dp[a] = -1 
        
        return dp[amount] if dp[amount] != amount + 1 else -1 # <--- 如果dp[amount]没有解，dp[amount]会stay at初始值，即amount + 1

     
# 11.27 复习自己写。自己第一反应仍然是先尽量多用最大的硬币，这个思路就是错的
# 看了neet code代码以后默写一遍bottom up DP。
# T O(#_coins * amount) M O(amount)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = (amount + 1) * [amount + 1] # instantiate the dp to impossible vals
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                need = i - coin
                if i >= coin:
                    dp[i] = min(dp[i], dp[need] + 1)
        
        return dp[amount] if dp[amount] != amount + 1 else -1