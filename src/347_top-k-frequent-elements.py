from typing import List
from collections import Counter
import heapq

# 12.03 first try自己做，但是这个应该不满足题目条件因为sort需要nlogn，但题目需要better than nlogn 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count = sorted(count, key=count.get, reverse=True)
        return count[:k]


# 12.04 自己写了个heap的，这个应该不用nlogn。因为count是O(n)。
# 然后heappop和heappush都是logn而且只要不是nums每个数字都disinct我们就不用做到n次因为count会比nums短。
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for num in count.keys():
            if len(heap) == k: 
                if count[num] > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (count[num], num))
                else:
                    continue
            else:
                heapq.heappush(heap, (count[num], num))
        
        return [tpl[1] for tpl in heap]


# better O(n) solution, bucket sort. 
# nums里面的字母，最多只能有len(nums)的count
# 我们instantiate一个hashmap，key是count，然后value是set of number。
# 最后从后往前iterate thru这个hashmap找到top k frequent nums
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count_hash = [set() for _ in range(len(nums) + 1)]
        for num, count in count.items():
            count_hash[count].add(num)
        
        res = []
        for bucket in count_hash[::-1]:
            if bucket:
                res.extend(bucket)
                k -= len(bucket)
            if k <= 0:
                return res


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        register = [set() for _ in range(len(nums))]  #需要注意记住initiate list of empty sets的方法
        res = []

        for num, count in count.items():  #注意这里不能用k, v 因为k会覆盖题目pass in的parameter
            register[count - 1].add(num)
        
        for nums in register[::-1]:
            if nums and k > 0:
                res.extend(nums)
                k -= len(nums)
            if k <= 0:
                return res


# 1.1 复习，还是不记得initiate empty set list的方法，查了答案
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [set() for _ in range(len(nums) + 2)]
        res = []
        cnt = Counter(nums)
        for key, val in cnt.items():
            freq[val].add(key)
        
        i = len(freq) - 1
        while k > 0 and i > 0:
            if freq[i]:
                res.extend(freq[i])
                k -= len(freq[i])
            i -= 1
        
        return res