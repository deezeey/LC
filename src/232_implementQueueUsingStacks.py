# 9.29 一刷，自己思路是对的但是没想通，peek过后element只要待在pop stack里，即使push stack是空的我们仍然保持了queue存在的。
class MyQueue:

    def __init__(self):
        self.pushStack = []
        self.popStack = []

    def push(self, x: int) -> None:
        self.pushStack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.popStack.pop()

    def peek(self) -> int:
        if len(self.popStack) == 0:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
        return self.popStack[-1]        

    def empty(self) -> bool:
        return len(self.pushStack) + len(self.popStack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# 11.02 复习自己写，我感觉题目是不让用self.stack[0]的
class MyQueue:

    def __init__(self):
        self.stack = []
        self.count = 0
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        self.count += 1

    def pop(self) -> int:
        tmp = self.stack[0]
        del self.stack[0]
        self.count -= 1
        return tmp

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return self.count == 0

# 12.07 复习自己写
class MyQueue:

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def pop(self) -> int:
        self.peek()
        val = self.pop_stack.pop()
        return val

    def peek(self) -> int:
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack[-1]

    def empty(self) -> bool:
        return len(self.push_stack) == len(self.pop_stack) == 0