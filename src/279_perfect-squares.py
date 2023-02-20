from math import sqrt, floor
# 2.19 first try。自己20 min想的思路
# 很明显我们只用考虑小于 square root n的整数作为perfect square nums
# 比如 n=12。log2(12) = 3.58。所以我们只用考虑 1，2，3的square即 1，4，9看看它们怎样以最少的组合sum up to 12
# [9, 4, 1]降序考虑。选了9以后第二位可以选9，4，1。再选一个9>12不行，再选一个4>12不行。那么只能选1。[9, 1]之后第三位只能选1。[9,1,1],然后又只能选1[9,1,1,1] = 12。break，记minCount为4。
# 因为12/4 = 3 < mincount 4，所以接下来可以不考虑9，第一位选4,选了4以后第二位可选4，1，再选4，【4，4】第三位可选【4，1】.[4,4,4]=12,break记min count为3
# 因为12/1 = 12 > minCount 3。所以不需要考虑只选1的情况

# 自己的思路前半部分差不多（但是错得离谱不是log2,是square root)，后半部分没有想清楚的，正确答案是用DP
# 比如n=12，DP arr就是 1-12. dp[1] = 1, dp[n] = min(dp[n-k] + 1), k是<=n的perfectSquare数字
# ex: dp[2] = dp[1-1] + 1,因为小于2的perfectSquare只有1，dp[3] = min(dp[3-1]+1) = 3, dp[4] = min(dp[4-4] + 1, dp[4-1] + 1)，因为1和4两个perfect square都小于4以此类推
# DP(n)
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        k = floor(sqrt(n))
        perfectSqrs = [k ** 2 for k in range(1, k+1)]
        for i in range(2, n+1):
            min_dp = i
            for perfect in perfectSqrs:
                if perfect > i:
                    break
                min_dp = min(min_dp, dp[i - perfect] + 1)
            dp[i] = min_dp
        return dp[n]
