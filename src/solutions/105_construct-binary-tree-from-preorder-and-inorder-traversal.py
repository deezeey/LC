from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 10.10 first try, 一开始自己没有主意因为不是很清楚preorder和inorder是什么
# 看了neet code讲解后自己写出来了
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildSubTree(preorder_ls, inorder_ls):
            if not preorder_ls or not inorder_ls:
                return None

            if len(preorder_ls) == len(inorder_ls) == 1:  # <--- 确实有上面的base case这个if没必要写
                root_node = TreeNode(val = preorder_ls[0], left = None, right = None)
                return root_node

            root_node = TreeNode(val = preorder_ls[0])

            for i in range(len(inorder_ls)): # <--- 这个部分用inorder.index(val)会快多了
                if inorder_ls[i] == root_node.val:
                    cut = i

            root_node.left = buildSubTree(preorder_ls[1:cut+1], inorder_ls[:cut])
            root_node.right = buildSubTree(preorder_ls[cut+1:], inorder_ls[cut+1:])

            return root_node

        return buildSubTree(preorder, inorder) # <--- 确实没有必要用个新function


# neet code写的。。。
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root
        
# 11.14复习自己写，能想出来思路但是还有一个环节没想通，这个过了test case但是submission自己知道肯定是fail的
# 后来发现是我没有理解preorder前序遍历，我自己画了个test case，把preorder写成了level order
# 比如[3 | 9, 20 | 10, 18, 15, 7 | null, null, null, null, null, 8, null, null] 这个树
# inorder是左根右，是[10, 9, 18, 3, 15, 8, 20, 7]
# preorder是根左右，应该是[3, 9, 10, 18, 20, 15, 8, 7] 但我写成了[3, 9, 20, 10, 18, 15, 7, 8]这个是level order
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def buildSubTree(root_val, inorder):
            # leaf node
            if len(inorder) == 1:
                return TreeNode(val = root_val)

        root = TreeNode(val = preorder[0])
        root_idx = inorder.index(root.val)
        # len_left, len_right = root.idx, len(inorder) - root_idx - 1
        root.left = buildSubTree(preorder[1], inorder[:root_idx]) # 我知道preorder[1]和preorder[2]不对，但是我想不通要怎样get subtree的root
        root.right = buildSubTree(preorder[2], inorder[root_idx + 1:])

        return root


# 弄明白以后自己重写的
# 节点数n，树的高度h。（极端情况h = n） 时间复杂度：O(n * h) 空间复杂度：额外栈空间 O(h) <--- 这是九章的人写的但是我不是很确定是否正确
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return

        root = TreeNode(val = preorder[0])
        root_idx = inorder.index(root.val)

        root.left = self.buildTree(preorder[1: root_idx + 1], inorder[:root_idx]) # list slicing是需要额外的memory的
        root.right = self.buildTree(preorder[root_idx + 1:], inorder[root_idx + 1:])

        return root


# 同一个思路靠记index来做可以避免slicing这样Space complexity会变成O(1), leetcode的M评分会一下从40%变成打败90%
def buildTree(self, preorder, inorder):
    return self.helper(0,0,len(inorder)-1,preorder,inorder)
    
def helper(self,pre_start,in_start,in_end,preorder,inorder):
    if pre_start>len(preorder)-1 or in_start>in_end:
        return None
    root = TreeNode(preorder[pre_start])
    in_idx = inorder.index(root.val)
    root.left = self.helper(pre_start+1,in_start,in_idx-1,preorder,inorder)
    root.right = self.helper(pre_start+in_idx-in_start+1,in_idx+1,in_end,preorder,inorder)
    return root


# 12.15 复习又跪了，记得算法但是implementation还是跪了
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 1:
            return TreeNode(val = preorder[0])

        root = TreeNode(val = preorder[0])
        root_idx = inorder.index(preorder[0])
        if len(preorder) == 2:
            if root_idx == 0:
                root.left = None
                root.right = self.buildTree(preorder[1:], inorder[root_idx+1:])
            else:
            # root_idx == len(inorder) - 1
                root.right = None
                root.left = self.buildTree(preorder[1:], inorder[:root_idx])
            return root

        root.left = None if root_idx == 0 else self.buildTree(preorder[1:], inorder[:root_idx])
        root.right = None if root_idx == len(inorder) - 1 else self.buildTree(preorder[2:], inorder[root_idx+1:])

        return root


# 1.7 复习自己写，这个没有optimize memory但是简单易懂
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(val=preorder[0])
        i = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1+i], inorder[:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return root