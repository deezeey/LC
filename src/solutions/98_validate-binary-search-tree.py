from typing import Optional
# 10.05 first try 自己写的碰到了【5， 4， 6， null， null， 3， 7】的case报错了，没有正确理解BST的概念

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 这个不能保证右边子树的所有node都大于root node val
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if root.left or root.right:
            if root.left and root.left.val >= root.val or root.right and root.right.val <= root.val:
                return False
            else:
                return self.isValidBST(root.left) and self.isValidBST(root.right)
            
        return True


# neetcode解法 O(n)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validateNode(node: Optional[TreeNode], min_val, max_val):
            if not node:
                return True
            if node.val >= max_val or node.val <= min_val:
                return False
            return validateNode(node.left, min_val, node.val) and validateNode(node.right, node.val, max_val)
        
        return validateNode(root, float("-inf"), float("inf")) # <---- python get 最大最小数的方式


# 11.13复习自己写. 思路倒是和neet code大概一致，但是我是bottom up。他是top down
# 于是写的更复杂，并且因为return了3个东西所以大于最小的小于最大的放在哪里弄了半天
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # left and right are both validBST and
        # min of right sub tree needs to be greater than root.val
        # max of left sub tree needs to be smaller than root.val
        if not root:
            return True

        def dfs(root):
            if not root:
                return True, float("inf"), float("-inf") # self valid, cur_min, cur_max
            
            left, right = dfs(root.left), dfs(root.right)
            isValid = left[0] and right[0] and left[2] < root.val and right[1] > root.val
            cur_max = right[2] if right[2] != float("-inf") else root.val
            cur_min = left[1] if left[1] != float("inf") else root.val

            return isValid, cur_min, cur_max
        
        return dfs(root)[0]