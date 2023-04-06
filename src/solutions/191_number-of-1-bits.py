# 2.1 first try. 没写过，bitwise calculation得背
# n & (n-1)会消除二进制形式n里的最后一个1
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n-1)
            count += 1
        return count