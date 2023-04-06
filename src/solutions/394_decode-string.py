# 3.8 first try 修修改改能过9个case把，string的edge case很多太麻烦
class Solution:
    def decodeString(self, s: str) -> str:
        # handle nested brackets
        #  k : 1 - 9
        # 3[a2[c1[b]]] --> 
        # cnt = 3, str = "a", next is a digit 2, so push to stack, [3], [a], 
        # cnt = 2, str = "c", closing bracket, compute, str = "cc", 
        # closing bracket, compute, cnt = 3, str = "a" + "cc", end of str, return

        # we compute res str when we see closing bracket or reached the end
        # if we see closing bracket and cnt = 0, pop cnt & str from stacks and (concatenate popped str + tmp res) x popped cnt and store this as tmp res
        # if cnt != 0, res = res + cnt * cur_str, set cnt = 0, cur_str = ""
        # when we see "[" we know to conclude cnt
        # cnt = 3, cur_str = a, 
        # when we see digit, if cur_str, we push existing cnt & cur_str to stack, and update cnt = digit, cur_str = "", otherwise, update cnt
        # [[3, "a"], [2, "c"]], cnt = 1, cur_str = "b"

        stack = [] # [k: int, chars: str]
        res = ""
        cnt, cur_str = 0, ""

        def _computeStr():
            nonlocal cnt, cur_str, res
            if cnt != 0:
                res = res + cnt * cur_str
            else:
                cnt, cur_str = stack.pop()
                cnt = max(1, cnt)
                res = (cur_str + res) * cnt
            cnt = 0
            cur_str = ""

        for c in s:
            if c in "0123456789":
                if cur_str:
                    stack.append([cnt, cur_str])
                    cnt = int(c)
                    cur_str = ""
                else:
                    cnt = cnt * 10 + int(c)
            elif c == "[":
                continue
            elif c == "]":
                _computeStr()
            else:
                cur_str += c
        
        res = res + cur_str
        while stack:
            _computeStr()

        return res

# 用2个stack的思路完全正确。但是需要一点逻辑整理能力。
# 每次遇到"[", append to stacks的数字代表后面的东西需要重复的次数，而str代表这个数字前面的str，而不是需要被重复的str，这点至关重要
class Solution:
    def decodeString(self, s: str) -> str:
        # only 4 types of c in s: digit, char, "[", "]"
        # before and after "[" it can be anything
        # before "]" is definitely a char or "]"
        # 3[a2[bc]]
        # num stack [3, 2]
        # str stack ["", "a"]
        # cur_str = "bc", 
        # closing bracket, compute by popping from num stack and str stack, cur_str = popped str + popped num * (cur_str) = "abcbc"
        # closing bracket, repeat above steps, "" + 3 * cur_str = "abcbcabcbcabcbc"

        # 3[z]2[2[y]pq4[2[jk]e1[f]]]ef
        # open bracket append to stacks
        # num stack [3]
        # str stack [""]
        # closing bracket, compute by popping from num stack and str stack, cur_str = "" + 3 * ("z") = "zzz"
        # cur_num = 2, open bracket, append to stacks
        # num stack [2]
        # str stack ["zzz"]
        # cur_num = 2, open bracket, append to stacks
        # num stack [2, 2]
        # str stack ["zzz", ""]
        # cur_str = "y", closing bracket, cur_str = "" + 2 * "y" = "yy"
        # cur_str = "yypq", cur_num = 4, open bracket, append to stacks
        # num stack [2, 4]
        # str stack ["zzz", "yypq"]
        # cur_num = 2, open bracket, append to stacks
        # num stack [2, 4, 2]
        # str stack ["zzz", "yypq", ""]
        # cur_str = "jk", closing bracket, cur_str = "" + 2 * "jk" = "jkjk"
        # cur_str = "jkjke", cur_num = 1, open brackte, append to stacks
        # num stack [2, 4, 1]
        # str stack ["zzz", "yypq", "jkjke"]
        # cur_str = "f", closing brackte, cur_str = "jkjke" + 1 * "f" = "jkjkef"
        # closing brackte, cur_str = "yypq" + 4 * "jkjkef" = "yypqjkjkefjkjkefjkjkefjkjkef"
        # closing brackte, cur_str = "zzz" + 2 * "yypqjkjkefjkjkefjkjkefjkjkef" = "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkef"
        # cur_str += "ef"
        # end of string, return cur_str
        num_stack, str_stack = [], []
        cur_num, cur_str = 0, ""
        for c in s:
            if c in "0123456789":
                cur_num = 10 * cur_num + int(c)
            elif c == "[":
                num_stack.append(cur_num)
                str_stack.append(cur_str)
                cur_num, cur_str = 0, ""
            elif c == "]":
                prev_num, prev_str = num_stack.pop(), str_stack.pop()
                cur_str = prev_str + prev_num * cur_str
            else:
                cur_str += c
        return cur_str