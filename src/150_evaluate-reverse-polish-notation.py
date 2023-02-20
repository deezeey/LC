from typing import List
import math

# 10.03 first try，自己用stack做出来了，就是第一次发现python的整除并floor但java和c++都是整除再round towards zero，所以需要处理一下
# T: O(2n) = O(n), M: O(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ("+", "-", "*", "/")
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                a = stack.pop()
                b = stack.pop()
                if tokens[i] == "/":
                    stack.append(str(math.trunc(b / float(a))))  # <--- 后来看了neet code发现只要写 int(b/a)就可以了
                else:
                    stack.append(str(eval(b + tokens[i] + a)))
        return eval(stack[0])
        

# 11.02 复习自己写，自己又忘了python //是floor division，找了半天int division用什么。 T O(n) M O(n)
# 然后没有用eval function所以长了点，不过应该没关系
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        int_stack = []

        for token in tokens:
            if token not in operators:
                int_stack.append(int(token))
            else:
                second = int_stack.pop()
                first = int_stack.pop()
                res = None
                match token:
                    case "+":
                        res = first + second
                    case "-":
                        res = first - second
                    case "/":
                        res = int(first / second)
                    case default:
                        res = first * second
                int_stack.append(res)
            
        return int_stack[0]

# 12.08 复习自己写，不用写那个inInt func的
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # when encountering an operator, pop 2 prev nums
        # calc res and push to stack
        def isInt(s):
            for i in range(len(s)):
                if i == 0 and s[i] == "-" and len(s) > 1:
                    continue
                elif not ord("0") <= ord(s[i]) <= ord("9"):
                    return False
            return True

        stack = []
        for token in tokens:
            if isInt(token):
                stack.append(int(token))
            else:
                last = stack.pop() 
                last_prev = stack.pop()
                res = 0
                match(token):
                    case "+":
                        res = last_prev + last
                    case "-":
                        res = last_prev - last
                    case "*":
                        res = last_prev * last
                    case "/":
                        res = int(last_prev / last)
                stack.append(res)
        
        return stack[0]