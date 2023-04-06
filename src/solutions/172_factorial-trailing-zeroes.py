import math
# 2.9 first try自己写的以为能过但是居然 40的结果是9个trailing 0s 我output了10
# 因为碰到35时候log5(35)记了2个5，而这只能算1个5
class Solution:
    def trailingZeroes(self, n: int) -> int:
        record = {5:0, 10:0}
        for i in range(1, n+1):
            if i % 10 == 0:
                record[10] += math.floor(math.log10(i))
            elif i % 5 == 0:
                record[5] += math.floor(math.log(i, 5))
        return record[5] + record[10]

# 其实只要不断除以5就可以了。。。
def trailingZeroes(self, n: int) -> int:
    zero_count = 0
    while n > 0:
        n //= 5
        zero_count += n
    return zero_count