from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# 自己没什么思路，看了neetcode讲解以后写出来了
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        node_hash = {}
        cur = head
        while cur:
            newNode = Node(cur.val)
            node_hash[cur] = newNode
            cur = cur.next
        cur = head
        while cur:
            newNode = node_hash[cur]
            newNode.next = node_hash[cur.next] if cur.next else None
            newNode.random = node_hash[cur.random] if cur.random else None
            cur = cur.next
        return node_hash[head]