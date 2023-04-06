# 2.7 first try
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # Z = ord("Z") - ord("A") + 1
        base = 0
        res = 0
        for c in reversed(columnTitle):
            res += 26 ** base * (ord(c) - ord("A") + 1)
            base += 1
        return res

# 官方答案，感觉我自己写的好点
class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        
        # Decimal 65 in ASCII corresponds to char 'A'
        alpha_map = {chr(i + 65): i + 1 for i in range(26)}

        n = len(s)
        for i in range(n):
            cur_char = s[n - 1 - i]
            result += (alpha_map[cur_char] * (26 ** i))
        return result

# 其实从左往右更简单
class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        n = len(s)
        for i in range(n):
            result = result * 26
            result += (ord(s[i]) - ord('A') + 1)
        return result