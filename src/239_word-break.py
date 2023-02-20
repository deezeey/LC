from typing import List

# 10.07 first try，自己没什么思路，看了neet code的DP解说
# 简直惊为天人的聪明。。。才10行代码。。。
# 这题感觉和322 coin change很像可以一起食用效果更佳

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i: i+len(word)] == word:
                    dp[i] = dp[i + len(word)]
                    if dp[i]:
                        break
        return dp[0]
