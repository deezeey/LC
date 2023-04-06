from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 03.08 first try
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # dummy head
        dummy = ListNode()
        dummy.next = head
        cur = dummy

        def _swapNext(root: [ListNode]) -> None:
            if root.next:
                next_1 = root.next
                next_2 = root.next.next
                root.next = next_2
                next_1.next = root
                root = next_1
            return root
        
        while cur and cur.next:
            cur.next = _swapNext(cur.next)
            cur = cur.next.next
        
        return dummy.next