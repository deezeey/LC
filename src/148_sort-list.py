from typing import Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2.9 first try, min heap做很intuitive但是应该不是最优解
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # going thru the linked list and store them in a min_heap, then pop and connect
        if not head:
            return None
        min_hp = [] # [val, i, node], i to prevent dupe values
        i = 0
        while head:
            min_hp.append([head.val, i, head])
            i += 1
            head = head.next
        heapq.heapify(min_hp)
        _, _, root = heapq.heappop(min_hp)
        cur = root
        while min_hp:
            cur.next = heapq.heappop(min_hp)[2]
            cur = cur.next
        cur.next = None
        return root

# 正解merge sort，参考了neetcode写的。还是有点套路的
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # merge sort
        if not head or not head.next:
            return head
        mid = self.findMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge2Sorted(left, right)
        
    def merge2Sorted(self, node1, node2):
        if not node1:
            return node2
        if not node2:
            return node1
        dummy = ListNode()
        cur = dummy
        while node1 and node2:
            if node1.val < node2.val:
                cur.next = node1
                node1 = node1.next
            else:
                cur.next = node2
                node2 = node2.next
            cur = cur.next
        if node1:
            cur.next = node1
        if node2:
            cur.next = node2
        return dummy.next

    def findMid(self, root):
        if not root or not root.next: # 这两行其实不用加因为在sortList里面已经确认过了
            return root
        prev, slow, fast = None, root, root
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return slow