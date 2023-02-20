from typing import List

# 1.11 first try。5分钟自己写出来的是 T O(n) M O(n)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = set()

        for n in nums:
            if n in visited:
                return n
            visited.add(n)


# 正解是floyd's algorithm
# 看似是array其实是linked list with a cycle
# 题目给出的重要条件是，array里的数字最大只能是长度n。
# 所以【1，3，4，2，2】可以看作0位是一个值为1的node，同时指向1位，得到node3，所以node3 val=3并指向3位得到node2，node2指向2位得到node4，node4指向2位又得到node2，发现cycle
# 画出来是 1-->3-->2-->4-->2 cycle
# 同理【3，1，3，4，2】可以看作0位node1 val=3, 指向idx3，node2 val=4，指向idx4， node3 val=2，指向idx2，node4 val=3 所以又指回了node1
# 明白这个原理后，首先用快慢指针找到首次重叠的节点。
# 然后再设置一个慢指针，于重叠节点的慢指针一起移动，当它们再次重叠，必然是cycle的开头
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] #要想通linked list用array怎么表现
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                break
        return slow