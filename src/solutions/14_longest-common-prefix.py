from typing import List
# 2.6 first try好像写的有点傻
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(w) for w in strs])
        res = ""
        for i in range(min_len):
            cur = strs[0][i]
            for j in range(1, len(strs)):
                str = strs[j]
                if str[i] != cur:
                    cur = ""
                    break
            if not cur:
                break
            res += cur
        return res

# 更好一点的写法，用all()
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: 
            return ""

        prefix = ""        
        for i in range(len(min(strs))):
            c = strs[0][i]
            if all(a[i] == c for a in strs):
                prefix += c
            else:
                break
        return prefix

# neetcode写法
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res