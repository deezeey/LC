from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 10.18 first try 好久没写tree的题目自己没什么思路跟着neet code写了一下
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        while cur or stack:
            while cur: # <-- 这个while loop会在left most leaf node结束
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right


# 11.14复习自己写，30min写出来了。写的过程中，recursion思路在不断修正。
# 我觉得neet code写的更简单但是他的stack更消耗memory因为是bottom down的一路push进去
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if k == 1 and not root.left and not root.right:
            return root.val
        # dfs inorder traversal
        res = []

        def dfs(root):
            if not root.left and not root.right:
                res.append(root.val)
                return
            if root.left:
                dfs(root.left)
            res.append(root.val)
            if root.right:
                dfs(root.right)
            if len(res) >= k:
                return res[k-1]
        
        return dfs(root)