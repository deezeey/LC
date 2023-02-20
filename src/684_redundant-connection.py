from typing import List

# 1.25 first try一开始自己没意识到是union find问题，觉得很简单，后来意识到了但是懒得自己想怎写了
# 这个naive solution能跑过10个case吧
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        exist = set()
        connected = []
        for a, b in edges:
            if a not in exist and b not in exist:
                connected.append(set([a, b]))
            else:
                for s in connected:
                    if a in s and b in s:
                        return [a, b]
                    if a in s:
                        s.add(b)
                    if b in s:
                        s.add(a)
            exist.update([a, b])

# neetcode union find 解法
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # just ignore the 0 index
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            # 假设6的parent是1，1的parent是3，3是root，
            # 那么parent[1] != 1,所以set parent[1] = parent[3] = 3
            p = parent[n]
            while parent[p] != p:
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
                return [n1, n2]

