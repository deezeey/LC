from typing import List
from collections import Counter

# 2.25 first try自己40min写出来的DP解法，能过但是TM不是非常好
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # self.arr1, self.arr2, self.arr3, self.arr4 = nums1, nums2, nums3, nums4
        # return count of tuples that sum up to 0
        # pick one from every arr
        # res[arr1, arr2, arr3, arr4, 0] = res[arr2, arr3, arr4, -v1] for v1 in arr1
        # res[arr2, arr3, arr4, v1] = res[arr3, arr4, -v1 - v2] for v2 in arr2
        # res[arr3, arr4, -v1 - v2] = res[arr4, -v1 - v2 - v3] for v3 in arr3
        # res[arr4, -v1 - v2 - v3] = count of (-v1 - v2 - v3) in  v4
        self.inputArrs = [nums1, nums2, nums3, nums4]
        return self.waysToForm(0, 0)

    @lru_cache(maxsize=None)
    def waysToForm(self, arr_idx:int, target) -> int:
        if arr_idx == 3:
            count = 0
            for e in self.inputArrs[3]:
                if e == target:
                    count += 1
            return count
        else:
            for i in range(arr_idx, 4):
                arr = self.inputArrs[i]
                ele_count = Counter(arr)
                res = 0
                for k, v in ele_count.items():
                    ele_res = self.waysToForm(i+1, target - k)
                    res += (v * ele_res)
                return res

# 别人写的解 。。。。seriously？
# 这个T是n^2 x 2 = O(n^2) M也和T一样
def fourSumCount(self, A, B, C, D):
    AB = Counter(a+b for a in A for b in B)
    return sum(AB[-c-d] for c in C for d in D)


# 理论上这样写也可以过，但是会TLE因为 n^3可比n^2大不少
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        AB = Counter(a + b + c for a in nums1 for b in nums2 for c in nums3)
        return sum(AB[-d] for d in nums4)
