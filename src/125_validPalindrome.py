#用python自带function有点cheat的意思在
def isPalindrome(s: str) -> bool:
    newstr = "" #used extra memory to store the newstr"
    for c in s:
        if c.isalnum():
            newstr += c.lower()
    return newstr == newstr[::-1]

#解法2，two pointers
def isPalindrome(s: str) -> bool:
    l, r = 0, len(s)-1
    while l < r:
        while not isAlphaNum(s[l]) and l < r:
            l += 1
        while not isAlphaNum(s[r]) and l < r:
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
    
    
def isAlphaNum(c:str) -> bool:
    return (
        ord("a") <= ord(c) <= ord("z")
        or ord("0") <= ord(c) <= ord("9")
        or ord("A") <= ord(c) <= ord("Z")
    )


# 9.25 复习自己写， 一开始漏掉了.lower()总也通不过
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l <= r:
            a, b = s[l], s[r]
            if not self.isAlphaNum(a): # <---自己总是习惯写if continue，看答案其实写while更好
                l += 1
                continue
            if not self.isAlphaNum(b):
                r -= 1
                continue
            if a.lower() == b.lower():
                l += 1
                r -= 1
            else:
                return False
        return True
                
    def isAlphaNum(self, c: str) -> bool:
        return (
            ord('a') <= ord(c) <= ord('z')
            or ord('A') <= ord(c) <= ord('Z')
            or ord('0') <= ord(c) <= ord('9')
        )


# 11.03复习自己写 T O(n) M O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        b, e = 0, len(s) - 1
        def isAlphaNum(c):
            return ((ord(c) >= ord("0") and ord(c) <= ord("9")) or
            (ord(c) >= ord("a") and ord(c) <= ord("z")) or
            (ord(c) >= ord("A") and ord(c) <= ord("Z")))

        while b <= e:
            if not isAlphaNum(s[b]):
                b += 1
                continue
            if not isAlphaNum(s[e]):
                e -= 1
                continue
            else:
                if s[b].lower() != s[e].lower():
                    return False
            b += 1
            e -= 1

        return True