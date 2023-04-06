from typing import List
# 1.26 firt try, 自己想了8分钟，思路大概是先把所有字母隔开，
# 然后从前往后抽掉隔板，如果这个隔板抽掉仍然满足palindrome条件，那么这个branch继续
# 但是关于如何去重这个问题还没想明白，时间限制直接看答案了
# 但是neetcode思路好像不是这样

# partition1，可能是从第一个字母到整个字符串
# 然后dfs剩下的字符串部分，iterate thru所有可能的partition，找第二个partition，看它是不是palindrome
# 第二个也找到的话就继续往下，否则branch到底
class Solution:
    def isPali(self, s, l, r):
        while l < r:
        # l = r时是single letter，直接return True
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part[::])
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res

