from collections import defaultdict
# 10.06 first try, 其实没什么特别难的就是一个dict of list of tuples。 
# tuples第一位是timestamp，条件有写insert的时候是only in increasing order的。
# 然后就是get function要apply一个BST，但是如果要搜4分钟，我们只有记录3和5，没有exact match，那就用3分钟这个逻辑有点绕
class TimeMap:

    def __init__(self):
        self.store = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        store = self.store
        if not store or key not in store:
            store[key] = [(timestamp, value)]
        else:
            store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        store = self.store
        if not store or key not in store:
            return ""
        else:
            data = store[key]
            b, e = 0, len(data) - 1
            res = ""
            while b <= e:
                mid = (b + e) // 2
                if e == b + 1 and data[b][0] < timestamp and data[e][0] > timestamp:
                    res = data[b][1]
                    break
                elif e == b and data[b][0] != timestamp:
                    res = data[b][1] if data[b][0] < timestamp else data[b-1][1]
                    break
                elif data[mid][0] == timestamp:
                    res = data[mid][1]
                    break
                elif data[mid][0] < timestamp:
                    b = mid + 1
                else:
                    e = mid - 1
            return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


# neet code的代码
class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyStore = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])  # <--- 他这个set function 写的更简洁

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0] # <---- 灵性，只要mid比timestamp小，先把res设置成mid再说，比起我那一大堆的if elif简单多了
                l = m + 1
            else:
                r = m - 1
        return res

# 11.05复习自己写, 一开始写成了二分搜索而忘了我们要的不是exact match T O(logn)
class TimeMap:

    def __init__(self):
        self.store = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(timestamp, value)]
        else:
            self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.store.get(key, [])
        l, r = 0, len(values) - 1

        if values and values[r][0] == timestamp:
            return values[r][1]

        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]  # <--- 这行很重要，我们要的不是exact match所以不能按binary search那种if mid == xxx: return mid来写
                l = mid + 1
            else:
                r = mid - 1
        return res

# 12.13复习自己写，这个在44 test case TLE了但是算法思路没错，不知道为什neetcode写的能过而我TLE，算了就这样吧
class TimeMap:

    def __init__(self):
        self.store = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        time = list(self.store[key].keys())
        l, r = 0, len(time) - 1
        res_time = -1
        while l <= r:
            mid = (l + r) // 2
            if time[mid] <= timestamp:
                res_time = time[mid]
                l = mid + 1
            else: 
                r = mid - 1
        return self.store[key][res_time] if res_time >= 0 else ""