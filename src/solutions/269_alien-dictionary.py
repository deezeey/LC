from typing import List

# 2.2 first try, 自己的思路大概就是build图然后检测有没有环，没有环就一层层剥掉叶子节点然后从左边不停push到res deque
# 太晚了有点写不动了，直接看答案思路对不对了
class Solution:
    def __init__(self):
        self.graph = {}
        self.letters = set()
    def alienOrder(self, words: List[str]) -> str:
        for i in range(1, len(words)):
            self.connectLetters(words[i-1], words[i])

    def connectLetters(self, a:str, b:str) -> None:
        for i in range(min(len(a), len(b))):
            if a[i] == b[i]:
                continue
            self.graph[b].append[a]
            self.letters.update({a[i], b[i]})

# neetcode的写法, 自己默写还有bug，comment里写出来了
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {char:set() for word in words for char in word}
        # 注意这里一定是先for外层再for里层

        # build graph
        for i in range(1, len(words)):
            w1, w2 = words[i-1], words[i]
            min_len = min(len(w1), len(w2))
            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
                # for case like ["wrfe", "wrf"], it is invalid so return "" immediately
                return ""
            for j in range(min_len): # var重名bug，一开始用的也是i，要换成j
                if w1[j] != w2[j]: 
                        graph[w1[j]].add(w2[j])
                        break
                        # 一开始这里漏了这个break导致graph build错误！
        
        visited = {} # char:bool, False -> visited before but not in cur path, True -> in current path, so there's a loop
        res = []
        def dfs(c):
            # post order dfs, do not process cur node untill all its descendents are processed
            # post order dfs不一定要从top node开始可以从任何node开始traverse
            if c in visited:
                # if c in visited, it's either in cur path or not, either way, return bool directly
                return visited[c]
            visited[c] = True
            # add cur node to cur path
            for nei in graph[c]:
                if dfs(nei):
                    # if any nei was in cur path, we have a loop return True immediately
                    return True
            visited[c] = False
            # remove cur node from cur path
            res.append(c)
            return False
            # since we cleared all the descendents, we can now add node to res
        
        for char in graph:
            if dfs(char):
                # if we see any loop, return"" immediately
                return ""

        res.reverse()
        return "".join(res)