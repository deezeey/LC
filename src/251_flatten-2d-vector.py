from typing import List
# 2.18 firs try 好像很简单？只需要2个for loop的list comprehension
class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.arr = [e for r in vec for e in r]
        self.idx = 0

    def next(self) -> int:
        if self.idx >= len(self.arr):
            return
        res = self.arr[self.idx]
        self.idx += 1
        return res

    def hasNext(self) -> bool:
        if self.idx < len(self.arr):
            return True
        else:
            return False

# 正解是写iterator/generator, 不要新建一个arr，因为会用掉额外的memory
class Vector2D:
    def __init__(self, vec: List[List[int]]) -> None:
        self.flatVecGenerator = self.flatGenerator(vec) # 把vec pass进去generator function，才是我们需要的generator
        self.findNextNum() # initially先call一次next(generator)来找到第一个数字
            
    def flatGenerator(self, vec: List[List[int]]) -> int: # general generator
        for nums in vec:
            for num in nums:
                yield num
				
    def findNextNum(self) -> None:
        try:
            self.nextNum = next(self.flatVecGenerator)
        except: #如果generator yield全部的element了，就设置下一个数字为None
            self.nextNum = None

    def next(self) -> int:
        toReturn = self.nextNum; self.findNextNum() #直接return当前数字，并且yield下一个
        return toReturn

    def hasNext(self) -> bool:
        return self.nextNum is not None #如果下一个是None就不行

# 也可以用list comprehension的放式来写generator
class Vector2D:
    def __init__(self, vec: List[List[int]]) -> None:
        self.flatVecGenerator = (num for nums in vec for num in nums)
        self.findNextNum()
				
    def findNextNum(self) -> None:
        try:
            self.nextNum = next(self.flatVecGenerator)
        except:
            self.nextNum = None

    def next(self) -> int:
        toReturn = self.nextNum; self.findNextNum()
        return toReturn

    def hasNext(self) -> bool:
        return self.nextNum is not None