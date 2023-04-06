from typing import List
from collections import deque

# 1.26 first try自己30min之内用BFS做的，卡在第41个case上过不了
# 我没太想明白为什么过不了
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # BFS
        # build graph
        graph = {i:[] for i in range(n)}
        for f, t, p in flights:
            graph[f].append([p, t])

        # run BFS from src
        q = deque([[0, src]])
        visited = set()
        res = []
        k = k + 1
        while q and k > 0:
            k -= 1
            for _ in range(len(q)):
                price, node = q.popleft()
                if node in visited: 
                    continue
                visited.add(node)
                for nei_price, nei in graph[node]:
                    if k >= 0 and nei == dst:
                        res.append(price + nei_price)
                    q.append([price + nei_price, nei])
        print(res)
        return min(res) if res else -1

# neetcode正解是用bellman ford algo，其实它也是BFS, 但是每次不是check当前node可以access的edge而是check所有edge
# n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1 这个案例
# price array的演变过程是 [0, inf, inf, inf] ---> [0, 100, inf, inf] ---> [0, 100, 200, 700], 然后k就用完了，结束loop
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # bellman ford algo
        price = [float("inf")] * n
        price[src] = 0
        for _ in range(k + 1):
            tmp_price = price.copy()
            for f, t, p in flights:
                if price[f] == float("inf"):
                    continue
                if price[f] + p < tmp_price[t]:
                    tmp_price[t] = price[f] + p
            price = tmp_price
        return -1 if price[dst] == float("inf") else price[dst]
