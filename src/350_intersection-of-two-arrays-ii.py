from collections import Counter
from typing import List

# 2.7 first try
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1, count2 = Counter(nums1), Counter(nums2)
        res = []
        for num in count1:
            if num in count2:
                freq = min(count1[num], count2[num])
                for _ in range(freq):
                    res.append(num)
        return res

# follow up里面的如果sorted我们就换two pointers做也应该很简单的