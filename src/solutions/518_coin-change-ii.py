from typing import List

# 1.30 first try自己的思路是正确的（如下comment），但是因为疑虑这题怎么是2D DP所以没有写出来
# T O(len(coins) * amount), M is the same
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # get rid of coins > amount and sort coins in descending order
        # Res([2,5]) = Res(must include 2) + Res([5])
        # Res([1, 2, 5]) = Res(must include 1) + Res([2, 5])
        coins = [c for c in coins if c <= amount]
        dp = {}
        def dfs(i, a):
            if a == amount:
                return 1
            if a > amount:
                return 0
            if i >= len(coins):
                return 0
            if (i, a) in dp:
                return dp[(i, a)]
            dp[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return dp[(i, a)]
        
        return dfs(0, 0)

#  2D DP的解法T和上面一样，但是M被reduce到了N。详情见pic。
# 每个cell代表的意思是使用本行即本行以下面值的coins，有多少种方法可以组成column header amount
# 然后他先从最底下一行只有5面值coin的情况，从右往左算起，然后再往上算面值【2， 5】的情况。这样每次memory里只需要存一行
# 这个cell的amount - coin即需要往右走的步数，按这个步数走到的cell的值， 加上这个cell自己下面的值，就是这个cell应该存储的值
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # DYNAMIC PROGRAMMING
        # Time: O(n*m)
        # Memory: O(n) where n = amount
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP
        return dp[amount]

        # 如下存整个grid也可以，只是这样M没有提升
        # DYNAMIC PROGRAMMING
        # Time: O(n*m)
        # Memory: O(n*m)
        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)
        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
                dp[a][i] = dp[a][i + 1]
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]
        return dp[amount][0]
