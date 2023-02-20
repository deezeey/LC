
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# 10.03 first try, 自己连题都没看懂。。。看了neet code，不是100%理解他的recursion但是自己尝试重新默写一下，一开始漏了一行就infinite recursion了
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        copied = {}

        if not node:
            return None

        def clone(node):
            if node in copied:
                return copied[node]
            copy = Node(node.val)
            copied[node] = copy # <----- 一开始就是漏了这行，就infinite loop了
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy
        
        return clone(node)

# 11.20 复习自己写。虽然心里发慌但竟然自己一次性写出来了，T O(n) M O(n)
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        visited = {}

        def cloneNode(node):
            if node.val in visited:
                return visited[node.val]

            clone = Node(val = node.val)
            visited[node.val] = clone

            if node.neighbors:
                for neighbor in node.neighbors:
                    neighbor_copy = cloneNode(neighbor)
                    clone.neighbors.append(neighbor_copy)
            
            return clone
        
        return cloneNode(node)

# 1.13 复习自己十几分钟写出来了，用的138 copy linked list with random pointer的办法
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        node_hash = {}
        def cloneNode(node):
            if node in node_hash:
                return
            new_node = Node(val=node.val)
            node_hash[node] = new_node
            for neighbor in node.neighbors:
                cloneNode(neighbor)
        cloneNode(node)
        for old_node in node_hash:
            new_node = node_hash[old_node]
            for neighbor in old_node.neighbors:
                new_node.neighbors.append(node_hash[neighbor])

        return node_hash[node]