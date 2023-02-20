# 2.1 first try自己想到了肯定是用 >> 和 << 但是么想出来怎么写
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1 # 比如 1001 & 1，相当于 1001 & 0001，就会取到最后一位
            res += (bit << (31 - i)) # 把最后一位顶到最前面
        return res