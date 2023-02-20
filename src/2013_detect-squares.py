from collections import defaultdict
from typing import List

# 1.31 first try自己有思路但是写起来发现需要dict of dict感觉有点复杂不是正确思路？所以写到一半没写下去了
class DetectSquares:

    def __init__(self):
        self.x_map = defaultdict(set) # set of [y, count]
        self.y_map = defaultdict(set) # set of [x, count]
        
    def add(self, point: List[int]) -> None:
        x, y = point
        if y in self.x_map[x]:
            self.x_map[y] = [y, self.x_map[y][1] + 1]
        else:
            self.x_map[y] = [y, 1]
        if x in self.y_map:
            self.y_map[x] = [x, self.y_map[x][1] + 1]
        else:
            self.y_map[y] = [x, 1]

    def count(self, point: List[int]) -> int:
        # for given (x, y), we are looking for one of the below 4:
        # 0 < n <= min(x, y)
            # same y     +  same x    +  diagnal
            # (x + n, y) + (x, y - n) + (x + n, y - n)
            # (x + n, y) + (x, y + n) + (x + n, y + n)
            # (x - n, y) + (x, y + n) + (x - n, y + n)
            # (x - n, y) + (x, y - n) + (x - n, y - n)
        # it's better to find diagnal point first and then check if there's same x & same y
        x, y = point
        n_max = min(x, y)
        for n in range(1, n_max + 1):
            if x + n in self.y_map and y - n in self.y_map:
                pass

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

# 看了下neetcode的，和我思路相同但是，根本没必要x map y map弄那么复杂。
# 我自己是这样写的，但是跑起来会碰到如下error，还是不能只keep一个dict，需要一个count一个store
# RuntimeError: dictionary changed size during iteration
#     for x, y in self.store.keys():
# Line 20 in count (Solution.py)
#     result = obj.count(
# Line 46 in __helper_select_method__ (Solution.py)
#     ret.append(__DriverSolution__().__helper_select_method__(method, params[index], obj))
# Line 84 in _driver (Solution.py)
#     _driver()
# Line 93 in <module> (Solution.py)

class DetectSquares:

    def __init__(self):
        self.store = defaultdict(int) # count of pts at (x, y) key
        
    def add(self, point: List[int]) -> None:
        self.store[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        # for given (x, y), we are looking for one of the below 4:
        # 0 < n <= min(x, y)
            # same y     +  same x    +  diagnal
            # (x + n, y) + (x, y - n) + (x + n, y - n)
            # (x + n, y) + (x, y + n) + (x + n, y + n)
            # (x - n, y) + (x, y + n) + (x - n, y + n)
            # (x - n, y) + (x, y - n) + (x - n, y - n)
        # it's better to find diagnal point first and then check if there's same x & same y
        px, py = point
        res = 0
        for x, y in self.store.keys():
            if abs(x - px) != abs(y - py):
                continue
            res += self.store[(x, py)] * self.store[(px, y)]
        return res

# 然后自己再写了一遍，这个还是错误答案，不能用set，因为diagonal的点如果有重复，是不会被self.pt_count[(x, py)] * self.pt_count[(px, y)]计算在内的
# 所以我们actually需要带dupe的list
class DetectSquares:

    def __init__(self):
        self.pt_count = defaultdict(int) # count of pts at (x, y) tuple key
        self.store = set() # set of lists
        
    def add(self, point: List[int]) -> None:
        self.pt_count[tuple(point)] += 1
        self.store.add(tuple(point))

    def count(self, point: List[int]) -> int:
        # for given (x, y), we are looking for one of the below 4:
        # 0 < n <= min(x, y)
            # same y     +  same x    +  diagnal
            # (x + n, y) + (x, y - n) + (x + n, y - n)
            # (x + n, y) + (x, y + n) + (x + n, y + n)
            # (x - n, y) + (x, y + n) + (x - n, y + n)
            # (x - n, y) + (x, y - n) + (x - n, y - n)
        # it's better to find diagnal point first and then check if there's same x & same y
        px, py = point
        res = 0
        for x, y in self.store:
            if (abs(x - px) != abs(y - py)) or x == px or y == py: #不要漏掉check x和y是不是和source点相同
                continue
            res += self.pt_count[(x, py)] * self.pt_count[(px, y)]
        return res