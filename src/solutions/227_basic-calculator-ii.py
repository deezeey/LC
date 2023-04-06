# 2.17 自己写了半个小时，写出来过不了"1-1+1"，因为用stack从后往前读会变成 “1 - 2”
class Solution:
    def helper(self, sign: str, num1: int, num2: int):
        if sign == "*":
            return num1 * num2
        if sign == "/":
            return int(num1 / num2)
        if sign == "+":
            return num1 + num2
        if sign == "-":
            return num1 - num2
            
    def calculate(self, s: str) -> int:
        # no bracket and negative nums
        num = 0
        num_stack = []
        sign_stack = []
        for i in range(len(s)):
            if s[i] in "0123456789":
                num = num * 10 + int(s[i])
            if s[i] in "+-*/":
                if sign_stack and sign_stack[-1] in "*/":
                    sign = sign_stack.pop()
                    prev_num = num_stack.pop()
                    num = self.helper(sign, prev_num, num)
                num_stack.append(num)
                sign_stack.append(s[i])
                num = 0
        if num >= 0:
            num_stack.append(num)
        while sign_stack:
            num = num_stack.pop()
            prev_num = num_stack.pop()
            sign = sign_stack.pop()
            num_stack.append(self.helper(sign, prev_num, num))

        return num_stack[0]

# 别人写的解，trick是碰到当前符号，记录并参与运算的是前一个符号，以及在最后加一个+
class Solution:
    def calculate(self, s: str) -> int:
            num, pre_op, stack = 0, '+', []
            s+='+'
            for c in s:
                if c.isdigit():
                    num = num * 10 + int(c)
                elif c == ' ':
                        pass
                else:
                    if pre_op == '+':
                        stack.append(num)
                    elif pre_op == '-':
                        stack.append(-num)
                    elif pre_op == '*':
                        operant = stack.pop()
                        stack.append((operant*num))
                    elif pre_op == '/':
                        operant = stack.pop()
                        stack.append(int(operant/num))
                    num = 0
                    pre_op = c
            return sum(stack)

# 用stack 是 T On M On 但是用variable的话是T On M O1，这个的关键是保持一个concluded last num然后同时还有一个cur_num
class Solution:           
    def calculate(self, s: str) -> int:
        cur_num, last_num, res, pre_op = 0, 0, 0, '+'
        s+='+'
        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            elif c == ' ':
                    pass
            else:
                if pre_op == '+':
                    res += last_num
                    last_num = cur_num
                elif pre_op == '-':
                    res += last_num
                    last_num = -cur_num
                elif pre_op == '*':
                    last_num *= cur_num
                elif pre_op == '/':
                    last_num = int(last_num / cur_num)
                cur_num = 0
                pre_op = c
        return res + last_num