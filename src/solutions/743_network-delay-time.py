from typing import List
from collections import defaultdict
import heapq


# 1.26 first try，刚刚做了1584 min-cost-to-connect-all-points,写这题就是加了一个需要把min_hp里的dist -1的脑筋急转弯而已
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build graph
        graph = {i:[] for i in range(n + 1)} # just ignore 0 index and leave it unused
        for s, t, d in times:
            graph[s].append([d, t])
        # run Prims'algo using min heap
        min_hp = [[0, k]] #(time, node)
        visited = set()
        res = 0
        while min_hp and len(visited) < n:
            time, node = heapq.heappop(min_hp)
            if node in visited:
                continue
            res += time
            visited.add(node)
            new_min_hp = [[t - time if t - time >= 0 else 0, i]for t, i in min_hp]
            for nei_time, nei in graph[node]:
                new_min_hp.append([nei_time, nei])
            heapq.heapify(new_min_hp)
            min_hp = new_min_hp
        return res if len(visited) == n else -1

# 看了下neetcode的我还是写的复杂了，不需要-1，因为d其实可以计算到达时间再push到hp里
# O(E * logV)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1
