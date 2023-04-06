from typing import Optional
from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# 2.8 first try, 自己写的BFS不是最高效的因为要用extra memory
class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return
        q = [root]
        while q:
            new_q = []
            for i in range(len(q)-1, -1, -1):
                node = q[i]
                if not node:
                    continue
                if i == len(q) - 1:
                    node.next = None
                else:
                    node.next = q[i + 1]
                new_q.extend([node.right, node.left])
            q = new_q[::-1]
        return root

# 官方的level order travesal
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        Q = deque([root])
        while Q:
            size = len(Q)
            for i in range(size):
                node = Q.popleft()
                # root他直接没有处理，因为默认next是None. 然后实际上是从第二层开始的 
                # 第二层，q会是【2，3】size = 2, i = 0，2被pop出来成为node，i = 0 < 2 - 1, 2.next = 3; 然后 i=1, 3被pop出来，i=1 >= 2-1不满足条件，所以不设置next，leave it as null
                if i < size - 1: # 当 i == size - 1时候说明是这一层最后一个node，就不用设置next。当 i < size - 1说明是这一层前面的node，直接point to 它的next node，which should be Q[0]，因为当前node已经被popleft出来了
                    node.next = Q[0] 
                # Add the children, if any, to the back of
                # the queue
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        
        # Since the tree has now been modified, return the root node
        return root

# neetcode写的 M O(1)的DFS
class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        cur, nxt = root, root.left if root else None
        while cur and nxt:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
            cur = cur.next
            if not cur:
                cur = nxt
                nxt = cur.left
        return root

# 我重写一遍过不了，bug找了好久
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        cur, nxt = root, root.left if root else None
        while cur and nxt:
            cur.left.next = cur.right
            cur.right.next = cur.next.left if cur.next else None
            cur = cur.next if cur.next else nxt 
            nxt = cur.left if cur.left else None # 问题就出在这一行，如果上面那行执行的是 cur = cur.next的话，我们其实不需要挪动nxt指针的
        return root
        
# 改成这样可以了
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        cur, nxt = root, root.left if root else None
        while cur and nxt:
            cur.left.next = cur.right
            cur.right.next = cur.next.left if cur.next else None
            cur = cur.next
            if not cur:
                cur = nxt
                nxt = cur.left if cur.left else None
        return root