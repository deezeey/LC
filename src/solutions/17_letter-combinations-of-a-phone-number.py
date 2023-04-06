from collections import deque
from typing import List

# 10.12 first try 自己暴力求组合解出来了，但是TM都不好
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letter_mapper = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        length_mapper = {k : len(v) for k, v in letter_mapper.items()}
        multiplier_mapper = [(1, 1)] * len(digits)
        res = []

        for i in range(len(digits)):
            c_multiplier = s_multiplier = 1
            if i != 0:
                for j in range(i):
                    s_multiplier *= length_mapper[digits[j]]
            if i != len(digits) - 1:
                for k in range(i + 1, len(digits)):
                    c_multiplier *= length_mapper[digits[k]]
            multiplier_mapper[i] = (c_multiplier, s_multiplier)

        for i in range(len(digits)):
            letter = digits[i]
            c_multiplier, s_multiplier = multiplier_mapper[i]
            local_res = []
            for c in list(letter_mapper[letter]):
                local_res.extend([c] * c_multiplier)
            local_res *= s_multiplier

            if not res:
                res.extend(local_res)
            else:
                res = [ s + c for s, c in zip(res, local_res)]

        return res


# neetcode写的backtracking func
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits): # <---假设digits是“23”，那么curStr是“ad” "ae" "cd" 这种就代表到了leaf，会append到res结束recursion
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c) # <--- 如果neet code如下这样，写 curStr += c 然后backtrack(i + 1, curStr) 那么他也需要pop掉最后一个字母
                # curStr += c
                # backtrack(i + 1, curStr)
                # curStr = curStr[:-1]

        if digits:
            backtrack(0, "")

        return res

#  leet code 官方的backtrack
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: 
            return []
        
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        
        def backtrack(index, path):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            for letter in letters[digits[index]]:
                path.append(letter)
                backtrack(index + 1, path)
                # Backtrack by removing the letter before moving onto the next
                path.pop() # <--- 为什么官方的需要pop而neet code的不用。因为官方的append这个动作是 happened outside the recursion function.
        
        backtrack(0, [])

        return res
        

# 11.29 复习自己写了个level order traversal
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapper = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        if len(digits) == 1:
            return list(mapper[digits])
        
        q = deque(list(mapper[digits[0]]))
        i = 1
        
        while q:
            if i >= len(digits):
                break
            d = digits[i]
            for _ in range(len(q)):
                c1 = q.popleft()
                for c2 in mapper[d]:
                    q.append(c1 + c2)
            i += 1
        
        return q