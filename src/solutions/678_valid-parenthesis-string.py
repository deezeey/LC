# 2.1 first try，自己写的能过俩test case但是我知道肯定逻辑有漏洞
class Solution:
    def checkValidString(self, s: str) -> bool:
        # if start with close, return False
        # count open and * until we encounter the first close or reach the last idx
        # start subtracting after above condition, close means open -= 1, 
        # if we see an open again, check cur_open == 0 or cur_* - cur_open >= 0, if not return False
        # now open should be 0, * may > 0, continue from first row
        cur_open, cur_star = 0, 0
        for c in s:
            if c == ")":
                if cur_open:
                    cur_open -= 1
                else:
                    cur_star -= 1
                if not cur_star >= 0:
                    return False
            if c == "(":
                cur_open += 1
            if c == "*":
                cur_star += 1
        return cur_open == 0

# greedy解法
# 基本思想是，用两个var来记录当前位置，最多和最少有可能有几个open bracket。* 如果是（会让count +1，是空格会让count不变，是）会让count -1。所以碰到*会让min-1，max+1
# （*() 的话， min, max的变化会是 1，1  ---> 0, 2 ---> 1, 3 ---> 0, 2。最后0在range内。
# （*())的话， min, max的变化会是 1，1  ---> 0, 2 ---> 1, 3 ---> 0, 2 ---> -1, 1。这仍然valid，0在range内，这个情况valid是因为 * 可以为空格
# （*()))的话， min, max的变化会是 1，1  ---> 0, 2 ---> 1, 3 ---> 0, 2 ---> -1, 1 ---> -2, 0, 这仍然valid，0在range内，这个情况valid是因为 * 可以为(
# （*())))的话， min, max的变化会是 1，1  ---> 0, 2 ---> 1, 3 ---> 0, 2 ---> -1, 1 ---> -2, 0 ---> -2, -1 这就不valid，这个情况即使 * 为(，还是有个多余的close bracket
class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open, max_open = 0, 0
        for c in s:
            if c == "(":
                min_open += 1
                max_open += 1
            if c == "*":
                min_open -= 1
                max_open += 1
            if c == ")":
                max_open -= 1
                min_open -= 1
            if max_open < 0:
                return False
            if min_open < 0: # 缺了这行会过不了"(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"这个case
                min_open = 0 # 为什么呢，因为min_open < 0代表加上*有超出open bracket个数的close bracket。我们没这个必要自找麻烦这不make sense
        return min_open == 0