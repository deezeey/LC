from typing import List
from collections import defaultdict

#10. 14 first try自己想到了一定是用前1个或者2个 connection最多的node为答案但是我不知道怎么算height。。。
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        distinct_nodes = set([num for ls in edges for num in ls])

        # build graph
        graph = {node : [] for node in distinct_nodes}
        for edge in edges:
            node1, node2 = edge[0], edge[1]
            graph[node1].append(node2)
            graph[node2].append(node1)

        # order the nodes in graph by count of appearance
        graph = dict(sorted(graph.items(), key=lambda x: len(x[1]), reverse = True))
        print(graph)


# 九章的解
# 复习了一下拓扑排序。这题的point应该就是：拓扑排序不止indegree==0可以当条件。 无向图，这里其实处理的时候是当作双向图。
# 单向图的时候 indegree==0 的时候把下一个item push。 双向图的时候，indegree<=1 的时候把下一个item push。 （==1的时候是双向撤销了1个依赖，已经没有除了当前点之外的依赖了，==0是个corner case，只有一个点）
# 按照层来遍历 for _ in range(len(q))，最后一层就是答案。
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        
        graph = [set() for _ in range(n)]
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
            
        # the intuition is that in a connected graph,
        # if you pick a node of degree 1 as the root
        # then the resulting tree has the max ht.
        # so trim the leaves until there are at most 2
        # and at least 1 node left.
        
        # graph = [(3), (3), (3), (0, 1, 2, 4), (3, 5), (4)]
        leaves = [i for i in range(n) if len(graph[i]) == 1] #[0, 1, 2, 5]
        while n > 2:
            n -= len(leaves) # 6 -= 4 = 2
            new_leaves = []
            for leaf in leaves: # leaf 0
                neighbor = graph[leaf].pop() # neighbor = graph[0].pop() = 3
                graph[neighbor].remove(leaf) # graph[3].remove(0)
                if len(graph[neighbor]) == 1: new_leaves.append(neighbor) 
            
            leaves = new_leaves
        
        return leaves


# 11.22 复习自己写，完全不记得无向图最小高度树只可能有1或2个节点了。更不记得剥叶子这个技巧。
# T O(v + e), M O(v)
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # node with most connections should be the root?
        # we want the tree to be as flat as possible
        indegree = defaultdict(int) # M O(v)
        graph = defaultdict(set) # M O(v)

        for a, b in edges: # T O(e)
            graph[a].add(b)
            graph[b].add(a)
            indegree[a] += 1
            indegree[b] += 1
    
        leaves = [k for k in indegree.keys() if indegree[k] == 1] # T O(v)

        # get rid of the leaves until we have 2 nodes left
        while n > 2: # T O(v)
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:  # <--- 一开始用了while loop是不行的，不要什么都想着bfs的方式写。这个例子是要一批一次性处理完的
                nbr = graph[leaf].pop()
                graph[nbr].remove(leaf)
                indegree[leaf] -= 1
                indegree[nbr] -= 1
                if indegree[nbr] == 1:  # <-- 用 <= 1不行因为example1会重复添加node 1到new_leaves
                    new_leaves.append(nbr)
            leaves = new_leaves
        
        # return remaining leaves
        return leaves


# 1.14 复习，过不了edges = [[0,1],[0,2],[0,3],[3,4],[4,5]]，我output[3,4]， expected[3]
# 还是关于如何让代码在剩1个和剩2个情况下都work没有办法想通
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 2:
            return edges[0]
        if n == 1:
            return [0]

        graph = defaultdict(set)
        cnt = defaultdict(int)
        nodes = set()

        # build graph
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
            cnt[a] += 1
            cnt[b] += 1
            nodes.update({a, b})
        
        # peel off cnt 1 nodes until there are at most 2 left
        q = deque()
        for k, v in cnt.items():
            if v == 1:
                q.append(k)
        
        while q:
            node = q.popleft()
            nodes.remove(node)
            for connect in graph[node]:
                graph[connect].remove(node)
                cnt[connect] -= 1
                if cnt[connect] <= 1 and len(nodes) > 3:
                    q.append(connect)
        
        return list(nodes)

# 稍微改了下过了
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(set)
        cnt = defaultdict(int)
        nodes = set()

        # build graph
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
            cnt[a] += 1
            cnt[b] += 1
            nodes.update({a, b})
        
        # peel off cnt 1 nodes until there are at most 2 left
        q = []
        for k, v in cnt.items():
            if v == 1:
                q.append(k)

        while len(nodes) > 2:  # 首先nodes count > 2才能执行是没错的
            new_q = []  # 使用new_q暂存当前q里的leaves剥离后下一批leaves，不能直接append new leaves到q里，这样我们不能在一层leaves剥完再次check是否还剩>2个node
            while q: # 这里其实用for就够了因为只要一开始len > 2我们一定要整层leaves剥离完
                node = q.pop()
                nodes.remove(node)
                for connect in graph[node]:
                    graph[connect].remove(node)
                    cnt[connect] -= 1
                    if cnt[connect] <= 1:
                        new_q.append(connect)
            q = new_q
        return list(nodes)

# 修改了一下写的更逻辑通顺一点。
# 写代码之前一定要想好这个剥叶子和check的顺序和逻辑。剥叶子一定是一整层一整层剥的，所以是for loop。
# 而新叶子一定是要check剩余nodes数量大于2才开始剥的所以不能直接append到原来的leaves array里。
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(set)
        cnt = defaultdict(int)

        # build graph
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
            cnt[a] += 1
            cnt[b] += 1
        
        # peel off cnt 1 nodes(leaves) until there are at most 2 left
        leaves = [k for k,v in cnt.items() if v == 1]
        while n > 2:
            new_leaves = []
            for leaf in leaves:
                for connect in graph[leaf]:
                    graph[connect].remove(leaf)
                    cnt[connect] -= 1
                    if cnt[connect] <= 1:
                        new_leaves.append(connect)
                del graph[leaf]
                n -= 1
            leaves = new_leaves

        return graph.keys()