from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 3.8 first try自己还记得Floyd's Cycle Detection Algo
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use slow & fast pointers to check if there's a cycle
        if not head or not head.next:
            return
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not slow == fast:
            return
        # add another slow at the begining to find where the cycle begins
        slow2 = head
        while slow != slow2:
            slow = slow.next
            slow2 = slow2.next
        return slow