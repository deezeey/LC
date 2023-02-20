# 1.30 first try自己觉得就这么简单？然后在291/305 TLE了
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1/self.positivePow(x, -n)
        return self.positivePow(x, n)

    def positivePow(self, x: float, n: int) -> float:
        res = 1
        for _ in range(n):
            res *= x
        return res

# 可以用不断对半拆实现O logn
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            return 1/self.positivePow(x, -n)
        return self.positivePow(x, n)

    def positivePow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        res = self.positivePow(x, n // 2)
        res = res * res
        return res * x if n % 2 == 1 else res