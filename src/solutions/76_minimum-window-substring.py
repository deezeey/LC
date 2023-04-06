from collections import Counter

# 10.18 first try自己写的版本能跑过2个case。。。但是没看清题目要我return min length substring
# s = "ADOBECODEBANC"， t = "ABC"的时候我这个解 return的是"ADOBEC"，但正确答案是 "BANC"
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        # initialize l r as 0, len(t)
        # move r towards the end, meanwhile recording the found letters in window in 
        # if repetitive letter found, record its position as potential_l
        # if repetitive repetitve = found, move l to potential_l

        l, i, r = 0, 0, len(t) - 1
        target = Counter(t)
        found = dict()
        repeated = dict()

        while r < len(s):
            while i <= r:
                if s[i] in target:
                    if not found:
                        l = i
                        found[s[i]] = 1
                    elif s[i] not in found:
                        found[s[i]] = 1
                    else:
                        found[s[i]] += 1
                        if found == repeated and found[s[i]] == target[s[i]]:
                            l = i
                        elif s[i] in repeated:
                            repeated[s[i]] += 1
                        else:
                            repeated[s[i]] = 1
                if found == target:
                    return s[l:i+1]
                i += 1
            r += 1

        return ""


# 不信邪自己改进了一下，这会儿能pass266个里面166个case但是碰到"ab" in "bdab"我的output是"bda"正确答案是"ab"
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        # initialize l r as 0, len(t)
        # move r towards the end, meanwhile recording the found letters in window in 
        # if repetitive letter found, record its position as potential_l
        # if repetitive repetitve = found, move l to potential_l

        l, i, r, potential_l = 0, 0, len(t) - 1, 0
        target = Counter(t)
        found = dict()
        repeated = dict()
        res = ""

        while r < len(s):
            while i <= r:
                if s[i] in target:
                    if not found:
                        l = i
                        found[s[i]] = 1
                    elif s[i] not in found:
                        found[s[i]] = 1
                    elif found[s[i]] < target[s[i]]:
                        found[s[i]] += 1
                    else:
                        if not repeated:
                            potential_l = i
                        if s[i] not in repeated:
                            repeated[s[i]] = 1
                        elif s[potential_l] == s[i]:
                            potential_l = i
                        else:
                            repeated[s[i]] += 1
    
                    if found == repeated:
                        l = potential_l
                        repeated = dict()

                if found == target:
                    if not res:
                        res = s[l:i+1]
                    elif len(s[l:i+1]) < len(res):
                        res = s[l:i+1]
                i += 1
            r += 1

        return res


# 清晰简单版本逻辑的sliding window
# The current window is s[i:j] and the result window is s[I:J]. 
# In need[c] I store how many times I need character c (can be negative) and missing tells how many characters are still missing. 
# In the loop, first add the new character to the window. 
# Then, if nothing is missing, remove as much as possible from the window start and then update the result.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        need = Counter(t)
        missing = len(t)
        window_l = window_r = res_l = res_r = 0

        for i, char in enumerate(s, 1): # 因为i从1开始所以return时候我们不用+1，而且这样它可以handle single letter s and t的case，enumerate的结果会是(1, s[0])
            if need[char] > 0 and missing > 0: # missing最小就是0，到0以后不会往下减
                    missing -= 1
            need[char] -= 1 # 即使 char not in need, need[char]也不会throw key error，会return 0
            if not missing: #当window里含有全部所需letter甚至含有超出所需数量的letter时，开始看左边能扔掉多少
                window_r = i
                while window_l < window_r and need[s[window_l]] < 0: #如果此letter的need是负数，我们可以移动左指针
                    need[s[window_l]] += 1
                    window_l += 1
                if not res_r or window_r - window_l < res_r - res_l: #如果是初次设置res或者新的res比旧的res短，update res
                    res_l, res_r = window_l, window_r
            
        return s[res_l: res_r]


# 11.04 复习自己想到了comment里面写的那种思路但不清晰，看了答案默写也花了45min，string处理实在太容易细节出错了。
# n = len(s) + len(t)， T O(n) M O(n), counter最后里面的keys会是t和s里所有的unique字母
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        # ADOBECODEBANC ABC
        # ADOBEC
        # ADOBECODEBA --> CODEBA
        # CODEBANC --> BANC
        l, r = 0, 0
        res = ""
        need = Counter(t)
        missing = len(t)

        while r < len(s):
            if need[s[r]] > 0 and missing:
                missing -= 1
            need[s[r]] -= 1
            if not missing:
                if not res:
                    res = s[l:r+1]
                while l < r and need[s[l]] < 0:
                    need[s[l]] += 1
                    l += 1
                res = s[l:r+1] if len(s[l:r+1]) < len(res) else res
            r += 1
        
        return res

# 12.14 复习自己写出来了但是也是修改再三
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        LEN = len(t)
        missing = LEN
        l, r = 0, 0
        res = s

        for i, c in enumerate(s):
            need[c] -= 1
            if c in t:
                r = i #一开始直接用的i没有initiate r
                if need[c] >= 0:
                    missing -= 1
            if not missing:
                while need[s[l]] < 0:
                    need[s[l]] += 1
                    l += 1
                if len(s[l:r+1]) < len(res): #这个部分一开始是漏掉的
                    res = s[l:r+1] 
                    
        return res if not missing else ""