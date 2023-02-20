def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    else:
        sHash, tHash = {}, {}
        for i in range(len(s)):
            sHash[s[i]] = sHash.get(s[i], 0) + 1
            tHash[t[i]] = tHash.get(t[i], 0) + 1
        return sHash == tHash

# 9.25 复习自己写，一样的思路但是没有答案写的简单
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    hashS, hashT = {}, {}
    for c in s:
        if c in hashS:
            hashS[c] += 1
        else:
            hashS[c] = 1
    for c in t:
        if c in hashT:
            hashT[c] += 1
        else:
            hashT[c] = 1
    return hashS == hashT


# 11.01 复习自己写，还是觉得答案那个hash.get(key, 0)写的好些, n = len(s) + len(t), T O(n), M O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def hashString(string):
            string_hash = {}
            for c in string:
                if c in string_hash:
                    string_hash[c] += 1
                else:
                    string_hash[c] = 1
            return string_hash

        s_hash, t_hash = hashString(s), hashString(t)
        return s_hash == t_hash