from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 有正确的思路，即bottoms up并计算height，但无法自己用recursion代码实现，下面是九章的写法
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
        def checkNode(root: Optional[TreeNode]) -> tuple[bool, int]:
            if not root:
                return True, 0
            
            leftBalanced, leftHeight = checkNode(root.left)
            if not leftBalanced:
                return False, 0
            
            rightBalanced, rightHeight = checkNode(root.right)
            if not rightBalanced:
                return False, 0
            
            return abs(rightHeight - leftHeight) <= 1, max(leftHeight, rightHeight) + 1
        
        balanced, _ = checkNode(root)
        return balanced

# neet code写法
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            # 这题要想清楚以上判断条件非常重要，root是否balanced，不仅仅取决于左右最高高度是否相差小于1
            # 还要看左右是否自身是balanced
            # 比如[1,2,2,3,null,null,3,4,null,null,4]这个tree。root的左右max高度一样，但是left子树和right子树自身不是balanced
            # 你仔细想想应该也能得出画出一个左右子树都是balanced但是左右高度差很多的树
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
        

# 另外一个iterative的解法，但感觉有点难以理解loop执行的顺序
class Solution(object):
    def isBalanced(self, root):
        stack, node, last, depths = [], root, None, {}
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right  = depths.get(node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1: return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True


# 11.12 复习自己写，跑不过[1,2,2,3,null,null,3,4,null,null,4]的case
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def getMaxHeight(root):
            if not root:
                return 0
            leftHeight = 1 + getMaxHeight(root.left)
            rightHeight = 1 + getMaxHeight(root.right)
            return max(leftHeight, rightHeight)

        return abs(getMaxHeight(root.left) - getMaxHeight(root.right)) <= 1


# 默写neet code的dfs方法，这个错的很经典
# 和所有需要遍历树的递归solution一样 T O(n) M O(n)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def getMaxHeight(root):
            if not root:
                return [0, True]
            left, right = getMaxHeight(root.left), getMaxHeight(root.right)
            return [1 + max(left[0], right[0]), abs(left[0] - right[0]) <= 1]
            # 错就错在判断当前root是否balanced不仅仅是看左右max height相差是否<=1，还要看左右是否都是balanced

        return getMaxHeight(root)[0]


# 12.15 复习自己写
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # left is balanced,
        # right is balanced,
        # height of left & right diff by 1 at most
        # helper function to return if a node is balanced and height
        def balancedNodeHeight(root):
            if not root:
                return (0, True)
            left, right = balancedNodeHeight(root.left), balancedNodeHeight(root.right)
            return (max(left[0], right[0]) + 1, left[1] and right[1] and abs(left[0] - right[0]) <= 1)
        
        return balancedNodeHeight(root)[1]

# 1.7 复习自己写
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # abs(h_left - h_right) <= 1 and l is balanced, r is balanced
        def dfs(root: Optional[TreeNode]) -> tuple[int, bool]:
            if not root:
                return 0, True
            l_h, l_b = dfs(root.left)
            r_h, r_b = dfs(root.right)
            return max(l_h, r_h) + 1, abs(l_h - r_h) <= 1 and l_b and r_b
        _, res = dfs(root)
        return res