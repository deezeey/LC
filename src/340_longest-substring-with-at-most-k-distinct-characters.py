from collections import defaultdict

# 2.22 first try 30min以内写出来的sliding window
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not k or not s:
            return 0

        n = len(s)
        if k >= n:
            return n
        
        # a window with min length k
        l, r = 0, k
        c_hash = defaultdict(int)

        for i in range(r):
            c_hash[s[i]] += 1
        key_count = len(c_hash.keys()) # key_count needs to be <= k
        cur_length = sum(c_hash.values())
        max_length = cur_length

        while r < n:
            if s[r] not in c_hash:
                key_count += 1
                while key_count > k:
                  prev_key = s[l]
                  c_hash[prev_key] -= 1
                  cur_length -= 1
                  if c_hash[prev_key] == 0:
                      del c_hash[prev_key]
                      key_count -= 1
                  l += 1
            c_hash[s[r]] += 1
            cur_length += 1
            max_length = max(max_length, cur_length)
            r += 1

        return max_length