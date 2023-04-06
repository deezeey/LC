from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 10.02 first try, 很简单的recursion
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        while root: # <--- 看neetcode写法确实从while到else都没必要写
            if not root.left and not root.right:
                return 1
            else:
                return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# 下面是neet code的三种解法
# RECURSIVE DFS, 这是从下往上搜
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# ITERATIVE DFS，这是从上往下搜
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop() # 注意这里是pop而不是popleft所以它才是DFS而不是BFS
            # 第二层先pop root的right child，然后就把right child的两个孩子加进去，第三层也是pop的rightmost child
            # 这样走最右边的路一路下去到leaf node，不满足if node:条件，不再往stack里加东西，开始pop最底层最右边子树的left child

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1]) #最终到达leaf node以后会append[None, this leaf node's height + 1]
                stack.append([node.right, depth + 1])
        return res


# BFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        q = deque()
        if root:
            q.append(root)

        level = 0

        while q:

            for i in range(len(q)): # <--- 这是遍历整层的办法
                node = q.popleft() # popleft就是bfs
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level


# 11.12 复习自己写 TM O(n)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1