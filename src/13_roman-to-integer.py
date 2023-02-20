# 2.6 first try感觉显得有点笨
class Solution:
    def romanToInt(self, s: str) -> int:
        mapper = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        exceptions = {"IV":4, "IX":9, "XL":40, "XC":90, "CD": 400, "CM": 900}
        res = 0
        l, r = 0, 1
        if len(s) == 1:
            return mapper[s]
        while r <= len(s):
            if s[l:r+1] in exceptions:
                res += exceptions[s[l:r+1]]
                l += 2
                r += 2
            else: # 一开始漏了这个else可debug了半天
                res += mapper[s[l]]
                l += 1
                r += 1
        return res

# 同一个思路官方写的解法
values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40, 
    "XC": 90,
    "CD": 400,
    "CM": 900
}

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            # This is the subtractive case.
            if i < len(s) - 1 and s[i:i+2] in values:
                total += values[s[i:i+2]] 
                i += 2
            else:
                total += values[s[i]]
                i += 1
        return total

# 这题其实从右往左更make sense
class Solution:
    def romanToInt(self, s: str) -> int:
        mapper = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res = 0
        res += mapper[s[-1]]
        for i in range(len(s)-1)[::-1]:
            if mapper[s[i]] < mapper[s[i+1]]:
                res -= mapper[s[i]]
            else:
                res += mapper[s[i]]
        return res