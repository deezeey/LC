from collections import Counter
# 2.7 first try, 自己写的太复杂了
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashS = {} # c:[]i, n] <- i is the first index of c and n is count
        for i in range(len(s)):
            c = s[i]
            if c in hashS:
                hashS[c][1] += 1 
            else:
                hashS[c] = [i, 1]
        res = []
        for idx, cnt in hashS.values():
            if cnt == 1:
                res.append(idx)
        return min(res) if res else -1

# 官方hashmap解法
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # build hash map : character and how often it appears
        count = Counter(s)
        
        # find the index
        for idx, ch in enumerate(s): # 哎我自己又忘记用enumerate
            if count[ch] == 1:
                return idx     
        return -1