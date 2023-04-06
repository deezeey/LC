import random
# 2.23 first try，没有写，直觉是用hashmap存keys或者直接用set，
# 关于如何保证getRandom()能真正random我不知道自己怎么实现，maybe by hash value?
# 官方解释的很清楚为什么要用 arrayList + hashmap的组合
# https://leetcode.com/problems/insert-delete-getrandom-o1/editorial/
class RandomizedSet:

    def __init__(self):
        self.ls = []
        self.hash = {}

    def insert(self, val: int) -> bool:
        if val in self.hash: return False
        self.ls.append(val)
        self.hash[val] = len(self.ls) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash: return False
        idx = self.hash[val]
        last_val = self.ls[-1]
        self.ls[idx] = last_val
        self.hash[last_val] = idx # 换位置以后不要忘记update last value的idx
        self.ls.pop()
        del self.hash[val] #也不要忘记delete val from hash
        return True

    def getRandom(self) -> int:
        return random.choice(self.ls) # 正解就是使用random.choice function没想到吧。。。这个function从ls里随机pick element
