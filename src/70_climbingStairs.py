# 9.29自己没想明白怎么求diff permutation，看了neet code解释发现就是fibonacci
# 但是仍然需要想明白从decision tree是如何总结成如此简单的数学公式的
# 它是一个bottom up DP solution。假设n是5。他先看base case。5->5只有1种方式。4->5也是只有1种方式。
# 3->5可以是take 1 step，变成4-->5这个问题，或者take 2 steps变成5-->5这个问题。所以有1+1 = 2种方式
# 2-->5可以是take 1 step变成3-->5或者take 2 steps变成 4-->5，即 2 + 1 = 3种方式
class Solution:
    def climbStairs(self, n: int) -> int:
        last, last_prev = 1, 1
        for _ in range(n - 1):
            temp = last_prev
            last_prev = last + last_prev
            last = temp
        return last_prev

# 11.27 复习自己写。能跑过16/45 test cases但是TLE。这个是brute force way
from collections import deque
class Solution:
    def climbStairs(self, n: int) -> int:
        # num of leaf nodes in the decision tree
        res = 0
        dp = deque([n])
        while dp:
            cur = dp.popleft()
            if cur == 0:
                res += 1
            if cur >= 2:
                dp.extend([cur-2, cur-1])
            if cur == 1:
                dp.append(cur-1)
        return res

# 看了neet code视频以后自己补写一个好理解一点的dp. T O(n) M O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        dp[n], dp[n-1] = 1, 1

        for i in range(n-2, -1, -1):
            dp[i] = dp[i+1] + dp[i+2]

        return dp[0]
        
# 更省memory的写法，比neet code还要简单的写法。这个T O(n) M O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        # before_last和last台阶都只有一种方式到last台阶，比如台阶4和台阶5都是1
        before_last, last = 1, 1

        for _ in range(n-1):
            # 台阶3=台阶4+台阶5，台阶4仍然是4但是assign var从before_last变成last
            before_last, last = before_last + last, before_last

        return before_last