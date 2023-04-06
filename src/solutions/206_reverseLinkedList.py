from typing import Optional

# 9.30 first try，没解出来，还是iterative的思维，而且用stack不work因为每个node内部的next并没有被改变
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeStack = []

        while head:
            # print('node', head.val, head.next)
            nodeStack.append(head)
            head = head.next
            # print('stack', nodeStack)

        newHead = nodeStack.pop()

        for i in range(len(nodeStack)):
            print(newHead)
            print(nodeStack)
            if len(nodeStack) > 1:
                newHead.next = nodeStack.pop()
            else:
                newHead.next = None
        
        return newHead

# with input[1, 2, 3, 4, 5], print出来的东西是这样的
# ListNode{val: 5, next: None}
# [ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}, ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}, ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}, ListNode{val: 4, next: ListNode{val: 5, next: None}}]
# Error - Found cycle in the ListNode
# [Error - Found cycle in the ListNode, Error - Found cycle in the ListNode, Error - Found cycle in the ListNode]
# Error - Found cycle in the ListNode
# [Error - Found cycle in the ListNode, Error - Found cycle in the ListNode]
# Error - Found cycle in the ListNode
# [Error - Found cycle in the ListNode]


# two pointers solution, iterative T O(n) M O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev


# neet code recursive solution, T O(n) M O(n)
# 很难理解，最好自己带入 1 —-> 2 --> 3这个test case写一下recursion的过程
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: # <--- base case
            return None

        newHead = head # <--- 如果只有1个node，reverse之后的head就是当前head
        if head.next: #
            newHead = self.reverseList(head.next) # <--- keep recursion going until tail node. the tail node becomes the new head
            head.next.next = head # <---- 假设是1->2->3。recursion走到3结束。return了point to none的3作为newHead。才会第一次开始执行这行，此时head是2，head.next是3。我们设置3.next = 2。
            # 但是注意，写newHead.next = head是不work的，因为newHead永远等于3
        head.next = None # <--- 暂时把2的next设置为None
        return newHead # <---- 但是咱们还是return 3所以不管recursion回到多少层，return的都是3


# 贵贵儿的recursion
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: # if head has <= 1 elements
            return head

        head_new = head # if head has >= 2 elements
        if head.next.next: # if head = [1,2,3] or longer
            head_new = self.reverseList(head.next)
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = head
        head.next = None
        if not head_new.next:
            head_new = temp
        return head_new


# 11.03复习自己没写出来。。。看了一下答案 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev


# 11.09复习自己写，iterative的记得，recursive的还是记不得
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev

# 1.10复习自己写， recursion那个真的难写，写多少遍都记不住，只能硬背
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        newHead = head  # newHead var的设置至关重要
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head #这一行必须在if条件句里面
        head.next = None
        return newHead