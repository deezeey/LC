from collections import deque
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

# 10.03 first try 直觉感觉是bfs但是没什么写bfs经验所以直接看答案，看了讲解以后自己没看代码几乎写出来了, 自己想到了for in while loop
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        res = []

        while queue:
            cur_level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur:
                    cur_level.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
            if cur_level:
                res.append(cur_level)
        
        return res

# 11.13 复习自己写
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        
        q = deque([root])
        res = []
        while q:
            cur_level = []
            for _ in range(len(q)):
                cur_node = q.popleft()
                cur_level.append(cur_node.val)
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            res.append(cur_level)

        return res   