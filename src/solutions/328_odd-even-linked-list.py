from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2.21 first try 自己30min内写的
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        odd_dummy, even_dummy = ListNode(), ListNode
        odd_cur, even_cur = odd_dummy, even_dummy
        odd_cur.next = head
        odd_cur = odd_cur.next
        while odd_cur and odd_cur.next:
            even_cur.next = odd_cur.next
            even_cur = even_cur.next
            if odd_cur.next.next:
                odd_cur.next = odd_cur.next.next
                odd_cur = odd_cur.next
            else:
                odd_cur.next = None
            
        even_cur.next = None
        odd_cur.next = even_dummy.next
        return odd_dummy.next
    
# 别人写的更简洁
class Solution:
    def oddEvenList(self, head):
        if head is None : return None
            
        odd = head
        dum = evn = head.next
        
        while evn and evn.next:
            odd.next = odd.next.next
            evn.next = evn.next.next
            odd = odd.next
            evn = evn.next
            
        odd.next = dum

        return head