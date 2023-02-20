from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 2.6 first try想到了思路但是没写出来因为不确定这个mirror的逻辑是否正确
# 还有就是来例假可能今天有点儿笨
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isMirror(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val == b.val and isMirror(a.left, b.right) and isMirror(a.right, b.left):
                return True
            return False
            
        return isMirror(root.left, root.right)
