from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 2.8 first try
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        deq, res = deque([root]), []
        reverse = False

        while deq:
            new_deq, cur_lvl = [], []
            for _ in range(len(deq)):
                if reverse:
                    cur = deq.pop()
                    if not cur:
                        continue
                    new_deq.extend([cur.right, cur.left])
                else:
                    cur = deq.popleft()
                    if not cur:
                        continue
                    new_deq.extend([cur.left, cur.right])
                cur_lvl.append(cur.val)
            if reverse:
                new_deq = reversed(new_deq)
            if cur_lvl:
                res.append(cur_lvl)
            deq.extend(new_deq)
            reverse = not reverse
        return res