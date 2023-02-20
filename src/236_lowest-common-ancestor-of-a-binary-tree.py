# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 10.06 first try, my brute force way. 计算并记录每个node的path，然后找p和q的path的latest cross point
# TM complexity很不理想
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # [(3), 5] [(3), 5, 2, 4] path for 5 and 4
        # [(3), 5, 6] [(3), 1, 8] path for 6 and 8
        # [3, (5), 6] [3, (5), 2, 4] path for 6 and 4
        path = {}
        def findPath(node, prev_node):
            if not node:
                return
            if not prev_node:
                path[node.val] = [node]
            else:
                path[node.val] = path[prev_node.val] + [node]  # <--- 一开始用的是path[node.val] = path[prev_node.val].append(node), 一直key error，因为我忘了append是mutate原本的array itself
            findPath(node.left, node)
            findPath(node.right, node)
        
        findPath(root, None)

        cross_point = root

        for i in range(min(len(path[p.val]), len(path[q.val]))):
            if path[p.val][i] == path[q.val][i]:
                cross_point = path[p.val][i]

        return cross_point


# 一个非常好的解，T: O(n) M: O(1) if not counting recursive stack frames b/c we're not storing anything, otherwise O(n)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:  # <--- 如果p和q分别在root的两边，那么lca一定是root
            return root
        else:  # <--- 如果有一边的subtree没有找到p也没找到q那么那边会return none。那么lca就是另一边subtree里，p/q之间，被先找到的那个
            return l or r


# 11.14 复习自己写，30分钟写出来了上面最好的那个解。但是代码可以被优化
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        if p.val == root.val or q.val == root.val: #不需比较val，直接比较node
            return root
        else:
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)
            if set([left, right]) == set([p, q]):  #这个判断句可以被简化为if left and right
                return root
            elif left or right: #这个可以被简化为else
                return left or right
            else:
                return
