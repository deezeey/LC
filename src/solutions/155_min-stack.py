# 10.04 first try, 自己想用linked list做，但是min功能碰到pop就没办法？
class stackNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class MinStack:

    def __init__(self, min_val=None, head=None):
        self.min_val = min_val
        self.head = head
        
    def push(self, val: int) -> None:
        head = stackNode(val=val, next=self.head)
        self.head = head
        if not self.min_val or val < self.min_val:
            self.min_val = val

    def pop(self) -> None:
        head = self.head
        self.head = self.head.next

    def top(self) -> int:
        head = self.head
        return head.val

    def getMin(self) -> int:
        return self.min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# 看了提示以后修改了一下自己的代码，即我们不在stack level maintain单独一个min value，而是每个被push成为stack head的node都有自己current level的一个min value
# 这样pop就完全不会影响到min value的维持
class stackNode:
    def __init__(self, val=None, next=None, min_val=None):
        self.val = val
        self.next = next
        self.min_val = min_val

class MinStack:

    def __init__(self, head=None):
        self.head = head
        
    def push(self, val: int) -> None:
        if not self.head:
            cur_min_val = val
        else:
            cur_min_val = min(self.head.min_val, val)
        head = stackNode(val=val, next=self.head, min_val=cur_min_val)
        self.head = head

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min_val


# neetcode的解法，没有用linked list而是用python list，但思路是差不多的
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# 11.09复习，一开始没想到如何maintain order by value & order by insert order，
# 后来看答案自己先写了一遍neet code的，又写了一遍linked list的
class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.cur_min = val

class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        node.cur_min = self.head.cur_min if self.head and self.head.cur_min < val else val
        self.head = node

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.cur_min


# 1.10 复习自己想了10分钟记起来linked list的怎么写的了
class Node:
    def __init__(self, val: int):
        self.val = val
        self.min = None
        self.prev = None

class MinStack:
    def __init__(self):
        self.tail = None

    def push(self, val: int) -> None:
        node = Node(val)
        if not self.tail:
            node.min = val
            self.tail = node
        else:
            node.min = min(self.tail.min, val)
            node.prev = self.tail
            self.tail = node

    def pop(self) -> None:
        self.tail = self.tail.prev

    def top(self) -> int:
        return self.tail.val

    def getMin(self) -> int:
        return self.tail.min