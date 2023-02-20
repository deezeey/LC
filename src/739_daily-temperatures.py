from typing import List

# 12.06 first try自己写的碰到一个有几千个47度的test case TLE了
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(res) - 1, -1, -1) :
            temp = []
            while stack and stack[-1] <= temperatures[i]:
                cur = stack.pop()
                temp.append(cur)
            res[i] = len(temp) + 1 if stack else 0
            stack.extend(temp[::-1])
            stack.append(temperatures[i])
        
        return res


# 正确答案。不要没想明白算法就急着开始写代码！这点太难戒了。O(n) O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (temp, index)
        res = [0] * len(temperatures)

        for i, v in enumerate(temperatures):
            while stack and stack[-1][0] < v:
                _, prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            stack.append((v, i))
        
        return res


# 12.08 复习， 写了复杂了，多了不需要的条件句
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures[:-1]):
            if temperatures[i + 1] <= t:
                stack.append((i, t))
            else:
                res[i] = 1
                while stack and temperatures[i + 1] > stack[-1][1]:
                    prev_i, _ = stack.pop()
                    res[prev_i] = i + 1 - prev_i
        
        return res

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                prev_i, _ = stack.pop()
                res[prev_i] = i - prev_i
            stack.append((i, t))
                
        return res

# 1.2 复习还记得
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # (index, temp)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                prev_i, prev_temp = stack.pop()
                res[prev_i] = i - prev_i
            stack.append((i, temperatures[i]))
        
        return res