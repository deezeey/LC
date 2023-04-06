from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 3.8 first try
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # if cur.left & right, push right to stack, cur.right = cur.left, cur = cur.right
        # if no left & no right, pop from stack, cur.right = popped, cur = cur.right
        # if only left or only right, cur.right = cur.left/right, cur = cur.right
        if not root or (not root.left and not root.right):
            return root
        stack = []
        cur = root
        while cur:
            if cur.left and cur.right:
                stack.append(cur.right)
                cur.right = cur.left
            elif not cur.left and not cur.right and stack:
                cur.right = stack.pop()
            elif cur.left:
                cur.right = cur.left
            else:
                pass
            cur.left = None
            cur = cur.right

# T O(n) M O(1)的解法。如果有left child，把当前的right child append到left child的rightmost child就好了
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        cur = root
        while cur:
            if cur.left:
                rightmost = cur.left
                while rightmost.right:
                    rightmost = rightmost.right
                rightmost.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right