from typing import List
from collections import deque
# 10.07 first try, 自己不断修修改改很久写出来的，能pass好几个case但是submission还是fail了。
# failed case: numCourses = 7, prerequisites = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]
# 然后看了下neetcode发现我写的基本就是他写的dfs solution而且代码都很像，i almost got it...可能太晚了脑子转不动了吧
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_dict = {}
        for ls in prerequisites:
            if ls[0] in prereq_dict:
                prereq_dict[ls[0]].append(ls[1])
            else:
                prereq_dict[ls[0]] = [ls[1]]

        forbidden = set()
        res = []
        def checkCourse(i):
            if i in forbidden:
                return False
            if i in prereq_dict:
                forbidden.add(i)
                for j in prereq_dict[i]:
                    if j in prereq_dict:
                        return checkCourse(j)
                    else:
                        continue
                forbidden.remove(i)
            else:
                return True
            return True
        
        for i in range(numCourses):
            res.append(checkCourse(i))

        return all(res)
        

# neetcode 的 DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_dict = {}
        for ls in prerequisites:
            if ls[0] in prereq_dict:
                prereq_dict[ls[0]].append(ls[1])
            else:
                prereq_dict[ls[0]] = [ls[1]]

        forbidden = set()

        def checkCourse(i):
            if i in forbidden:
                return False
            if i not in prereq_dict:
                return True
            
            forbidden.add(i)
            for j in prereq_dict[i]:
                if not checkCourse(j):
                    return False
            forbidden.remove(i)
            prereq_dict[i] = []
            return True
        
        for i in range(numCourses):
            if not checkCourse(i):
                return False
        
        return True


# 11.21 复习自己写，pass不了numCourses = 2， prerequisites = [[1,0]]的test case.
# 还是一样的问题。思路是对的，但具体怎么写不太清晰，recursion的终止条件以及用for还是while都没想清楚就开始写了
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        goals = list(range(numCourses))
        cant = set()

        # 1) draw a graph with directions
        for a, b in prerequisites:
            if a in graph:
                graph[a].append(b)
            else:
                graph[a] = [b]

        # 2) check if there's any closed loop in the graph using dfs
        def dfs(course):
            if course in cant:
                return False
            goals.pop(course)
            cant.add(course)

            if course in graph:
                for required in graph[course]:
                    res = []
                    if required in cant:
                        return False
                    else:
                        res.append(dfs(required))
                        return all(res)
            
        # 3) for course in numCourses, apply dfs
        while goals:
            course = goals[-1]
            if course not in graph:
                goals.pop(course)
                continue
            else:
                return dfs(course)

# 看了答案自己写的
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        cant = set()

        # 1) draw a graph with directions
        for a, b in prerequisites:
            if a in graph:
                graph[a].append(b)
            else:
                graph[a] = [b]

        # 2) check if there's any closed loop in the graph using dfs
        def dfs(course):
            if course in cant:
                return False
            if course not in graph:
                return True
            cant.add(course)
            for required in graph[course]:
                if not dfs(required):
                    return False
            cant.remove(course)
            graph[course] = [] # <--- 一开始漏了这行会TLE
            return True
            
        # 3) for course in numCourses, apply dfs
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True

# 九章的解法和neet code不一样是topology式的，更加高效
# 这道题顺序无所谓, 正常思路是从第一个没有依赖的课程逐步宽搜, 然后依次把依赖减为0的课程加入结果中. 
# 也可以反向思考, 把每个课程依赖的课程都扫描(这里的indegree其实就是相当于前置课程的outdegree), 当前置课程的outdegree全部检查过了之后, 这个课程就可以加入结果了. （这个是neet code的解法）
# 这道题宽搜的目的主要是排除图中的环, 所以可以通过, 不过这种方式获取的结果需要reverse

# 拓扑的复杂度分析
# 时间复杂度O(V + E)
# 建图，扫描一遍所有的边O(E)。
# 每个节点最多入队出队1次，复杂度O(V)。
# 邻接表最终会被遍历1遍，复杂度O(E)。
# 综上，总复杂度为O(E + V)。
# 空间复杂度O(V + E)
# 邻接表占用O(E + V)的空间。
# 队列最劣情况写占用O(V)的空间。
# 综上，总复杂度为O(V + E)。
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # write your code here
        n = numCourses
        node_neighour = {x : [] for x in range(n)}
        node_indegree = {x : 0 for x in range(n)}
        
        for from_node, to_node in prerequisites:
            node_indegree[to_node] += 1 # indegree代表这个node被多少个其他node require
            node_neighour[from_node].append(to_node) # neighbour是这个node require的node
        
        start_nodes = [node for node in range(n) if node_indegree[node] == 0]
        queue = deque(start_nodes)
        result = []

        while queue :
            node = queue.popleft()
            result.append(node) # 没人require当前node，先把node放res里
            for neighbor in node_neighour[node] : # 看当前node需要的prerequisites
                node_indegree[neighbor] -= 1 # 需要这个prerequisite的node少了一个
                if node_indegree[neighbor] == 0 : # 如果没人需要这个prerequisite的话，放到q里
                    queue.append(neighbor)
        return len(result) == numCourses
                
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # write your code here
        n = numCourses
        node_neighour = {x : [] for x in range(n)}
        node_indegree = {x : 0 for x in range(n)}
        
        for from_node, to_node in prerequisites:
            node_indegree[from_node] += 1 # indegree代表这个node有多少prerequisites
            node_neighour[to_node].append(from_node) # neighbour是这个node被多少个node require
        
        start_nodes = [node for node in range(n) if node_indegree[node] == 0]
        queue = deque(start_nodes)
        result = []

        while queue :
            node = queue.popleft()
            result.append(node) # 当前node没有prerequisite，把node放res里
            for neighbor in node_neighour[node] : # 看需要当前node的node
                node_indegree[neighbor] -= 1 # 把这些node的prerequisite数量-1
                if node_indegree[neighbor] == 0 : # 如果减完1这个node不再需要任何node
                    queue.append(neighbor) # 他也可以被放进res里
        return len(result) == numCourses

# 1.13 复习自己记得思路不太记得graph的写法了。过不了prerequisites = [[0,1]]， numCourses = 2的case
# 其实只要initiate as dict然后记得用一个res keep track of 剥掉的node就好了
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph, count indregrees
        graph = [set() for _ in range(numCourses)]
        indegrees = [0] * numCourses
        for c, req in prerequisites:
            graph[c].add(req)
            indegrees[req] += 1
        
        # start from 0 indegree nodes, detach nodes
        while len(indegrees) > 0:
            if 0 not in indegrees:
                return False
            cur_c = indegrees.index(0)
            del indegrees[cur_c]
            for req_c in graph[cur_c]:
                indegrees[req_c] -= 1
            del graph[cur_c]
        
        return True
        
# 改一下就能过
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {x: set() for x in range(numCourses)}
        indegrees = {x: 0 for x in range(numCourses)}
        q = deque()
        res = set()

        # build graph, count indregrees
        for c, req in prerequisites:
            graph[c].add(req)
            indegrees[req] += 1

        # put 0 indegree nodes to q
        for c, d in indegrees.items():
            if d == 0:
                q.append(c)

        # start from 0 indegree nodes, detach nodes
        while q:
            cur_c = q.popleft()
            res.add(cur_c)
            for req_c in graph[cur_c]:
                indegrees[req_c] -= 1
                if indegrees[req_c] == 0:
                    q.append(req_c)
        
        return len(res) == numCourses 