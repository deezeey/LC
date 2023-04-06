from collections import defaultdict
from functools import lru_cache
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

# 1.19 first try自己写的能过160/180 cases，碰到[[1,1],[0,1]]挂了
class Solution:
    def __init__(self):
        self.ppl = set()
        self.known_by_hash = defaultdict(set)

    def checkConnection(self, a, b):
        a_knows_b = knows(a, b)
        b_knows_a = knows(b, a)
        if a_knows_b:
            self.ppl.add(a)
            self.known_by_hash[b].add(a)
        else:
            self.ppl.add(b)
        if b_knows_a:
            self.ppl.add(b)
            self.known_by_hash[a].add(b)
        else:
            self.ppl.add(a)
        if a not in self.ppl:
            return a
        if b not in self.ppl:
            return b
        else:
            return False

    def findCelebrity(self, n: int) -> int:
        for i in range(n-1):
            if i in self.ppl:
                continue
            for j in range(n):
                if j != i and j not in self.known_by_hash[i]:
                    potential_celeb = self.checkConnection(i, j)
                    if not potential_celeb:
                        break
            if len(self.known_by_hash[i]) == n-1:
                return i
        return -1

# 正解和我的思路是一致的，a knows b，则排除a，a doesn't know b, 则排除b。
# 但是它的思路更佳，因为它按顺序问，0 know 1，那么排除0，candidate变1，接下来直接check 1 knows 2？注意这里不用回头check does 1 know 0。
# 1 doesn't know 2, 排除2，继续check1。1 knows 3？no，继续check 1，直到最后就剩1个candidate（因为题目guarantee只有最多一个celeb）
# 最后再check一遍是否所有其他人都know candidate就好
# T O(n), 两个for loop各iterate thru n一遍。 M O(1)
class Solution:
    
    @lru_cache(maxsize=None)
    def cachedKnows(self, a, b):
        return knows(a, b)
    
    def findCelebrity(self, n: int) -> int:
        self.n = n
        celebrity_candidate = 0
        for i in range(1, n):
            if self.cachedKnows(celebrity_candidate, i):
                celebrity_candidate = i #这个loop是很不常规的写法，i走它自己的，candidate换了就换了，i还是继续当前位置下一位
        if self.is_celebrity(celebrity_candidate):
            return celebrity_candidate
        return -1

    def is_celebrity(self, i):
        for j in range(self.n):
            if i == j: continue
            if self.cachedKnows(i, j) or not self.cachedKnows(j, i): # 一开始觉得这里不用再重复checkself.cachedKnows(i, j)，但是过不了[[1,1],[1,1]]
                return False
        return True