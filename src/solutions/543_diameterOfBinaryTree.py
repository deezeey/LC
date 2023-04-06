from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 10.02 first try，一开始自己是没有思路的，看了neet code的讲解部分自己的代码实现
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def checkNode(node: Optional[TreeNode]) -> tuple[int, int]:
            nonlocal maxDiameter
            # returns (diameter, height)
            if not node:
                return (0, -1)
            leftChild = checkNode(node.left)
            rightChild = checkNode(node.right)
            height = max(leftChild[1], rightChild[1]) + 1
            # diameter passing a node = height of left child + height of right child + 2
            diameter = leftChild[1] + rightChild[1] + 2
            if diameter > maxDiameter:
                maxDiameter = diameter
            return(diameter, height)

        maxDiameter = 0
        checkNode(root)

        return maxDiameter


# 同样思路， neetcode的代码更简洁，
# 确实因为我们recursion中其实只会用到上一个recursion的height，所以没必要return diameter，diameter在过程中和max diameter比较一下就可以了
# 和所有recursion遍历树的solution一样 T O(n) M O(n)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0 # <--- 这个写法 leaf node的height会是1而不是0，这样方便算某个node的diameter，因为diameter = left height + right height
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right) # <--- 如果left height + right height > cur max diameter, 则重新赋值

            return 1 + max(left, right) # <--- recursive function return的是此node的height

        dfs(root)
        return res
        

# 11.12 复习自己写，倒是跑过了99个case但是不知为何TLE，明明和neetcode写的一模一样
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(root):
            nonlocal res
            if not root:
                return -1
            left_height, right_height = dfs(root.left), dfs(root.right)
            res = max(dfs(root.left) + dfs(root.right) + 2, res) # <---找到问题了，这里有call了2个recursion，没必要
            # 写成res = max(left_height + right_height + 2, res)就能过
            return max(left_height, right_height) + 1
        
        dfs(root)
        return res