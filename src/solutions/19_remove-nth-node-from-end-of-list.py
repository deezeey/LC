from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 自己规定时间内解出来的遇到一个edge case[1, 2], n = 2 过不了
# 思路是快慢指针，快针永远比慢针快n个node这样快针到底慢针刚好在要delete的node上
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # fast will always be n - 1 next node of slow
        dummy = ListNode()

        slow = fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            count = n - 1
            fast = slow
            while count:
                fast = fast.next
                count -= 1
        # detach slow and connect prev and slow.next
        print(prev, slow.val, slow.next)
        if not prev:
            return None

        temp = slow.next
        prev.next = temp
        return head

# neetcode写的很简洁，其实是一个linkedlist的滑动窗口。首先让窗口右端走到需要的长度，接下来就是左右同时前进就好了。
# 用了dummy，快慢指针从dummy和head开始
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy # 为什么left要point to dummy。因为如果【1，2】，n=2那么滑不动
        right = head

        while n > 0: #为什么不需要n - 1,因为我们想要最后left point在要删掉的node前面一个
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # delete
        left.next = left.next.next
        return dummy.next