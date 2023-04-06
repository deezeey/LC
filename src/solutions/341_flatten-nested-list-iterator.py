# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> [NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

# 2.22 first try. 自己知道应该可以用generator写，但是写不出来，还是对怎么写generator不太熟
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.listGenerator = self.flatGenerator(nestedList)
        self.findNext()

    def flatGenerator(self, ls:List[int | List]):
        for e in ls:
            if isinstance(e, int):
                yield e
            else:
                yield self.flatGenerator(e)  # 其实就差一个from，这里改成yield from然后这个function里用上自带的 isInteger(), getInteger(), getList() func就好了

    def findNext(self):
        try:
            self.next_num = next(self.listGenerator)
        except:
            self.next_num = None
    
    def next(self) -> int:
        res = self.next_num
        self.findNext()
        return res
    
    def hasNext(self) -> bool:
        return True if self.next_num else False  # 这里不能是 if self.next_num 因为 它可以是0
    

# 官方正解的generator的写法
    class NestedIterator:

    def __init__(self, nestedList: [NestedInteger]):
        # Get a generator object from the generator function, passing in
        # nestedList as the parameter.
        self._generator = self._int_generator(nestedList)
        # All values are placed here before being returned.
        self._peeked = None

    # This is the generator function. It can be used to create generator
    # objects.
    def _int_generator(self, nested_list) -> "Generator[int]":
        # This code is the same as Approach 1. It's a recursive DFS.
        for nested in nested_list:
            if nested.isInteger():
                yield nested.getInteger()
            else:
                # We always use "yield from" on recursive generator calls.
                yield from self._int_generator(nested.getList())
        # Will automatically raise a StopIteration.
    
    def next(self) -> int:
        # Check there are integers left, and if so, then this will
        # also put one into self._peeked.
        if not self.hasNext(): return None
        # Return the value of self._peeked, also clearing it.
        next_integer, self._peeked = self._peeked, None
        return next_integer
    
    def hasNext(self) -> bool:
        if self._peeked is not None: return True
        try: # Get another integer out of the generator.
            self._peeked = next(self._generator)
            return True
        except: # The generator is finished so raised StopIteration.
            return False

# 根据官方的改了一下不知道为什么这个总是跑出来空集
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self._listGenerator = self._flatGenerator(nestedList)
        self.findNext()

    def _flatGenerator(self, ls):
        for e in ls:
            if isinstance(e, int):
                yield e.getInteger()
            else:
                yield from self._flatGenerator(e.getList())

    def findNext(self) -> None:
        try:
            self._next_num = next(self._listGenerator)
        except:
            self._next_num = None
    
    def next(self) -> int:
        res = self._next_num, self.findNext() # bug在这里把逗号后面东西挪到下一行就好了
        return res
    
    def hasNext(self) -> bool:
        return self._next_num is not None
         
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())