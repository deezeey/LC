from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 2.19 first try 自己想的能过16/24 cases碰到[5,3,6,1,4,null,null,null,2]挂了
# 自己本来的思路是 in order是左根右。所以如果p是左，一定return根，如果p是根，一定return右，如果是右，我以为一定return右的左边最深，但是其实也可能是parent的parent
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        def getSuccessor(root, parent, isLeft):
            if not root:
                return None
            if root.val == p.val:
                if isLeft:
                    return parent
                else:
                    while root:
                        root = root.left
                    return root
            else:
                if root.val > p.val:
                    return getSuccessor(root.left, root, True)
                else:
                    return getSuccessor(root.right, root, False)
                    
        if root.val == p.val:
            return root.right
        elif root.val > p.val:
            return getSuccessor(root.left, root, True)
        else:
            return getSuccessor(root.right, root, False)

# 改了一下还是过不了[6,2,8,0,4,7,9,null,null,3,5]....原来有根并且root是根的左边的情况，也不一定是return根的，也可能return右边最左
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        def getSuccessor(root, parent, grandParent, isLeft):
            if not root:
                return None
            if root.val == p.val:
                if isLeft:
                    return parent
                elif grandParent:
                    return grandParent
                else:
                    while root:
                        root = root.left
                    return root
            else:
                if root.val > p.val:
                    return getSuccessor(root.left, root, parent, True)
                else:
                    return getSuccessor(root.right, root, parent, False)
                    
        if root.val == p.val:
            return root.right
        elif root.val > p.val:
            return getSuccessor(root.left, root, None, True)
        else:
            return getSuccessor(root.right, root, None, False)

# 正解，还是自己没理清逻辑，这个其实不用考虑什么没有root,是root的左child还是右child的情况。
# root=p了，只有两种情况，root有右和没右。有右，是右边child的左边最底,如果右child没有左child，这个左边最底是它自身。
# 没有右，是root的parent，或者是root的parent的某个parent
# 那么如果一个root <= p, 我们要往右找，左边全部包括根都可以被舍弃，所以simply root = root.right
# 如果一个root > p, 我们要往左找，这时候当前root可能是successor，先update successor为root，然后root = root.left
class Solution:
    
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        successor = None
        
        while root:
            
            if root.val <= p.val: #这个等于很关键
                root = root.right
            else:
                successor = root
                root = root.left
                
        return successor


# If p has a right leaf, we only need to traverse from p to leaf (one step right, all step left)
# Else, we only need to traverse from root to p
class Solution:
    def inorderSuccessor(root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if p.right:
            curr = p.right
            while curr.left:
                curr = curr.left
            return curr
        else:
            successor, curr = None, root
            while curr != p:
                if curr.val < p.val:
                    curr = curr.right
                else:
                    successor, curr = curr, curr.left
            return successor
        
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        # 基本上是一个iteratively create in order traversal的过程
        stack = []
        take = False
        while True:
            while root: #这个while loop先一路下到root的最左，等到下面再循环回来，这个就会是最左的right child，继续下到它的最左
                stack.append(root)
                root = root.left
            if not stack:
                return None
            root = stack.pop() #最左的rootpop出来
            if root==p: # 如果它是p， mark一下flag
                take = True
            elif take:
                return root
            root = root.right #把pop出来的这个node的right child设为root
        
        return None