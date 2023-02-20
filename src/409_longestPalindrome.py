from collections import Counter
# 9.29 first try，能pass但仍然写的不够简洁
class Solution:
    def longestPalindrome(self, s: str) -> int:
        palindromeLen = 0
        hasSingle = 0
        for c in set(s):
            if s.count(c) >= 2:
                pairs, modulo = s.count(c) // 2, s.count(c) % 2
                palindromeLen += pairs * 2
                if modulo:
                    hasSingle = 1
            else:
                hasSingle = 1
        if hasSingle:
            return palindromeLen + 1
        else:
            return palindromeLen
        

# 和我思路一样，九章的写法
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashC = {}

        for c in s:
            if c in hashC:
                del hashC[c]
            else:
                hashC[c] = 1

        odd = len(hashC)
        if odd:
            return len(s) - odd + 1
        else:
            return len(s) - odd

# 11.01 复习自己写, 觉得九章写的好点，直接delete from hash。 但是我的T能beat 88%，他们的T只能beat 5%，我估计del这个操作比较耗时。这个解法 T O(n) M O(n)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        length = 0
        can_be_odd = False

        for k, v in count.items():
            if v >= 2 and v % 2 == 0:
                length += v
            elif v >= 2 and v % 2 != 0:
                length += v - 1
                can_be_odd = True
            else:
                can_be_odd = True
        
        return length + 1 if can_be_odd else length