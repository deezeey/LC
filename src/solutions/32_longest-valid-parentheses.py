# 3.13 first try过不了 135/231 ")()())()()("
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s or len(s) == 1:
            return 0
        # "(()", ")())())"
        # if in a str every opened bracket is closed then it is a valid str
        # iterate from r to l, use a num to store close bracket, open bracket makes close bracket count -= 1, add 2 to cur_max
        # if close count == 0, update res, if close go below 0, update res to be max(cur_max, res), and update cur_max to be 0
        close_cnt, cur_max, res = 0, 0, 0
        for i in range(len(s)-1, - 1, -1):
            c = s[i]
            if c == "(":
                close_cnt -= 1
                if close_cnt >= 0:
                    cur_max += 2
                    res = max(cur_max, res)
                else:
                    close_cnt, cur_max = 0, 0
            elif c == ")":
                close_cnt += 1
        return res
    
# 新的想法，一个valid substring外面包了一个valid substring或者它end之后接了另一个valid substring那他们的length就可以被加起来