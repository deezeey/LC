# 10.02 first try, 思路想到了但是代码没实现出来，九章的while loop很易懂
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        index_a = len(a) - 1
        index_b = len(b) - 1
        sum = ""
        carry = 0
        while index_a >= 0  or index_b >= 0:  # 这个用两个不一样的idx并且用一个 or 条件判断句很聪明
            val_a = int(a[index_a]) if index_a >= 0 else 0
            val_b = int(b[index_b]) if index_b >= 0 else 0
            if (val_a + val_b + carry) % 2 == 0:
                sum = "0" + sum
            else:
                sum = "1" + sum
            carry = (val_a + val_b + carry) // 2
            index_a -= 1
            index_b -= 1
        if carry == 1:
            sum = "1" + sum
        return sum


# 11.01 复习自己写，感觉代码长了点，可以优化成九章的写法
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        res_ls = [0] * (max_len)
        carry = False

        if len(a) < max_len:
            a = "0" * (max_len - len(a)) + a
        if len(b) < max_len:
            b = "0" * (max_len - len(b)) + b

        def binary_sum(c1, c2):
            nonlocal carry
            add_one = False
            if carry:
                add_one = True
                carry = False
            res = ""
            if c1 == c2 == "0":
                res = "0"
            elif c1 == c2 == "1":
                carry = True
                res = "0"
            else:
                res = "1"
                if add_one:
                    carry = True
            if add_one:
                res = "0" if res == "1" else "1"
            return res

        for i in reversed(range(max_len)):
            res_ls[i] = binary_sum(a[i], b[i])
        
        return "1" + "".join(res_ls) if carry else "".join(res_ls)

# 改了一下，虽然代码比九章长一点但是因为我少了一个运算所以跑起来快一点点
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        index_a, index_b = len(a) - 1, len(b) - 1
        carry = 0
        res = ""

        while index_a >= 0 or index_b >= 0:
            val_a = int(a[index_a]) if index_a >= 0 else 0
            val_b = int(b[index_b]) if index_b >= 0 else 0
            ab_sum = sum([val_a, val_b, carry])
            if ab_sum == 0:
                res = "0" + res
            elif ab_sum == 1:
                res = "1" + res
                carry = 0
            elif ab_sum == 2:
                res = "0" + res
                carry = 1
            else:
            # ab_sum == 3
                res = "1" + res
                carry = 1
            index_a -= 1
            index_b -= 1
        
        return "1" + res if carry else res

# 12.07 复习
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = "0" * (max_len - len(a)) + a
        b = "0" * (max_len - len(b)) + b
        carry = 0
        res = ""

        for i in range(max_len)[::-1]:
            ad, bd = int(a[i]), int(b[i])
            total = ad + bd + carry
            if total == 0:
                res = "0" + res
                carry = 0
            elif total == 1:
                res = "1" + res
                carry = 0
            elif total == 2:
                res = "0" + res
                carry = 1
            elif total == 3:
                res = "1" + res
                carry = 1
        
        return res if not carry else "1" + res