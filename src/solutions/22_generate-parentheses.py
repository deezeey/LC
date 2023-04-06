from typing import List
# 12.06 first try。自己的思路是对的，backtracking + stack. 但是这个backtracking我没写出来

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # initiate open & close count to n
        # first one needs to be open. res = ["("] to start, if stack is empty, next has to be open
        # next to open we can put either open or close as long as their count is not 0
        # each time we add open, we need to push it to a stack
        # after close we pop from stack

        res = []
        stack = 0

        def backtrack(open_count, close_count, cur):
            nonlocal stack
            if open_count == close_count == 0:
                res.append(cur)
                return
            if not stack:
                cur += "("
                stack += 1
                open_count -= 1
                backtrack(open_count, close_count, cur)
            elif not open_count:
                cur += ")"
                stack -= 1
                close_count -= 1
                backtrack(open_count, close_count, cur)
            else:
                # all edge case handled now we can choose to append either open or close next
                for c in ("(", ")"):
                    cur += c
                    if c == "(":
                        stack += 1
                        open_count -= 1
                        backtrack(open_count, close_count, cur)
                    if c == ")":
                        stack -= 1
                        close_count -= 1
                        backtrack(open_count, close_count, cur)
        
        backtrack(n, n, "")
        return res


# 正确代码没那么复杂
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(open_count, close_count):
            if open_count == close_count == 0:
                res.append("".join(stack))
                return
            if open_count > 0:
                stack.append("(")
                backtrack(open_count - 1, close_count)
                stack.pop()
            if close_count > open_count:
                stack.append(")")
                backtrack(open_count, close_count - 1)
                stack.pop()
        
        backtrack(n, n)
        return res


# 12.08 复习自己写，虽然写出来了但是我感觉对这个call stack的理解还是不是很清楚
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []

        def backtrack(open_count, close_count):
            if open_count == close_count == 0:
                res.append("".join(cur))
                return
            if open_count > 0:
                cur.append("(")
                open_count -= 1
                backtrack(open_count, close_count)
                cur.pop()
                open_count += 1
            if close_count > open_count:
                cur.append(")")
                close_count -= 1
                backtrack(open_count, close_count)
                cur.pop()
                close_count += 1

        backtrack(n, n)
        return res

# 1.2 复习，度假回来不记得这个backtracking怎么写了。看了答案又背了一遍
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = ""

        def backtrack(open_cnt, close_cnt):
            nonlocal cur
            print(cur, open_cnt, close_cnt)
            if open_cnt == close_cnt == 0:
                res.append(cur)
                return
            if open_cnt > 0:
                cur += "("
                open_cnt -= 1
                backtrack(open_cnt, close_cnt)
                cur = cur[:-1]
                open_cnt += 1
            if close_cnt > open_cnt:
                cur += ")"
                close_cnt -= 1
                backtrack(open_cnt, close_cnt)
                cur = cur[:-1]
                close_cnt += 1

        backtrack(n, n)
        
        return res

# print(cur, open_cnt, close_cnt)的call stack
# 3 3
# ( 2 3
# (( 1 3
# ((( 0 3
# ((() 0 2
# ((()) 0 1
# ((())) 0 0
# -----------
# (() 1 2 # 这里其实是backtrack(0, 0) return后，返回了（0，1），（0，2），（0，3）
# 然后执行了if open_cnt里面的cur = cur[:-1] open_cnt += 1, 
# 然后往下执行if close_cnt > open_cnt里面，此时，close_cnt 3, open_cnt 1, 
# 满足条件，所以append ")", close_cnt -= 1, backtrack(1, 2), 才又再碰到了print语句
# (()( 0 2
# (()() 0 1
# (()()) 0 0
# (()) 1 1
# (())( 0 1
# (())() 0 0
# () 2 2
# ()( 1 2
# ()(( 0 2
# ()(() 0 1
# ()(()) 0 0
# ()() 1 1
# ()()( 0 1
# ()()() 0 0