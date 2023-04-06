from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 12.15 first try 在25分钟内写出来了但是也是修修改改写出来的
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root_a, root_b):
            if not root_a and not root_b:
                return True
            if not root_a or not root_b:
                return False
            return root_a.val == root_b.val and isSameTree(root_a.left, root_b.left) and isSameTree(root_a.right, root_b.right)

        if not root and not subRoot:
            return True
        if not root:
            return False
        
        if isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


# neetcode写法，思路完全相同都需要same tree helper func但是他的逻辑写的更简洁
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        if not s:
            return False

        if self.sameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        return False


# 1.6 复习，这个过不了
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if not a and not b:
                return True
            if a and b and a.val == b.val:
                return isSameTree(a.left, b.left) and isSameTree(a.right, b.right)
            else:
                return False

        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        # 把上面那句改成下面这样就能过啦。
        # if not subRoot:
        #     return True
        # if not root:
        #     return False
        # return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if not a and not b:
                return True
            if a and b and a.val == b.val:
                return isSameTree(a.left, b.left) and isSameTree(a.right, b.right)
            return False

        if not subRoot:
            return True
        if not root:
            return False

        if isSameTree(root, subRoot):
            return True
        return isSameTree(root.left, subRoot) or isSameTree(root.right, subRoot) # 后来改了一下这里用错了func还是过不了，找了好久bug
        