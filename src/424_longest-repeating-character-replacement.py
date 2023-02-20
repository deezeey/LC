from collections import defaultdict

# 12.14 first try，能过test case但是碰到"ABBB", k=2跪了
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # longest continuous substring with k or less exceptions in between
        if len(s) == 1:
            return 1

        res = 0

        def search(k, l, r):
            nonlocal res
            cur = 1
            while k >= 0 and r < len(s):
                if s[r] != s[l]:
                    k -= 1
                if k < 0:
                    break
                cur += 1
                r += 1
            res = max(res, cur)
        
        for i in range(len(s)):
            search(k, i, i + 1)
        
        return res

# neetcode解法
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res

# 自己按neetcode解法写了一下，while loop碰到"AABABBA" k=1 return 6 instead of 4, 过不了
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_f = 0 # max freq
        l, r = 0, 0
        res = 0

        while l <= r and r < len(s):
            window_len = r - l + 1
            count[s[r]] += 1
            max_f = max(max_f, count[s[r]])
            if window_len - max_f > k:
                count[s[l]] -= 1  #没太想明白l move了为什么不影响count和max_f
                l += 1
            else: #不需要这个else因为如果k不符合条件了我们要做的是l + 1，但是r也得 + 1
                r += 1
            res = max(res, window_len)  # 这里用window_len还是在l/r改变前compute的，所以不对
        
        return res

# 修改一下这回行了
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_f = 0 # max freq
        l, r = 0, 0
        res = 0

        while l <= r and r < len(s):
            count[s[r]] += 1
            max_f = max(max_f, count[s[r]])
            if r - l + 1 - max_f > k:
                count[s[l]] -= 1
                l += 1
            r += 1
            res = max(res, r - l)
        
        return res

# 1.5 复习，一开始自己不记得算法了，看了一眼note的提示自己写出来了
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        count = defaultdict(int)
        max_count = 0
        max_window = 0

        while r < len(s):
            window = r - l + 1
            c = s[r]
            count[c] += 1
            if count[c] > max_count:
                max_count = count[c]
            if window - max_count > k:
                count[s[l]] -= 1 #一开始忘了这行，很不好
                l += 1
            else:
                max_window = max(window, max_window)
            r += 1
        
        return max_window

# 1.9 复习自己写，对于如何increase l，要一次increase多位还是1位有点迷糊，以为过不了结果居然过了
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        hash = defaultdict(int)
        max_freq = 0
        res = 0

        while r < len(s):
            window = r - l + 1
            hash[s[r]] += 1
            max_freq = max(max_freq, hash[s[r]])
            if window - max_freq <= k:
                res = max(res, window)
            else:
                hash[s[l]] -= 1
                l += 1 #感觉这里不用在while loop里一直挪动l的原因是，没有必要check更短的window
            r += 1
        
        return res