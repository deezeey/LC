# 10.04 first try，没写过trie，直接看的neetcode

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
                cur = cur.children[c]  # <----- 自己写第一遍时候漏了这行，一直报错找了5分钟原因才找到。。。
            else:
                cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]
        return cur.end
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# 11.17 复习，自己不记得怎么写了。看了neet code重新默写了一遍
class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
                cur = cur.children[c]
            else:
                cur = cur.children[c]
        cur.end = True      

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if not c in cur.children:
                return False
            else:
                cur = cur.children[c]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if not c in cur.children:
                return False
            else:
                cur = cur.children[c]
        return True

# 1.9 复习，自己大概30多分钟修修改改写出来了。这个关于怎么合并使用hash + node的逻辑是有点绕的。
class TrieNode():
    
    def __init__(self):
        self.next = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root
        for c in word:
            cur = root.next
            if not c in cur:
                node = TrieNode()
                cur[c] = node # {a: node_a}
            root = cur[c]
        root.end = True
        
    def search(self, word: str) -> bool:
        root = self.root
        for c in word:
            cur = root.next
            if not c in cur:
                return False
            root = cur[c]
        return root.end

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for c in prefix:
            cur = root.next
            if not c in cur:
                return False
            root = cur[c]
        return True