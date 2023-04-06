from typing import List
from collections import Counter

# 10. 13 first try 一开始以为很简单但是这样写过不了s = "ababababab" p = "aab"的case
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        len_p = len(p)
        res = []

        for i in range(len(s) - len_p + 1):
            if set(s[i:i+len_p]) == set(p):
                res.append(i)

        return res


# 10. 14自己用sliding window + hashmap写的
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        l, r = 0, len(p) - 1
        hash_p = {c : p.count(c) for c in set(p)}
        hash_s = {}
        res = []

        while r < len(s):
            if not hash_s:
                hash_s = {c : s[l:r+1].count(c) for c in set(s[l:r+1])}
            else:
                hash_s[s[l-1]] -= 1
                if hash_s[s[l-1]] == 0:
                    del hash_s[s[l-1]]
                if s[r] in hash_s:
                    hash_s[s[r]] += 1
                else:
                    hash_s[s[r]] = 1
                    
            if hash_s == hash_p:
                res.append(l)

            l += 1
            r += 1

        return res


# 这个是我目前看到最简洁的，直接比较python存的hash value之和
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        LS, LP, S, P, A = len(s), len(p), 0, 0, []
        if LP > LS: return []
        for i in range(LP): S, P = S + hash(s[i]), P + hash(p[i])
        if S == P: A.append(0)
        for i in range(LP, LS):
            S += hash(s[i]) - hash(s[i-LP])
            if S == P: A.append(i-LP+1)
        return A


# 11.03 复习自己写。怎么又写不出来了。。。这个能pass "abc" in "cbaebabacd", 但 pass不了"ab" in "abab"
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        P_HASH = Counter(p)
        s_hash = {}
        l, r = 0, 0
        res = []
        while r < len(s):
            if s_hash == P_HASH:
                res.append(l)
                if s_hash[s[l]] > 1:
                    s_hash[s[l]] -= 1
                else:
                    del s_hash[s[l]]
                l += 1
            elif s[r] in p:
                if s[r] not in s_hash:
                    s_hash[s[r]] = 1
                elif s[r] in s_hash and s_hash[s[r]] < P_HASH[s[r]]:
                    s_hash[s[r]] += 1
                else:
                    s_hash = {s[r]:1}
                    l = r
            else:
                s_hash = {}
                l = r + 1
            r += 1
        
        return res

# 看了答案默了一遍，用Counter比dict comprehension慢，但胜在方便易读懂 T O(n)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l, r = 0, len(p) - 1
        P_HASH = Counter(p)
        s_hash = {}
        res = []

        while r < len(s):
            if not s_hash:
                s_hash = Counter(s[l:r+1])
            else:
                # move the window
                s_hash[s[l-1]] -= 1
                if s_hash[s[l-1]] == 0:
                    del s_hash[s[l-1]]
                if s[r] in s_hash:
                    s_hash[s[r]] += 1
                else:
                    s_hash[s[r]] = 1

            if s_hash == P_HASH:
                res.append(l)
            
            l += 1
            r += 1
        
        return res

# 12.14 复习自己写，刚刚写完567，代码几乎一样
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        LEN = len(p)
        need = Counter(p)
        missing = LEN
        l = 0

        for i, c in enumerate(s):
            if c in need:
                need[c] -= 1
                if need[c] >= 0:
                    missing -= 1
            if i >= LEN:
                l += 1
                if s[i-LEN] in need:
                    need[s[i-LEN]] += 1
                if need[s[i-LEN]] > 0:
                    missing += 1
            if not missing:
                res.append(l)

        return res