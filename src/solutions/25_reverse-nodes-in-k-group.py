from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 一组一组的reverse
# 自己很容易想到算法但是这个代码真的是，太tmd难了。
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) #任何potentially要change head node的东西都适合来一个dummy head
        groupPrev = dummy

        while True: #直到最后不满足k个条件之前要一直reverse group
            kth = self.getK(groupPrev, k) # kth = 2
            if not kth:
                break
            groupNext = kth.next #先把下一个group的第一个节点存起来 groupNext = 3

            prev, cur = kth.next, groupPrev.next #因为我们知道reverse之后group第一个node的下一个得是下一个group的第一个，所以先把它存成prev。然后cur是group第一个节点 prev，cur = 3， 1
            while cur != groupNext: #从前往后reverse直到cur move到下一个group第一个node跳出reverse loop.
                tmp = cur.next # tmp = 2， tmp = 3
                cur.next = prev # 1.next = 3， 2.next = 1
                prev = cur # prev = 1, prev = 2
                cur = tmp # cur = 2, cur = 3
            tmp = groupPrev.next # tmp = dummy.next = 1
            groupPrev.next = kth # dummy.next = 2
            groupPrev = tmp # groupPrev = 1
        return dummy.next

    def getK(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur    