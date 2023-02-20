
from typing import List
from collections import heapq
# 1.26 firt try自己想了5分钟，自己的思路是
# 计算所有点到所有点的距离，存在（距离，点A，点B)的tuple里
# 从小到大排序，然后开始backtracking直到所有点都被连结起来
# 我的想法和正解大概50%一致。prims algo不一样的地方是
# 1）用min heap instead of sort
# 2）不需要backtrack，

# neetcode的解法是用prim‘s algo to find minimum spanning tree（MST）
# T O(n^2logn) n^2是edge数量，logn是prim algo的消耗
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # build adj lists
        N = len(points)
        adj = {i:[] for i in range(N)} # i is the index of the node, [] contains [dist, idx of another node]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1) 
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0
        visited = set()
        min_hp = [[0, 0]] # the dist to connect node 0 to itself is 0
        while len(visited) < N:
            dist, i = heapq.heappop(min_hp)
            if i in visited:  #千万不要忘了这个check否则会产生错误答案
                continue
            visited.add(i)
            res += dist
            for nei_dist, nei in adj[i]:
                if nei in visited:
                    continue
                heapq.heappush(min_hp, [nei_dist, nei])
        return res