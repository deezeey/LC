from collections import deque
# 1.25 first try自己感觉handle search . 应该用level order BFS
# 但是这个跑出来不对
class Node:
    def __init__(self, val=None):
        self.end = False
        self.children = {}
        self.val = val

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node(c)
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        cur_level = deque()
        cur_level.append(self.root)
        for c in word:
            if c == ".":
            # search all children
                for _ in range(len(cur_level)):
                    cur = cur_level.popleft()
                    cur_level.extend(cur.children.values())
            else:
                for _ in range(len(cur_level)):
                    cur = cur_level.popleft()
                    if c in cur.children:
                        # not a "." and c does exist
                        cur_level.append(cur.children[c])
            # not a "." and c does not exist
                if not cur_level:
                    return False

        return True if cur.end == True else False


# neetcode用backtracking DFS handle .
# 这个代码一开始会TLE,需要在class里保持一个最大word length记录
# 然后只要search的word长度超出最大记录直接return False
class Node:
    def __init__(self):
        self.end = False
        self.children = {}
        # self.max_word_length = 0  # 把 max_word_length的这几行加上就能避免TLE

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.end = True
        # self.max_word_length = max(self.max_word_length, len(word))

# 这个recursion有点难写的因为根据if else分别走recursive和iterative的路线
    def search(self, word: str) -> bool:
        # if len(word) > self.max_word_length:
        #     return False
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values(): # 这个for自己完成了backtracking，因为一条路通了会立马return True，如果不通会执行下一个for loop即走另一条路
                        if dfs(i + 1, child):
                            return True
                    return False #如果for loop结束代表所有路都不通，就return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.end
        return dfs(0, self.root)