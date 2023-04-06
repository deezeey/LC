# 1.30 first try也没太看明白啥让干啥不让干，自己随便写了个
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        mapper = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        num_int_1 = 0
        for i in range(len(num1)):
            num_int_1 = 10 * num_int_1 + mapper.index(num1[i])
        res = 0
        for i in range(len(num2)):
            res = 10 * res + self.singleDigitMultiply(num_int_1, mapper.index(num2[i]))
            
        return str(res)
    def singleDigitMultiply(self, num1: int, num2: int) -> int:
        # num1 multi digit, num2 single digit
        return num1 * num2

# neetcode解法，我怀疑我那样不可以，因为如果num1非常大的话可能会是bigint
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10

        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = map(str, res[beg:])
        return "".join(res)