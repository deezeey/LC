# 2.2 first try
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        num, res = 0, 0
        sign = x / abs(x)
        x = abs(x)
        while x:
            res = 10 * res + (x % 10)
            x = x // 10
        res = int(res * sign)
        return 0 if res > 2 ** 31 or res < -(2 ** 31) - 1 else res