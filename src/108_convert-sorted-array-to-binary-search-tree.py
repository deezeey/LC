from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 2.6 first try，还行写出来了
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildNode(s, e):
            if s == e:
                return TreeNode(nums[s])
            if s + 1 == e:
                node = TreeNode(nums[e])
                node.left = TreeNode(nums[s])
                return node
            mid = s + (e - s) // 2
            node = TreeNode(nums[mid])
            node.left = buildNode(s, mid - 1)
            node.right = buildNode(mid + 1, e)
            return node
        return buildNode(0, len(nums) - 1)

# 看了下neetcode的，改进了一下base case，照理说我应该能想到，可能是今天来例假变傻了
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildNode(s, e):
            if s > e:
                return None
            mid = s + (e - s) // 2
            node = TreeNode(nums[mid])
            node.left = buildNode(s, mid - 1)
            node.right = buildNode(mid + 1, e)
            return node
        return buildNode(0, len(nums) - 1)