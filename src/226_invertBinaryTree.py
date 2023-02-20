
# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    
    #swapping children
    temp = root.left
    root.left = root.right
    root.right = temp
    
    self.invertTree(root.left)
    self.invertTree(root.right)
    
    return root

# 9.25 复习自己写，不熟悉binary tree的写法，没有想好怎么handle leaf nodes, infinite while loop，运行exceeded time limit：
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    while root: # <---把while换成if，就work了。因为while loop内部没有increase root的value，外层的while loop会runs forever，不会走到return那一行
        temp = root.right
        root.right = root.left
        root.left = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
    return root

# 11.11 复习自己写。想了五分钟把recursion写出来了
#  T O(n), n是node数量，因为每个node都要被visit一次
#  M O(n) Because of recursion, O(h) (height) function calls will be placed on the stack in the worst case
# Because h ∈ O(n), 这个念做h is a certain O(n). h is an element of O(n)的意思. the space complexity is O(n)
class Solution:
    def invertTree(self, a: Optional[TreeNode]) -> Optional[TreeNode]:
        if not a:
            return
        a.left, a.right = self.invertTree(a.right), self.invertTree(a.left)
        return a


# iterative的方法是用queue。类似BFS
# T O(n)也是因为要visit every node
# M O(n)因为q里面最长需要存n/2 nodes (full binary tree的情况），which = n。
class Solution:
    def invertTree(self, a: Optional[TreeNode]) -> Optional[TreeNode]:
        if not a:
            return
        
        q = deque([a])

        while q:
            cur = q.popleft()
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            
        return a

# 12.15 复习自己写
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root