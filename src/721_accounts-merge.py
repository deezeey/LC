from collections import defaultdict
from typing import List

# 10.07 first try 自己没有什么思路， 看了youtube cracking faang的解
# 是把所有connected email画成图，然后用while loop进行dfs穷尽所有网点，这些网点全部belong to 1 person
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set) # <--- defaultdict可以让我们方便的initialize empty set
        email_to_name = {}

        # build the graph
        for accnt in accounts:
            name = accnt[0]
            for email in accnt[1:]: # <---- 一开始我觉得可以从[2:]开始，1单独处理一下，后来发现不行，因为如果这个accnt只有1个email呢
                graph[accnt[1]].add(email) # <--—— 灵性画图，第一个email连接到所有email
                graph[email].add(accnt[1]) # <---- 所有email都连接到第一个email
                email_to_name[email] = name
        # 这个图画完，即使不同accnt在for loop的不同round里被处理，
        # 只要他们之间有一个共同email，图上他们一定会有路连在一起的，所以我们待会儿可以dfs穷尽所有email

        res = []
        visited = set()

        # bfs
        for email in graph:
            if email not in visited: # <--- email没有被visit过，代表这个part还没有被traverse过，我们从这个点，搜寻connected的整个email网络
                stack = []
                email_list = set()
                stack.append(email)
                while stack:
                    node = stack.pop()
                    email_list.add(node)
                    visited.add(node)
                    for connected in graph[node]:
                        if connected not in visited:
                            email_list.add(connected)
                            visited.add(connected)
                            stack.append(connected)
                res.append([email_to_name[email]] + sorted(email_list)) # <--- 这行的缩紧位置为什么在这里，因为while loop走完代表图这个dfs遍历结束
        
        return res


# 九章uf答案, 时间复杂度应该比bfs优秀
# Cccus在这个答案里写了解决连通性问题时候，bfs和union find的区别 https://www.jiuzhang.com/problem/accounts-merge/
class Solution:
    def accountsMerge(self, accounts):
        self.f = {} # the father dict to represent the union tree: self.f[email] = email
        self.name = {} # email to name mapper

        # build union tree / father dict(self.f)
        for account in accounts:
            for j in range(1, len(account)):
                if account[j] not in self.f:
                    self.f[account[j]] = account[j]
                self.union(account[1], account[j]) # all the emails are unioned with the 1st email, so they're in the same union
                self.name[account[j]] = account[0]
        
        # build node to root mapper from the union tree
        unions = defaultdict(set)
        for account in accounts:
            for j in range(1, len(account)):  #也可以不用两个for loop用 for k in self.f.keys():，但是那样有额外开销
                root = self.find(account[j]) # find the root for all the emails, 非常重要这里要call find来找root。而不是self.f[accnt[i]]一定是root
                unions[root].add(account[j]) # emails with the same root belongs to the same person/union

        res = []
        for k, v in unions.items():
            res.append([self.name[k]] + sorted(list(v)))
        return res
    
    def union(self, a, b):  # <--- standard union func, merges 2 unions to the same root
        fa = self.find(a)
        fb = self.find(b)
        if fa != fb:
            self.f[fb] = fa
    
    def find(self, a): # <--- standard find func, returns the root of an element
        if self.f[a] != a:
            return self.find(self.f[a])
        else:
            return a

# 演示一下how union find works for this case
# 假设我们的accounts是[[1, 2, 3, 4], [2, 5], [6, 5]], 我们知道union find得有办法把这三个list都联通起来
# 在build union环节。
# iterate thru [1, 2, 3, 4]，会得到 f[1] = 1, f[2] = 1, f[3] = 1, f[4] = 1
# iterate thru [2, 5]，会得到 f[2] = 1, f[5] = 1
# iterate thru [6, 5], 会得到 f[6] = 6, f[5] = 1, f[1] = 6
# 最后成型的 f looks like: { 1: 6, 2: 1, 3: 1, 4: 1, 5: 1, 6: 6}
# 这就是为什么最后我们要重新iterate thru all the emails再一遍，去找每一个的root,并把他们加到unioned解集里。因为father字典不能保证每个k的v都是它的root。需要call find来找
        

# 11.21 复习自己写出来了build graph部分但是下面怎么bfs没记起来，其实倒是不难但是想通逻辑需要脑子清晰
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # common email in 2 lists means merging, they definitely have the same name
        # name ---> email indegree > 1
        # need a email to name mapping
        # link all the emails
        connected_emails = defaultdict(set)
        email_to_name = {}

        for accnt in accounts:
            name = accnt[0]
            for i in range(1, len(accnt)):
                email_to_name[accnt[i]] = name
                connected_emails[accnt[1]].add(accnt[i])
                connected_emails[accnt[i]].add(accnt[1])
        
        res = []
        visited = set()

        for email in connected_emails:
            if email not in visited:
                q = []
                email_list = set()
                q.append(email)
                while q:
                    cur = q.pop()
                    email_list.add(cur)
                    visited.add(cur)
                    for connected in connected_emails[cur]:
                        if connected not in visited: # <--- 一开始漏了这行迟迟跑不过
                            email_list.add(connected)
                            visited.add(connected)
                            q.append(connected)
                res.append([email_to_name[email]] + sorted(email_list))
        
        return res

# 重新研习了一下union find然后自己默写了一遍union find
# 有路径压缩的话，find效率是O(1), 没有的话O(logn)。
# 这样假设n为邮箱数量。九章说T O(n) 因为3个for loop对所有email进行了1次union,一次find。路径压缩后这俩都是O(1)
# 但我觉得sorted也是O(nlogn)啊，所以应该还是O(nlogn)把
# M O(n) 因为我们存了 f， name_mapper都是n长
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # union find helper function
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                f[rb] = ra

        def find(a): 
            if f[a] != a:
                # f[a] = find(f[a]) # <--- 加上这行就是路径压缩。即一旦发现不是根的节点，把他的父直接设置成根
                # 可以提升效率。因为我们并不关心图的形状，只关心节点的根。
                return find(f[a])
            return a

        # build union tree
        f = {} # father mapper of union tree, f[email] = email
        name_mapper = {} # {email: name}
        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                if account[i] not in f:
                    f[account[i]] = account[i]
                union(account[1], account[i])
                name_mapper[account[i]] = name

        # create node to root mapper
        root_mapper = defaultdict(set)
        for account in accounts:
            for i in range(1, len(account)):
                root = find(account[i])
                root_mapper[root].add(account[i])

        # build result
        res = []
        for k, v in root_mapper.items():
            res.append([name_mapper[k]] + sorted(v))
        
        return res


# 1.13 复习自己写出来了BFS
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        email_to_name = {}
        res = []
        visited = set()

        # build graph
        for accnt in accounts:
            name = accnt[0]
            for e in accnt[1:]:
                graph[accnt[1]].add(e)
                graph[e].add(accnt[1])
                email_to_name[e] = name
        
        # connect nodes
        for node in graph:
            if node in visited:
                continue
            q = deque()
            q.append(node)
            email_ls = set()
            while q:
                n = q.pop()
                if n in email_ls:
                    continue
                email_ls.add(n)
                visited.add(n)
                q.extend(graph[n])
            email_ls = sorted(list(email_ls))
            name = email_to_name[email_ls[0]]
            res.append([name] + email_ls)
        
        return res

# 重新写一遍union find
class Solution:
    def __init__(self):
        self.f = {}
        self.e_to_name = {}

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # build union tree
        for accnt in accounts:
            name = accnt[0]
            for i in range(1, len(accnt)):
                if accnt[i] not in self.f:
                    self.f[accnt[i]] = accnt[i]
                self.union(accnt[i], accnt[1])
                self.e_to_name[accnt[i]] = name
        
        # merge unioned nodes into a set
        mapper = defaultdict(set)
        res = []
        for accnt in accounts:
            for i in range(1, len(accnt)):
                fi = self.find(accnt[i])  # 一开始这行写了 fi = self.f[accnt[i]]过不了的。记住这里一定要重新call find找root！！
                mapper[fi].add(accnt[i])
        for k, v in mapper.items():
            res.append([self.e_to_name[k]] + sorted(v))
        return res

    def find(self, a):
        if self.f[a] != a:
            return self.find(self.f[a])
        else:
            return a

    def union(self, a, b):
        fa, fb = self.find(a), self.find(b)
        if fa != fb:
            self.f[fa] = fb