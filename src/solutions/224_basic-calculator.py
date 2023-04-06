# 10.22 first try 因为只有加减和括号所以比较简单，但是自己也没想出来
# 看了一眼九章的答案自己默写出来了

class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        res = 0
        sign = 1
        stack = []

        for c in s:
            if c in '0123456789':
                num = num * 10 + int(c)
            elif c == "+":
                res += sign * num
                num = 0
                sign = 1
            elif c == "-":
                res += sign * num
                num = 0
                sign = -1
            elif c == "(":
                stack.append((res, sign))
                res = 0
                sign = 1
            elif c == ")":
                res += sign * num
                prev_res, prev_sign = stack.pop()
                # print(c, res, prev_res, prev_sign)
                res = prev_res + prev_sign * res
                num = 0
                sign = 1

        res += sign * num

        return res


# 另一个评论区里的高票答案
def calculate(self, s):
    total = 0
    i, signs = 0, [1, 1]
    while i < len(s):
        c = s[i]
        if c.isdigit():
            start = i
            while i < len(s) and s[i].isdigit():
                i += 1
            total += signs.pop() * int(s[start:i])
            continue
        if c in '+-(':
            signs += signs[-1] * (1, -1)[c == '-'],
        elif c == ')':
            signs.pop()
        i += 1
    return total


# 11.03 复习自己写，又没写出来
class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        sign = 1
        num_stack = []
        operator_stack = []

        for c in s:
            if ord(c) <= ord(9) and ord(c) >= ord(0):
                num = 10 * num + int(c)
            elif c in ["+", "-"]:
                if not operator_stack:
                    num_stack.append(num)
                    operator_stack.append(c)
                else:
                    operator = operator_stack.pop()
                    match operator:
                        case "+":
                            num_stack.append(num_stack.pop() + num)
                        case "-":
                            num_stack.append(num_stack.pop() - num)
                operator_stack.append(c)
            
        # num_stack = [1]
        # operator_stack = ["+"]

# 看了答案又默写了一遍 T O(n) M O(n)
class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        res = 0
        sign = 1
        stack = []

        for c in s:
            if ord(c) >= ord("0") and ord(c) <= ord("9"):
                num = num * 10 + int(c)
            elif c == "+":
                res += sign * num
                num = 0
                sign = 1
            elif c == "-":
                res += sign * num
                num = 0
                sign = -1
            elif c == "(":
                stack.append((sign, res))
                num = 0
                res = 0
                sign = 1
            elif c == ")":
                res += sign * num
                prev_sign, prev_res = stack.pop()
                res = prev_res + prev_sign * res
                num = 0
                sign = 1
            else:
                continue
        if num:
            res += sign * num
        return res


# 12.06 复习自己花了大概1个小时写出来的，这个题主要就是太麻烦了要理清楚逻辑很难
class Solution:
    def calculate(self, s: str) -> int:
        # negative sign
        # open parenthesis --> store everything before it for future use
        # close parenthesis --> conclude the current calculation and fetch things stored before open parenthesis
        # multi digits numbers
        num, cur_sum = 0, 0
        cur_sign = 1 # representing "+" or "-"
        sum_stack = []
        sign_stack = []

        for c in s:
            if c.isdigit():
                num = (num * 10 + int(c))
            elif c == "-":
                cur_sum += cur_sign * num
                num = 0
                cur_sign = -1
            elif c == "+":
                cur_sum += cur_sign * num
                num = 0
                cur_sign = 1
            elif c == "(":
                sum_stack.append(cur_sum)
                sign_stack.append(cur_sign)
                cur_sum, num = 0, 0
                cur_sign = 1
            elif c == ")":
                cur_sum += cur_sign * num
                num = 0
                cur_sign = 1
                prev_sign = sign_stack.pop()
                prev_sum = sum_stack.pop()
                cur_sum = prev_sum + prev_sign * cur_sum
            else:
                continue
        
        return cur_sum + cur_sign * num

# 12.08 复习，这回花了大概20分钟写出来了，还是不能一次记住，这题就是逻辑理清挺麻烦
class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        sign = 1
        stack = []
        res = 0

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "+":
                res += sign * num
                sign = 1
                num = 0
            elif c == "-":
                res += sign * num
                sign = -1
                num = 0
            elif c == "(":
                stack.append((sign, res))
                res = 0
                sign = 1
                num = 0
            elif c == ")":
                res += sign * num
                prev_sign, prev_num = stack.pop()
                res = prev_num + prev_sign * res
                sign = 1
                num = 0
            else:
                continue
        
        return res + sign * num if num else res