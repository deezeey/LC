# 10.09 first try 看着挺简单其实写的时候小地方容易出错
# 比如不valid string应该return 0 而不是none

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        range_begin, range_end = ord("0"), ord("9")
        number = ""
        evaluated_number = 2 ** 31 - 1

        for i in range(len(s)):
            if i == 0 and s[i] in ["+", "-"]:
                evaluated_number = 2 ** 31 - 1 if s[i] == "+" else -(2 ** 31)
            elif ord(s[i]) >= range_begin and ord(s[i]) <= range_end:
                number += (s[i])
            else:
                break
        
        if not number:
            return 0

        if evaluated_number > 0 and int(number) <= evaluated_number:
            evaluated_number = int(number)
        if evaluated_number < 0 and -int(number) >= evaluated_number:
            evaluated_number = -int(number)
        
        return evaluated_number


# 11.01 复习自己写，弄了半天，感觉写的还没第一次好了呢 T O(n) M O(n)
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = None
        number = ""
        
        def isInt(c):
            return ord(c) >= ord("0") and ord(c) <= ord("9") 

        for c in s:
            if not sign:
                if isInt(c):
                    number += c
                    sign = 1
                elif c == "+":
                    sign = 1
                elif c == "-":
                    sign = -1
                else:
                    break
            else:
                if isInt(c):
                    number += c
                else:
                    break

        if not number:
            return 0
        
        return min(int(number), 2**31 - 1) if sign > 0 else max(-int(number), -2**31)


# 看到一个评论说不可以在 last step compare final answer的，很有意思，但是10年前大部分操作系统和processor就已经是64bit的了
# in real interview, even you use python, you need to assume current system only support 32 bit. 
# So instead of compare the final answer in the last step, you need to manualy trim the result at adding digit step

# 12.08 复习
class Solution:
    def myAtoi(self, s: str) -> int:
        num = ""
        sign = 1

        s = s.strip()  # strip不是mutate method需要重新赋值！
        
        for i in range(len(s)):
            c = s[i]
            if i == 0 and c in ("+", "-"):
                if c == "-":
                    sign = -1
                continue
            if not c.isdigit():
                break
            else:
                num += c
        
        if num:
            res = min(2 ** 31 - 1, int(num)) if sign > 0 else max(-1 * (2 ** 31), -1 * int(num))

        return res if num else 0