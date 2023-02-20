from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 2.6 first try自己规定时间写的解过不了[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,30,31,32]  & [30,31,32] intersect at 30的case
# 有这个解法，只不过需要O（M）memory所以不是最优解
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()
        while headA or headB:
            if headA in visited or headA == headB:  # 最后发现bug来自于漏掉了non null判断
            # if headA and headA in visited or headA == headB:
                return headA
            if headB in visited:
            # if headB and headB in visited:
                return headB
            visited.update({headA, headB})
            headA = headA.next if headA else None
            headB = headB.next if headB else None
        return None

# neetcode写法，最优解是iterate每个list2遍。
# 假设A长8，B长3. 从A开始走到尽头接上B，从B开始走到尽头接上A。第一次两者当前node相同，就是intersection。如果不相交，intersection会是null
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1