from typing import List

# 1.25 first try，刚刚写过684，所以这题10分钟写出来了
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # union find
        parent = [i for i in range(n)]
        rank = [1] * n
        uniq_p = set()

        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(a, b):
            pa, pb = find(a), find(b)
            if rank[pa] > rank[pb]:
                parent[pb] = pa
                rank[pa] += rank[pb]
            else:
                parent[pa] = pb
                rank[pb] += rank[pa]
        
        for n1, n2 in edges:
            union(n1, n2)
        
        for n in range(n):
            pn = find(n)
            if pn not in uniq_p:
                uniq_p.add(pn)

        return len(uniq_p)