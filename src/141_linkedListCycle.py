from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# first try自己的解，时间好像不太理想
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        visited = []
        while head:
            if head.next not in visited:
                visited.append(head.next)
                head = head.next
            else:
                return True


# neetcode更优解，龟兔赛跑算法。快指针每次走两步，慢指针一次走一步。 在慢指针进入环之后，快慢指针之间的距离每次缩小1，所以最终能相遇
# T O(n)当链表中不存在环时，快指针将先于慢指针到达链表尾部，链表中每个节点至多被访问两次。
# 当链表中存在环时，每一轮移动后，快慢指针的距离将减小一。而初始距离为环的长度，因此至多移动 n 轮。
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        
        while fast and fast.next: # 只要fast不是none，slow必定不是none。fast.next不能是none，fast.next.next可以是none，因为在下一个循环里它会被evaluate成fast = None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False


# 11.09 复习，自己写不出快慢指针
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head.next:
            slow = head.next
            fast = head.next.next # <--- 错就错在两根针都挂在head var上，这样两个循环没有自成体系就不能保证一定相遇
            if slow == fast:
                return True
            head = slow

        return False

# 1.10 复习自己写。写出来了但是其实脑子里关于check none的逻辑不清晰，试了好多次才pass
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while True:
            if not slow or not fast or not slow.next or not fast.next: # <---这行自己一开始没有搞清楚逻辑，试了好几遍试出来的
                return False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        