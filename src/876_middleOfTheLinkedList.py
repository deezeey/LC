from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 10.02 first try, 快慢双指针
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        if not head.next.next:
            return head.next
        
        slow, fast = head.next, head.next.next
        while slow and fast:
            if not fast.next:
                return slow
            if not fast.next.next:
                return slow.next
            slow = slow.next
            fast = fast.next.next


# 九章快慢双指针的写法， 确实没有必要像我写的那么复杂 T O(n) M O(1)
class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next # 只要有fast.next, fast.next.next可以是None，此时slow的指针也move了一位，就不用判断要return slow.next还是slow了
        return slow


# 11.09 复习还是自己写的很复杂
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        if not head.next.next:
            return head.next
        
        slow, fast = head, head
        
        while fast.next:
            if not fast.next.next:
                return slow.next
            else:
                slow = slow.next
                fast = fast.next.next

        return slow

# 1.10 复习自己写了简单的快慢指针
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while True:
            if not fast or not fast.next:
                return slow
            slow = slow.next
            fast = fast.next.next