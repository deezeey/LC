from typing import List

# 自己快写完了但是总觉得如果要写的这么复杂不可能是easy题就没再写了
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                tmp = nums1[i]
                nums1[i] = nums2[j]
                if j == n - 1 or nums2[j + 1] >= tmp:
                    nums2[j] = tmp
                else:
                    k = j + 1
                    while k < n and nums2[k] < tmp:
                        k += 1
                    nums2[k] = tmp
        if j < n:
            nums1[i+1]
        
# neetcode的写法，从右往左食用更佳
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m, n, fill = m - 1, n - 1, len(nums1) - 1
        while m >= 0 and n >= 0:
            if nums1[m] <= nums2[n]:
                nums1[fill] = nums2[n]
                n -= 1
            else:
                nums1[fill] = nums1[m]
                m -= 1
            fill -= 1
        if n >= 0:
            nums1[:n+1] = nums2[:n+1]