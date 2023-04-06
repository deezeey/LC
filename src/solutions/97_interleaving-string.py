# 1.30 first try规定时间30min内没写出来但是自己是有思路的，而且自己在写这个recursion的时候想到了画matrix，col和row分别是两个string的情况
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # strs can be split in any ways, but all chars need to be used and order can't be changed
        if len(s3) != len(s1) + len(s2):
            return False
        # f(c, ca, cac) = f(c, "", c) and f(c, a, ac) <---- T and T
        # f(c, a, ca) = f(c, "", c) + f("", a, a) <--- returns T
        # f("", a, a) = T, f(c, "", c) = T <--- base case
        dp = {}
        # i1, i1, i3 are idx of s1, s2, s3
        def dfs(i1, i2, i3):
            if (i1, i2, i3) in dp:
                return dp[(i1, i2, i3)]
            if (i1 == len(s1) and s2[i2] == s3[i3]) or (i2 == len(s2) and s1[i1] == s3[i3]):
                dp[i1, i2, i3] = True
                return True
    
# neetcode的 recursion memoization 写法
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # strs can be split in any ways, but all chars need to be used and order can't be changed
        if len(s3) != len(s1) + len(s2):
            return False
        # f(c, ca, cac) = f(c, "", c) and f(c, a, ac) <---- T and T
        # f(c, a, ca) = f(c, "", c) + f("", a, a) <--- returns T
        # f("", a, a) = T, f(c, "", c) = T <--- base case
        dp = {}
        # i1, i1, i3 are idx of s1, s2, s3
        def dfs(i1, i2):
            if (i1, i2) in dp:
                return dp[(i1, i2)]
            if i1 >= len(s1) and i2 >= len(s2):
                return True # 注意全程甚至不需要存True结果在dp里，因为如果后面的recursion return True了这个位置evaluate了当前字母相同以后可以直接return True，不再需要cache的结果来做任何运算的
            if i1 < len(s1) and s1[i1] == s3[i1 + i2] and dfs(i1 + 1, i2):
                return True
            if i2 < len(s2) and s2[i2] == s3[i1 + i2] and dfs(i1, i2 + 1):
                return True
            dp[(i1, i2)] = False
            return False

        return dfs(0, 0)

# 2d DP的写法 我觉得有点难理解
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    print("check i:", i, j, s3[i + j], dp[i+1][j])
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    print("check j:", i, j, s3[i + j], dp[i][j+1])
                    dp[i][j] = True
        return dp[0][0]
# s1 = "aabcc"  s2 = "dbbca"  s3 = aadbbcbcac"
# check i: 4 5 c True
# check j: 4 4 a True
# check j: 4 3 c True
# check j: 4 2 b True
# check i: 3 4 c True
# check i: 3 2 c True
# check j: 3 1 b True
# check i: 2 4 b True
# check j: 2 3 c True
# check i: 2 2 b True
# check j: 2 2 b True
# check i: 2 1 b True
# check j: 2 1 b True
# check j: 2 0 d True
# check i: 1 0 a True
# check i: 0 0 a True