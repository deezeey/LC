# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # setting cur node val to be next.val
        # delete last node
        while node.next:
            node.val = node.next.val
            if not node.next.next:
                node.next = None
            else:
                node = node.next

# 其实break，reconnect就行了不用while一直替换
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # setting cur node val to be next.val
        # delete last node
        node.val = node.next.val
        node.next = node.next.next