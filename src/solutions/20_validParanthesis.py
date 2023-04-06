# 自己的第一次尝试，wrong answerL: True for "([)]"
def isValid(self, s: str) -> bool:
    ls = [*s]
    pairs = {')': '(', ']': '[', '}': '{'}
    count = {'(': 0, '[': 0, '{': 0}
    for s in ls:
        if s in count:
            count[s] += 1
        else:
            opener = pairs[s]
            count[opener] -= 1
    return not any(count.values()) 


# neet code 正解，用stack
def isValid(self, s: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for p in s:
        if p not in pairs: #如果p不是pairs的keys之一，代表他是open bracket，append到stack上
            stack.append(p)
            continue
        if not stack or pairs[p] != stack[-1]: #如果是close bracket，stack为空，代表close bracket在第一位，return false，如果stack最上层，即最后一个open bracket不能被p抵消，也return false
            return False
        # 以上情况都不是，代表最后一位open bracket可被p抵消
        stack.pop()
        
    #最后我们希望结果stack为空
    return not stack


# 9.25 复习自己写
def isValid(s: str) -> bool:
    mapper = {')': '(', ']': '[', '}': '{'}
    stack = []
    for c in s:
        if c not in mapper:
            stack.append(c)
        elif stack and mapper[c] == stack[-1]:
            stack.pop()
        else:
            return False
    return not stack


# 11.02 复习自己写 T O(n) M O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in [")", "]", "}"]:
                last_open_parenthsis = stack.pop() if stack else ""
                if last_open_parenthsis != mapper[c]:
                    return False
                else:
                    continue
            if c in ["(", "[", "{"]:
                stack.append(c)
        
        return not stack