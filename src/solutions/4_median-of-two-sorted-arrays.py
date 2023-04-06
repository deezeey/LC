from typing import List
# 12.14 first try 10分钟过去了没什么思路，只想到了可能可以比较两个array分别的median然后调整指针，但没有具体思路

# neetcode写法 Time: log(min(n, m))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # A
            j = half - i - 2  # B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


# 自己重写了一遍
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        search, check = nums2, nums1
        TOTAL = len(nums1) + len(nums2)
        HALF = TOTAL // 2

        if len(nums1) < len(nums2):
            # always search the shorter array
            search, check = nums1, nums2

        l, r = 0, len(search) - 1
        while True: #while True makes l, r possible to go outside bounds so we reach +-inf to handle edge case
            search_l_e = (l + r) // 2
            check_l_e = HALF - search_l_e - 2

            # use infinite to handle edge case
            search_l = search[search_l_e] if search_l_e >= 0 else float("-inf")
            search_r = search[search_l_e + 1] if (search_l_e + 1) < len(search) else float("inf")
            check_l = check[check_l_e] if check_l_e >= 0 else float("-inf")
            check_r = check[check_l_e + 1] if (check_l_e + 1) < len(check) else float("inf")

            if search_l <= check_r and check_l <= search_r:
                # left half is correct
                if TOTAL % 2 == 0:
                    # even
                    return (max(search_l, check_l) + min(search_r, check_r)) / 2
                else:
                    # odd
                    return min(search_r, check_r)
            elif search_l > check_r:
                # if max of left half in search > min or right half in check, 
                # it means we need to include less elements from search left half
                r = search_l_e - 1
            else:
                l = search_l_e + 1

# 1.5 复习，不记得算法也不记得怎么写。重新背了一遍，这题是真的难。
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        search, check = nums1, nums2
        if len(nums1) > len(nums2):
            search, check = check, search
        TOTAL = len(nums1) + len(nums2)
        HALF = TOTAL // 2
        l, r = 0, len(search) - 1

        while True:
            search_mid = (l + r) // 2
            check_mid = HALF - search_mid - 2
            
            search_l = search[search_mid] if search_mid >= 0 else float("-inf")
            search_r = search[search_mid + 1] if search_mid + 1 < len(search) else float("inf")
            check_l = check[check_mid] if check_mid >= 0 else float("-inf")
            check_r = check[check_mid + 1] if check_mid + 1 < len(check) else float("inf")

            if search_l <= check_r and check_l <= search_r:
                if TOTAL % 2 == 0:
                    return (max(search_l, check_l) + min(search_r, check_r)) / 2
                else:
                    return min(search_r, check_r)
            elif search_l > check_r:
                r = search_mid - 1
            else:
                l = search_mid + 1

# 1.9 复习自己写了一遍，基本上写对了但是有细节错误导致跑不过 nums1 = [], nums2 = [1]的case
# 找到了bug，comments写在下面
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        TOTAL = len(nums1) + len(nums2)
        HALF = TOTAL // 2

        search, check = nums1, nums2
        if len(nums2) > len(nums1):  #这里写反了所以过不了
            search, check = check, search
        
        l, r = 0, len(search) - 1
        
        while l <= r: # 这里必须是while True否则可能会有return None的情况
            m = (l + r) // 2
            search_l_e, check_l_e = m, HALF - m - 2
            search_r_s, check_r_s = search_l_e + 1, check_l_e + 1
            search_l = search[search_l_e] if 0 <= search_l_e else float("-inf")
            check_l = check[check_l_e] if 0 <= check_l_e else float("-inf")
            search_r = search[search_r_s] if search_r_s < len(search) else float("inf")
            check_r = check[check_r_s] if check_r_s < len(check) else float("inf")
            if search_r >= check_l and check_r >= search_l:
                if TOTAL % 2 == 0:
                    return (max(search_l, check_l) + min(search_r, check_r)) / 2
                else:
                    return min(search_r, check_r)
            elif check_r < search_l:
                r = m - 1
            else:
                l = m + 1
