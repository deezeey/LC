# 10.10 first try, 看了neet code自己写的解

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0

        for i in range(len(s)):
            l, r = i, i
            #odd
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1
                l -= 1
                r += 1

            #even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1
                l -= 1
                r += 1

        return res
        

# 11.05 复习自己改进了一下代码 
# 枚举中心点l,r,即for loop,是O(n). checkPalindrome function worst case 也是 O(n), 所以双指针 T O(n^2)。因为只存了一个常量 max_str所以 S O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = ""

        def checkPalindrome(l, r):
            nonlocal max_str
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    max_str = s[l:r+1] if len(s[l:r+1]) > len(max_str) else max_str
                else:
                    break
                l -= 1
                r += 1

        for i in range(len(s)):
            checkPalindrome(i, i)
            if len(s) > 1:
                checkPalindrome(i, i + 1)

        return max_str

# 马拉车算法可以在 T O(n)内解决这个问题
# https://www.felix021.com/blog/read.php?2040

# 12.13 复习，自己能pass128 out of 144.碰到 s="aaaa" 跪了，return了"aaa"
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        res = ""
        for i in range(1, len(s)):
            if i < len(s) - 1 and s[i - 1] == s[i + 1]:
                # odd
                l, r = i - 1, i + 1
            elif s[i] == s[i - 1]:
                # even
                l, r = i - 1, i
            else:
                if not res:
                    res = s[i]
                continue
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > len(res):
                res = s[l + 1: r]
        
        return res

# 重新默写一遍helper function版本
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        res = ""

        def checkPalindrome(l, r):
            nonlocal res
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            if r - l - 1 > len(res):
                res = s[l + 1 : r]
        
        for i in range(len(s)):
            checkPalindrome(i, i)
            if len(s) > 1:
                checkPalindrome(i, i + 1)
        
        return res

# 12.15 复习写出来了
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        res = ""
        def getPalindrome(l, r):
            nonlocal res
            while l >= 1 and r <= len(s) - 2 and s[l-1] == s[r+1]:
                l -= 1
                r += 1
            if r - l + 1 > len(res):
                res = s[l:r+1]
        
        for i in range(len(s)):
            getPalindrome(i, i)
            if i < len(s) - 1 and s[i] == s[i+1]:
                getPalindrome(i, i+1)
        
        return res