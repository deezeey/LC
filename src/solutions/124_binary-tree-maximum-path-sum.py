from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 12.15 first try 自己在45min内写出来了！
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int: 
        # non empty path has at least 2 nodes
        # each node has a 1 side max & w side max
        # 1 side max = max(left.1sidemax, right.1sidemax) + self.val
        # 2 side max = left.1sidemax + right.1sidemax + self.val
        res = float("-inf")

        def getMax(root):
            nonlocal res
            if not root:
                return 0
            l_max, r_max = getMax(root.left), getMax(root.right)
            one_side_max = max(l_max, r_max) + root.val
            both_side_max = l_max + r_max + root.val
            # in case children are only making things worse
            one_side_max = max(root.val, one_side_max)
            both_side_max = max(root.val, both_side_max)
            res = max(res, one_side_max, both_side_max)
            return one_side_max

        getMax(root)
        return res

# neetcode 写的更简单
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = [root.val]

        # return max path sum without split
        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute max path sum WITH split
            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]

# 1.7 复习自己写还记得
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal res
            if not root:
                return 0
            l_max = dfs(root.left)
            r_max = dfs(root.right)
            sub_max = max(l_max, r_max)
            cur_max = max(sub_max + root.val, root.val)
            res = max(res, cur_max, l_max + r_max + root.val)
            return cur_max
        
        dfs(root)
        return res