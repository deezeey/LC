
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 9.26自己尝试解，思路完全正确但是代码实现有问题
# 还是不太会写recursion，除了p, q在最外层就满足条件可以return，要drill down多几层就总是return null
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if p.val == root.val or q.val == root.val:
            print('equal', root.val)
            return root
        if p.val < root.val < q.val or q.val < root.val < p.val:
            print('split', root.val)
            return root
        if p.val < root.val and q.val < root.val:
            self.lowestCommonAncestor(root.left, p, q) # <--- 其实只要在这一行加上return，就可以pass
        else:
            self.lowestCommonAncestor(root.right, p, q) # <--- 其实只要在这一行加上return，就可以pass


# recursion的更优写法
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root


# 也可以iterative，用while loop, 时空复杂度比recursion跑出来好很多
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if cur.val > p.val and cur.val > q.val:
                cur = cur.left
            elif cur.val < p.val and cur.val < q.val:
                cur = cur.right
            else:
                return cur


# 11.11 复习自己写, 能pass但是这个if条件判断句属实没有必要
# T O(n)最坏情况（BST退化成链表，而pq在链表最深处）需要访问all the nodes
# M O(n)最坏情况递归栈开辟的额外空间等于树的高度
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (p.val == root.val or 
            q.val == root.val or 
            p.val < root.val and q.val > root.val or 
            q.val < root.val and p.val > root.val):
            return root
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)


# 12.15 复习自己写
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)