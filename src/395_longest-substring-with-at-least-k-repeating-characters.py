from collections import Counter, defaultdict
# 2.24 first try 自己写了一半就知道这个sliding window不move左边pointer是不行的，30min以内没有想出来如何move左边pointer
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        if n < k:
            return 0
        # sliding window
        need, max_len = 0, 0
        seen = set()
        for i in range(n):
            if s[i] in set():
                need = max(0, need - 1)
            else:
                need += k - 1
            if not need:
                max_len = max(0, max_len + 1)
        return max_len
    
# 这题卡了好几个小时，看答案主要是recursive和sliding window两种解法
# recursion比较简单。从头开始碰到总freq < k的字母，就以它为中点split两半，分别recurse on 这两半，取max
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if s == [] or k > len(s):
            return 0
        freq = Counter(s)
        for i, char in enumerate(s):
            if freq[char] < k:
                return max(self.longestSubstring(s[:i], k),  self.longestSubstring(s[i+1:], k))
        return len(s)
    
# 很不intuitive的slinding window：
# 假设总共有n个distinct chars. 然后令 T 为substring总共可以有的distinct char数量，这个数字一定是在 <1 ~ n> 之间。
# for T = < 1 ~ n >, 做sliding window。
# sliding window的func body有freq_hash，uniq_count, k_plus_freq_count三个变量。
# 分别是目前window的char：freq，当前window总共的uniq char数量，当前window满足freq >= k条件的uniq char数量。
# window不断往右边扩充, update freq_hash（不断-1），uniq_count（如果是新字母）, k_plus_freq_count(如果有字母的freq首次>=k）。
# 如果uniq_count结果>T了（ex：要2个uniq char，但window里有3个了），window左边pointer前进，再次update freq_hash(不断-1), k_plus_freq_count（如果有字母的freq跌破了k)，uniq_count（如果有字母的freq跌到了0），一直移动左边直到uniq_count变回T。
# 然后此时如果k_plus_freq_count == uniq_count == T，则可以记录result(r - l + 1)

# 相当于做了 n pass sliding window
# 自己重新实现一遍sliding window
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s or k > len(s):
            return 0
        # get n = number of distinct chars in s
        n = len(Counter(s))
        res = 0
        # for T in <1~n>, run sliding window
        for T in range(1, n + 1):
            # l, r defines the window
            l, r = 0, 0
            # given cur window: freq_hash: char:freq, uniq_count: uniq chars, above_k_count: uniq chars with freq >= k
            freq_hash = defaultdict(int)
            uniq_cnt, above_k_cnt = 0, 0
            # move right pointer and update 3 vars above
            while r < len(s):
                r_char = s[r]
                if not r_char in freq_hash:
                    uniq_cnt += 1
                freq_hash[r_char] += 1
                if freq_hash[r_char] == k:
                    above_k_cnt += 1
                # if uniq_count > T, move left pointer until uniq_count == T
                while uniq_cnt > T:
                    l_char = s[l]
                    freq_hash[l_char] -= 1
                    if freq_hash[l_char] == k - 1:
                        above_k_cnt -= 1
                    if freq_hash[l_char] == 0:
                        del freq_hash[l_char]
                        uniq_cnt -= 1
                    l += 1
                # if uniq_count == above_k_count == T: update res
                if uniq_cnt == above_k_cnt == T:
                    res = max(res, r - l + 1)
                r += 1
        return res