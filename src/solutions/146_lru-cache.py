# 10.17 first try自己用doubly linked list写的，思路是对的但是对doubly linked list不熟悉，有些固定用来handle edge case的技巧要学会
# 写了三四个小时，各种edge case改了一堆，然后submit还是报错
class Node:
    def __init__(self, key: None, value: None, prev: None, next: None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.items = {}
        self.head_key = None
        self.tail_key = None

    def get(self, key: int) -> int:
        # print('get', key)
        if key == self.tail_key:
            return self.items[key].value
        elif key in self.items:
            node = self.items[key]
            if key == self.head_key and node.next:
                self.head_key = node.next.key
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            prev_tail = self.items[self.tail_key]
            node.prev = prev_tail
            prev_tail.next = node
            node.next = None
            self.tail_key = node.key
            # print('head and tail', self.head_key, self.tail_key)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # print('put', key)
        if not self.items:
            node = Node(key, value, prev = None, next = None)
            self.count += 1
            self.head_key = key
            self.tail_key = key
            self.items[key] = node
        else:
            if key == self.tail_key:
            # if putting new value to the tail, we only need to update value of the tail node
                node = self.items[self.tail_key]
                node.value = value
            elif key in self.items:
            # if key exist, update current node and break the link
                node = self.items[key]
                node.value = value
                if key == self.head_key:
                    node.next.prev = None
                    self.head_key = node.next.key
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                node.prev = self.items[self.tail_key]
                node.next = None
                self.items[self.tail_key].next = node
            else:
            # else create new node and pop the lru node if we're at capacity
                if self.count == self.capacity:
                    # pop head
                    new_head = self.items[self.head_key].next
                    # print(self.head_key, self.items[self.head_key])
                    if new_head:
                        new_head.prev = None
                    del self.items[self.head_key]
                    if not self.items:
                        self.head_key = self.tail_key = None
                    else:
                        self.head_key = new_head.key
                    self.count -= 1
                if not self.head_key: # check if cache is empty after popping
                    node = Node(key, value, prev = None, next = None)
                    self.head_key = key
                else:
                    node = Node(key, value, prev = self.items[self.tail_key], next = None)
                    self.items[self.tail_key].next = node
                self.count += 1
            # append the node to tail
            self.tail_key = key
            self.items[key] = node
            # print('items', self.items)
            # print('head and tail', self.head_key, self.tail_key)


# 看了九章答案以后重写的，虽然都是doubly linked list，但是正解看起来非常简洁。原因1是用了dummy head and tail，原因2是写了两个internal helper function
class Node:
    def __init__(self, key: None, value: None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.cache = dict() # <--- 首先cache里key对应的value是node而不是int
        self.head = self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _detach_node(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_tail(self, node) -> None:
        prev_last = self.tail.prev # <--- 这里的self.tail是一个dummy node，真正的tail永远都是self.tail.prev
        prev_last.next = node
        self.tail.prev = node
        node.prev = prev_last
        node.next = self.tail

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        node = self.cache[key]
        self._detach_node(node)
        self._move_to_tail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._detach_node(node)
            self._move_to_tail(node)
        else:
            if self.count == self.capacity:
                first_node = self.head.next # <--- 这里的self.head也是个dummy node，真正的head永远是self.head.next
                self._detach_node(first_node)
                del self.cache[first_node.key]
                self.count -= 1
            node = Node(key, value)
            self.cache[key] = node
            self._move_to_tail(node)
            self.count += 1


# 11.09复习，一开始自己压根儿不记得用doubly linked list做，用了hashmapped linked list所以get和put都是 T O(1)， M O(n) n是capacity
class ListNode:
    
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.head = self.tail = ListNode() # <--- these two are dummies and will be forever empty
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _detach_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _move_to_tail(self, node):
        # use a dummy tail to prevent NoneType error
        real_tail = self.tail.prev
        real_tail.next = node
        node.prev = real_tail
        node.next = self.tail
        self.tail.prev = node
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._detach_node(node)
            self._move_to_tail(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        # if key exists, update key
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._detach_node(node)
            self._move_to_tail(node)
        else:
            # if at capacity, evict lru key
            if len(self.cache) == self.capacity:
                real_head = self.head.next
                self._detach_node(real_head)
                del self.cache[real_head.key]
            # put new key, update lru
            node = ListNode(key, value)
            self._move_to_tail(node)
            self.cache[key] = node


# 1.10 自己可能写了快一个小时，这题真的就是很难写，容易出各种问题
# 看了一下前面的答案。要记得写detach node和move to tail helper function啊！！
class Node:
    def __init__(self, val: int, key: Optional[int]):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # capacity and cache
        self.cap = capacity
        self.cache = {}
        self.head = Node(val = 0, key = None)
        self.tail = Node(val = 0, key = None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # returns -1 if key is not in cache
        if not key in self.cache:
            return -1
        # needs to update lru / put node to tail
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        real_tail = self.tail.prev
        real_tail.next = node
        node.prev = real_tail
        node.next = self.tail
        self.tail.prev = node
        return node.val

    def put(self, key: int, value: int) -> None:
        # update key or insert key
        if not key in self.cache:
            node = Node(val = value, key = key)
            real_tail = self.tail.prev
            node.prev = real_tail
            node.next = self.tail
            real_tail.next = node
            self.tail.prev = node
            self.cache[key] = node
        else:
            node = self.cache[key]
            node.val = value
            self.get(key)
        # need to check lru, evict if needed        
        if len(self.cache) > self.cap:
            real_head = self.head.next
            self.head.next = real_head.next
            real_head.next.prev = self.head
            if real_head.key in self.cache:
                del self.cache[real_head.key]