from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# n = len(list1) + len(list2) T: O(n) M: O(1) if res is not counted as extra memory
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
        
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
        
    return dummy.next #dummy.next才是我们while loop里面append上去的第一个tail node，即真正的linked list head


# 9.25 复习自己写，不熟悉linked list在python里的implementation，错得离谱
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    node1 = list1
    node2 = list2
    if node1.val > node2.val:
        dummy.next = node2
        node2 = node2.next
    else:
        dummy.next = node1
        node1 = node1.next
    return dummy.next

n3 = ListNode(val=4, next=None)
n2 = ListNode(val=2, next=n3)
n1 = ListNode(val=1, next=n2)
n6 = ListNode(val=4, next=None)
n5 = ListNode(val=3, next=n6)
n4 = ListNode(val=1, next=n5)

print(mergeTwoLists(n1, n4).val)


# 11.09 复习自己写，总是AttributeError: 'NoneType' object has no attribute 'next' at cur.next = list2
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy.next  # <--- 这里应该是cur = dummy，自己脑子没想清楚

        while list1 and list2:
            if not cur: # <--- 这里也是典型的脑子没想清楚，根本没必要
                if list1.val < list2.val:
                    temp = list1
                    list1 = list1.next
                else:
                    temp = list2
                    list2 = list2.next
                cur = temp
            else:
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
        
        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2

        return dummy.next

# 1.10 复习自己写
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
            
        return dummy.next