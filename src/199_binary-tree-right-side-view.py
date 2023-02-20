from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 10.10 first try test case跑过了但是submission failed at [1,2,3,4]
# 忽略了如果right child下面没有东西，那么需要看left child这个点
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # rightmost nodes from top to bottom
        res = []

        def nextNode(node):
            while node:
                res.append(node.val)
                if node.right:
                    node = node.right
                else:
                    node = node.left
        
        nextNode(root)

        return res


# 10.10 2nd try with BFS, 跑过了
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque()
        res = []

        q.append(root)
        while q:
            res.append(q[-1].val)
            new_q = deque()
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q

        return res

# neet code的代码，他的优点在于没有用new_q而是靠一个被不断重写的var rightSide来记录要append的东西
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        q = deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res


# 10.10 贵贵儿的recursion, 每个node的结果都等于node value本身加上right tree以及left tree比right长的部分
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        right_res = self.rightSideView(root.right)
        left_res = self.rightSideView(root.left)
        if len(right_res) < len(left_res):
            return [root.val] + right_res + left_res[len(right_res) : len(left_res)]
        else:
            return [root.val] + right_res


# 11.14 复习自己写 T O(n) M O(n)
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return

        res = []
        q = deque([root])
        # storing all the node at current level to the q and push last one into res
        while q:
            res.append(q[-1].val)
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        
        return res