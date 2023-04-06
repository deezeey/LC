from typing import List
from collections import defaultdict, deque

# 1.24 first try，debug以后写出来了了
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        count = [0] * numCourses
        res = []
        q = deque()

        # build graph & count outdegree
        for c, req in prerequisites:
            graph[req].append(c)
            count[c] += 1
        # push 0 outdegree to res and edit count
        for i, v in enumerate(count):
            if v == 0:
                q.append(i)
        while q:
            req = q.popleft()
            res.append(req)
            for c in graph[req]:
                count[c] -= 1
                if count[c] == 0:
                    q.append(c)
                    # graph[req].remove(c)  #一开始有这行迟迟过不了，remove from graph是没必要的
        # return res if len(res) == numCourses else []
        return res if len(res) == numCourses else []