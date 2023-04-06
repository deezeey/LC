from typing import Optional, List
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 10.20 first try 自己没什么思路，想到了用heap但是没想到具体怎么写
# 这个是默写的九章的解法
# 先把所有first node弄成一个min heap。然后while heap，pop root， append到tail，如果tail有next，就把tail.next push到heap，再重复pop heap root check next的过程
# heapsort 时间复杂度：nlgn（建堆复杂度n但是排序是nlgn）空间复杂度：n
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        heap = []

        for i, node in enumerate(lists):
            if not node:
                continue
            heapq.heappush(heap, (node.val, i, node))
            # 这里把index放进tuple里非常聪明
            # 因为tuple比较的时候，如果（node1.val, node1）和（node2.val,node2）同时存在，heap在计算最小 值的时候需要比较，如果node1.val和node2.val一样，那么node1和node2就需要比较，但这两个Listnode不支持比较。

        while heap:
            _, i, node = heapq.heappop(heap)
            tail.next = node
            tail = node
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next


# mergesort 时间复杂度：nlgk 空间复杂度：1，merge sort应该才是这题真正要考察的东西. 

# 注意正常 mergesort array的话空间复杂度是 O(n)但是merge sort linked list的话空间复杂度是 O(1)
# Unlike an array, in the linked list, we can insert items in the middle in O(1) extra space and O(1) time. 因为我们只是move指针
# Therefore, the merge operation of merge sort can be implemented without extra space for linked lists.
# 但是quick sort就不适合linked list。因为quick sort需要大量的random access。比如长度为6的array，access i=3的元素。
# array因为element在memory里是contiguous的，所以我们可以quickly access random element by computing index位置
# 可linked list东西都是散在memory里我们必须iterate thru all the nodes till we get the point。
# linked list就是easy to insert，but hard to access，所以更适合merge sort

# merge sort的时间复杂度分析如下：
# A merge sort consists of several passes over the input. 
# The first pass merges segments of size 1, the second merges segments of size 2, and the i_{th}  pass merges segments of size 2i-1. 
# Thus, the total number of passes is [log2n]. 
# As merge showed, we can merge two sorted segments in linear time, which means that each pass takes O(n) time. 
# Since there are [log2n] passes, the total computing time is O(nlogn).
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge_two_list(left, right): # merge2list不是recursive func
            dummy = ListNode()
            tail = dummy

            while left and right:
                if left.val < right.val:
                    tail.next = left
                    tail = left
                    left = left.next
                else:
                    tail.next = right
                    tail = right
                    right = right.next
            
            if left:
                tail.next = left
            
            if right:
                tail.next = right

            return dummy.next
            
        if not lists:
            return None
        if len(lists) == 1: # mergeKList的base case， mergeklist是recursive func
            return lists[0]
        
        mid = len(lists) // 2   # <-- 好好背一下这个部分merge sort的代码执行，自己写还用while loop
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return merge_two_list(left, right)


# 11.10 复习自己写
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # base case
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        # merge sort func
        def merge2(list1, list2):
            head = ListNode()
            cur = head
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
            return head.next

        while len(lists) >= 2: # <--- 自己不记得merge sort的写法了居然写了个while loop，虽然也能过但是还是不太常规
            list1 = lists.pop()
            list2 = lists.pop()
            lists += [merge2(list1, list2)]

        return lists[0]


# 11.09 看了min heap的解法自己又默了一遍min heap
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, node in enumerate(lists):
            if not node:
                continue
            heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode()
        tail = dummy

        while heap:
            _, i, root = heapq.heappop(heap)
            tail.next = root
            if root.next:
                heapq.heappush(heap, (root.next.val, i, root.next))
            tail = tail.next
        
        return dummy.next


# 1.11 复习自己写出来了
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        hp = []
        dummy = ListNode()
        cur = dummy

        for i in range(len(lists)):
            node = lists[i]
            if node:
                hp.append([node.val, i, node])
        heapq.heapify(hp)

        while hp:
            _, i, node = heapq.heappop(hp)
            cur.next = node
            if node.next:
                heapq.heappush(hp, [node.next.val, i, node.next])
            cur = cur.next
        
        return dummy.next