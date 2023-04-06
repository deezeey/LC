from typing import List

# 不知为啥 10.07第一遍做没有记录也没有submit到leet code
# 11.27复习自己还是不知道怎么弄这个DP，看了neetcode视频又重新默了一遍
# T O(len(s) * len(wordDict)) M O(len(s))
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if len(word) <= len(s) - i:
                    if s[i : i + len(word)] == word and dp[i + len(word)]:
                        dp[i] = True
        
        return dp[0]


# neet code写法
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break # 这里break out of for loop非常节省时间，因为只要有一个词令dp[i]为True我们就不需要再check wordlist里的其他词

        return dp[0]
