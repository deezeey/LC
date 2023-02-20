from typing import List
import heapq

# 12.11 first try，在9 out of 10 test case TLE了
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [-num for num in nums]
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        tmp = []
        k = self.k
        while k > 0:
            tmp.append(heapq.heappop(self.nums))
            k -= 1
        res = -tmp[-1]
        self.nums.extend(tmp)
        heapq.heapify(self.nums)
        return res

# neetcode写法。他只keep k个数
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # minHeap w/ K largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k: # 假设k是3，那么我们可以一直pop这个min heap直到只剩下3个数，这就是最大的3个数
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) 
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) # push了新数进去以后len会是4，这时候pop掉最小的一个
        return self.minHeap[0] #剩下的min heap的顶端，就是第3个最大的数，即3个最大数中，最小的那一个

# 1.4 复习自己写。也是只keep k个数。
# 但是我这个遇到[[2,[0]],[-1],[1],[-2],[-4],[3]] return了[null,0,1,1,1,3]，应该是[null,-1,0,0,0,1]
# 我没有考虑到一开始nums没有k个数的情况，这里是个坑需要注意
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.min_hp = nums
        heapq.heapify(self.min_hp)
        while len(self.min_hp) > k:
            # pop until min_hp becomes size k
            heapq.heappop(self.min_hp)

    def add(self, val: int) -> int:
        if self.min_hp and val <= self.min_hp[0]:
            return self.min_hp[0]
        else:
            if self.min_hp:
                heapq.heappop(self.min_hp)
            heapq.heappush(self.min_hp, val)
            return self.min_hp[0]

# 1.9 复习自己写，一开始还是不记得nums可以是empty的，submit错误后改过来了
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]