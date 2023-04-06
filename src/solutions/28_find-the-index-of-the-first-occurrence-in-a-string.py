# 2.8 first try 过不了 "mississippi" and "issip"的case
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, j = 0, 0
        res = -1
        while j < len(needle) and i < len(haystack):
            if haystack[i] == needle[j]:
                if res == -1:
                    res = i
                j += 1
            else:
                res = -1
                j = 0
            i += 1
        return res if j == len(needle) else -1

# 从后往前写的话，又过不了"sadbutsad" 和 "sad"的case
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, j = len(haystack) - 1, len(needle) - 1
        res = -1
        while i >= 0 and j >= 0:
            print(i, j, haystack[i], needle[j])
            if haystack[i] == needle[j]:
                res = i
                j -= 1
                i -= 1
            else:
                if res != -1:
                    res = -1
                    j = len(needle) - 1
                else:
                    i -= 1
        return res if j == -1 else -1

# brute force way是sliding window
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(needle), len(haystack)
        for l in range(n - m + 1):
            r = l
            while r - l < m:
                if haystack[r] != needle[r - l]:
                    break
                r += 1
            if r - l == m:
                return l
        return -1

# 标答sliding window
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)

        for window_start in range(n - m + 1):
            for i in range(m): # 这里用for loop更好理解
                if needle[i] != haystack[window_start + i]:
                    break
                if i == m - 1:
                    return window_start

        return -1

# 正解是KMP algo, 他能保证worse case scenario T O(M + N) 但是真的过于复杂，以后再revisit吧
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        lps = [0] * len(needle)

        prevLPS, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]

        i = 0  # ptr for haystack
        j = 0  # ptr for needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            if j == len(needle):
                return i - len(needle)
        return -1

# Rabin Karp algo - double hash
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)

        if n < m:
            return -1

        # CONSTANTS
        RADIX_1 = 26
        MOD_1 = 10**9+33
        MAX_WEIGHT_1 = 1
        RADIX_2 = 27
        MOD_2 = 2**31-1
        MAX_WEIGHT_2 = 1

        for _ in range(m):
            MAX_WEIGHT_1 = (MAX_WEIGHT_1 * RADIX_1) % MOD_1
            MAX_WEIGHT_2 = (MAX_WEIGHT_2 * RADIX_2) % MOD_2

        # Function to compute hash_pair of m-String
        def hash_pair(string):
            hash_1 = hash_2 = 0
            factor_1 = factor_2 = 1
            for i in range(m - 1, -1, -1):
                hash_1 += ((ord(string[i]) - 97) * (factor_1)) % MOD_1
                factor_1 = (factor_1 * RADIX_1) % MOD_1
                hash_2 += ((ord(string[i]) - 97) * (factor_2)) % MOD_2
                factor_2 = (factor_2 * RADIX_2) % MOD_2

            return [hash_1 % MOD_1, hash_2 % MOD_2]

        # Compute hash pairs of needle
        hash_needle = hash_pair(needle)

        # Check for each m-substring of haystack, starting at window_start
        for window_start in range(n - m + 1):
            if window_start == 0:
                # Compute hash pairs of the First Substring
                hash_hay = hash_pair(haystack)
            else:
                # Update Hash pairs using Previous using O(1) Value
                hash_hay[0] = (((hash_hay[0] * RADIX_1) % MOD_1
                               - ((ord(haystack[window_start - 1]) - 97)
                                  * (MAX_WEIGHT_1)) % MOD_1
                               + (ord(haystack[window_start + m - 1]) - 97))
                               % MOD_1)
                hash_hay[1] = (((hash_hay[1] * RADIX_2) % MOD_2
                               - ((ord(haystack[window_start - 1]) - 97)
                                  * (MAX_WEIGHT_2)) % MOD_2
                               + (ord(haystack[window_start + m - 1]) - 97))
                               % MOD_2)

            # If the hash matches, return immediately.
            # Probability of Spurious Hit tends to zero
            if hash_needle == hash_hay:
                return window_start
        return -1