# 1.26 first try, 自己隐约想到了确定中间点然后往两边扩散的解法但是不确定，直接看了neetcode的代码重写了一遍
class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPali(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        res = 0
        for i in range(len(s)):
            res += countPali(i, i) # odd len pali
            res += countPali(i, i+1) # even len pali
        return res