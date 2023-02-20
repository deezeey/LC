from typing import Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1.11 first try做出来了但应该不至于这么简单
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getNum(node):
            pos = 0
            res = 0
            while node:
                cur = node.val * (10 ** pos) if pos > 0 else node.val
                res += cur
                pos += 1
                node = node.next
            return res
        
        n1, n2 = getNum(l1), getNum(l2)
        total = n1 + n2
        dummy = ListNode()
        tail = dummy
        for c in str(total)[::-1]:
            node = ListNode(int(c))
            tail.next = node
            tail = tail.next
        return dummy.next

# 正解就是一对一对nodes加起来
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            node = ListNode(val)
            cur.next = node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next
        
        return dummy.next