from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2.7 first try碰到【1，0，1】过不了
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        if not head or not head.next:
        # 0 or 1 node, return true
            return True
        cur = head
        while cur:
            if stack and cur.val == stack[-1]:
                stack.pop()
                cur = cur.next
                continue
            stack.append(cur.val)
            cur = cur.next
        return not stack

# 看了neetcode答案。和我自己隐约想到的快慢指针找中点然后reverse差不多但是我自己写不出来
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find middle point
        fast, slow = head, head
        while fast: # 这里要改成while fast and fast.next
            slow = slow.next
            fast = fast.next.next
        # reverse 2nd half
        prev = None
        cur = slow
        while cur and cur.next: # 归根结底还是不记得怎么reverse linked list了
            temp = cur.next
            cur.next.next = cur
            cur.next = prev
            prev = cur
            cur = temp
        # check palindromic
        while cur and head: # 这里要check的不是cur而是prev，因为cur最后会停在最后一个node的next，即None
            if cur.val != head.val:
                return False
            cur = cur.next
            head = head.next
        return True

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head
        
        # find the middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # reverse second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

# 对照neetcode的答案自己找了一下bug
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find middle point
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse 2nd half
        prev = None
        cur = slow
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        # check palindromic
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True