class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 12.15 first try, 10分钟做出来了，ß这题好像很简单感觉比很多easy还容易？
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 1

        def checkNode(prev_max, node):
            nonlocal count
            if not node:
                return
            if node.val >= prev_max:
                count += 1
            now_max = max(prev_max, node.val)
            checkNode(now_max, node.left)
            checkNode(now_max, node.right)
        
        checkNode(root.val, root.left)
        checkNode(root.val, root.right)
        return count

# 1.6 复习自己写
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(root: TreeNode, prev_max: float) -> tuple:
            nonlocal res
            if not root:
                return
            if root.val >= prev_max:
                res += 1
            cur_max = float(max(root.val, prev_max))
            dfs(root.left, cur_max)
            dfs(root.right, cur_max)

        dfs(root, float("-inf"))

        return res