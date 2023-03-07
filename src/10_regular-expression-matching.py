# 2.27 first try自己40min写的，能过278/354 cases.碰到s = "aab", p = "c*a*b" 挂了，原来p里面可以有s没有的东西
# s = "aab", p = "c*a*b"应该return True， 但s = "ab"， p = ".*c"应该return False， s = "aaa"，p = "ab*a"应该return False
# 我说真的没太搞明白为什么p里可以有s里没有的东西
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # "." --> if next is not "*", we can skip the next char b/c it can be matched
        # "." --> if next is "*" return True immediately
        # "*" --> if s[i] == s[i-1], we can move i till s[i] != s[i-1]
        # "*" --> if s[i] != s[i-1], we can move i on p but not on s
        i, j = 0, 0
        
        while i < len(s) and j < len(p):
            if s[i] == p[j]:
                i += 1
                j += 1
            elif p[j] == "*":
                prev_c = s[i - 1]
                while i < len(s) and s[i] == prev_c:
                    i += 1
                while j < len(p) and (p[j] == "*" or p[j] == prev_c):
                    j += 1
            elif p[j] == ".":
                if j + 1 < len(p) and p[j+1] == "*":
                    i = len(s)
                    j = j + 2
                else:
                    i += 1
                    j += 1
            else:
                return False

        return i == len(s) and j == len(p)
    
# 仔细研究了下，还是自己对regex不熟，s = "aab", p = "c*a*b"为什么是True,因为这个pattern代表0-n个c + 0-n个a + 一个b
# 我没有理解“*”在regex里的真正含义
# 官方recursion解法，也会TLE，其实加上lru_cache就可以算是DP了，也就能过，而且T和下面自己写的DP差不多，M稍微差点因为cache整个array作为input了
class Solution(object):
    def isMatch(self, s: str, p: str) -> bool:      
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or # 此处即可handle s = “aab" match p = “a*b"
                    first_match and self.isMatch(s[1:], p)) #此处可带入“aa” “a*”case走一遍，最后迭代成“” “a*”，会在上面那行的情况下return True
        else:
            return first_match and self.isMatch(s[1:], p[1:])


# 官方最优解是DP
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j+1 < len(p) and p[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)
    

# 不死心修改了一下自己的解法，能过第一次挂掉的case但是碰到s ="aaa"， p = "ab*a*c*a" 还是挂了
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # i, j as pointer in s and p
        # "." --> if next is not "*", we can skip the next char b/c it can be matched
        # "." --> if next is "*" return move i till the end b/c any string can be matched
        # "*" --> if s[i - 1] == p[j - 1], we can move i till s[i] != s[i-1] and p[j] != p[j - 1]
        # "*" --> if s[i - 1] != p[j - 1], we can move j to j + 1
        i, j = 0, 0
        while i < len(s) and j < len(p):
            if s[i] == p[j]:
                i += 1
                j += 1
            elif p[j] == ".":
                if j + 1 < len(p) and p[j+1] == "*":
                    i = len(s)
                    j = j + 2
                else:
                    i += 1
                    j += 1
            elif p[j] == "*":
                prev_c = p[j-1]
                while i < len(s) and s[i] == prev_c:
                    i += 1
                while j < len(p) and (p[j] == prev_c or p[j] == "*"):
                    j += 1
            else:
                if j + 1 < len(p) and p[j+1] == "*":
                    j = j + 2
                else:
                    return False

        return i == len(s) and j == len(p)
    
# 自己默写了一遍DP
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        def idxMatch(i, j):
            if (i, j) not in dp:
                if i == len(s) and j == len(p):
                    res = True
                else:
                    firstMatch = i < len(s) and j < len(p) and p[j] in {s[i], "."}
                    if j + 1 < len(p) and p[j+1] == "*":
                        res = idxMatch(i, j+2) or firstMatch and idxMatch(i+1, j)
                    else:
                        res = firstMatch and idxMatch(i+1, j+1)
                dp[(i, j)] = res
            return dp[(i, j)]

        return idxMatch(0, 0)