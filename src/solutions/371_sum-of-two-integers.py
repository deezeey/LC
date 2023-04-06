import math
# 2.2 first try
# 记住，减反是加一，反减是减一
# 这好像不行因为还是用了减号
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b:
            a = -~a
            b = ~-b
        return a

# 谁说这个不行一定要我用bit manipulation我就吐他脸上
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return int(math.log2((2**a)*(2**b)))