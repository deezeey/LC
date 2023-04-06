from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1.11 first try自己鼓捣了一个小时终于能过testcase但是在11/12 TLE了
# 自己的想法是，存1，把2 mark成newhead，走到尾巴，存5，把4point到none，这样4就是new tail。然后取出newHead 2，重新开始这个走到尾巴的过程。
# 现在想想肯定是要TLE的毕竟要不断的traverse entire list
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy = ListNode()
        cur = dummy

        def traverseList(head):
            nonlocal cur
            cur.next = head
            cur = cur.next
            if not head.next:
                return
            newHead = head.next
            while head.next.next:
                head = head.next
            cur.next = head.next
            head.next = None
            if cur.next:
                cur = cur.next
            traverseList(newHead)
        
        traverseList(head)

        return dummy.next

# 看了neetcode解释自己尝试实现，明明一开始想到了快慢指针的，没想到可以reverse 2nd half。自己写的这个有bug，stackoverflow了
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # use fast/slow pointer to break the lists into 2 halfs
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None
        # reverse the 2nd half  #最后debug出来这个部分产生了stackoverflow
        prev = None
        while right.next:
            temp = right.next
            temp.next = right
            right.next = prev
            right = temp
        # traverse 2 lists and merge together
        cur_l, cur_r = head, right # cur_r不能是right，得是prev
        while cur_l and cur_r:
            temp_l, temp_r = cur_l.next, cur_r.next
            cur_l.next = cur_r
            cur_r.next = temp_l
            cur_l, cur_r = temp_l, temp_r

# 改一下代码过了
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # use fast/slow pointer to break the lists into 2 halfs
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None
        # reverse the 2nd half
        prev = None
        while right:
            temp = right.next
            right.next = prev
            prev = right
            right = temp
        # traverse 2 lists and merge together
        cur_l, cur_r = head, prev
        while cur_l and cur_r:
            temp_l, temp_r = cur_l.next, cur_r.next
            cur_l.next = cur_r
            cur_r.next = temp_l
            cur_l, cur_r = temp_l, temp_r
