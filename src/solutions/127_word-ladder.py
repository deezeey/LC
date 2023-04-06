from collections import defaultdict, deque
from typing import List

# 10.23 first try，自己想到了graph然后看了下BFS找graph最短路径
# 这个是能过的，但是，提交超时 :(
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        if beginWord not in wordList:
            wordList.append(beginWord)

        graph = defaultdict(set)

        def wordsDifferByOne(s1, s2):
            diff = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff += 1
            return diff == 1

        # build graph。这个build graph的方法要掌握
        for key_word in wordList:
            for compare_word in wordList:
                # print(key_word, compare_word, wordsDifferByOne(key_word, compare_word))
                if wordsDifferByOne(key_word, compare_word):
                    graph[key_word].add(compare_word)

        # print(graph)
        # calc min path using bfs
        def bfs(graph, start, end):  
            #这个和neet code的最大不同是，neet code是找路径长度，不需要返回路径。但这个是graph会记录路径。所以一个q里面只需要node。另一个q里面放的是path。
            path_q = deque() # queue of current explored path. ex:[["hit", "hot"], ["hit", "dot"]]
            visited = set()
            path_q.append([start])
            while path_q:
                path = path_q.popleft()
                last_node = path[-1]
                if last_node not in visited:
                    for neighbor in graph[last_node]:
                        new_path = list(path)
                        new_path.append(neighbor)
                        # print(new_path)
                        path_q.append(new_path)
                        # print(path_q)
                        if neighbor == end:
                            return new_path

                    visited.add(last_node)

            # default: assuming we can't find any path, return []
            return []
            
        shortest_path = bfs(graph, beginWord, endWord)
        return len(shortest_path)
        

# neet code的解法，他比较取巧的地方是他用pattern build the graph，在wordlist的size比较小的情况下这样会更高效率
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)

        pattern_mapper = defaultdict(list)

        # build the graph
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_mapper[pattern].append(word)
        
        q = deque([beginWord])
        visited = set((beginWord))
        res = 1

        # 分层BFS
        while q:
            # print(q)
            for _ in range(len(q)): #一开始漏掉了这行，res会在每次pop完一个词时候+1，而加上for loop，res只有在process完了整层的词的时候才会+1
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for connected_word in pattern_mapper[pattern]:
                        if connected_word not in visited: # 因为如果已经visit过，代表path在走回头路，我们不予考虑
                            visited.add(connected_word)
                            q.append(connected_word)
            res += 1

        return 0


# 11.22 复习自己完全不记得怎么build这个graph。看完怎么build graph也不记得怎么求最短路径
# T O(n) M O(n)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        
        wordList.append(beginWord)
        # build the graph
        # words under the same pattern are connected with each other
        graph = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                graph[pattern].add(word)
        
        # BFS shortest path
        q = deque([beginWord])
        visited = set([beginWord])
        res = 0

        while q:
            res += 1
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for connected in graph[pattern]:
                        if connected not in visited:
                            q.append(connected)
                            visited.add(connected)
        return 0

# 1.14 复习自己30分钟写出来了BFS分层搜索
class Solution:
    def __init__(self):
        self.graph = defaultdict(set) # key: pattern, val: set of words
        
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        res = 0
        q = []
        visited = set()

        wordList.append(beginWord)
        # build graph
        for word in wordList:
            self.checkPattern(word)

        # BFS find the shortest path
        q.append(beginWord)
        while q:
            res += 1
            new_q = []
            for _ in range(len(q)):
                w = q.pop()
                if w == endWord:
                    return res
                visited.add(w)
                for i in range(len(w)):
                    pattern = w[:i] + "*" + w[i+1:]
                    for nei in self.graph[pattern]:
                        if nei not in visited:
                            new_q.append(nei)
            q = new_q
        return 0
    
    def checkPattern(self, word:str) -> None:
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i+1:]
            self.graph[pattern].add(word)