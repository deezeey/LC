from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # union find detect existing union and check if all unioned
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
            if pa == pb:
                return True
            if rank[pa] > rank[pb]:
                parent[pb] = pa
                rank[pa] += rank[pb]
            else:
                parent[pa] = pb
                rank[pb] += rank[pa]
            return False
        
        for n1, n2 in edges:
            if union(n1, n2):
                return False
        
        for i in range(n):
            p = find(i)
            if p not in uniq_p:
                uniq_p.add(p)
        
        return False if len(uniq_p) > 1 else True