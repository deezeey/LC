from typing import List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # always starts with lo
        # there will always be n // 2 hi
        # get the highs first and then insert the lows
        if len(nums) == 1:
            return nums
        k = len(nums) // 2 # we have k highs
        nums.sort(reverse=True)
        nums[::2], nums[1::2] = nums[k:], nums[:k]

# 这题真心难。。。
# 基本思路

# 先用Find Kth Smallest/Largest Number in an Array找中位数
# 再用3 Way Partition (148 Sort Colors) 分成 > mean | ==mean | <mean 3部分
# 结果奇数位 = 现在数组的后半部分(<=mean的部分，并且==mean的部分在最前面)
# 结果偶数位 = 现在数组的前半部分(>=mean的部分， 并且==mean的部分在最后面)
# 分成3个部分/把==mean的单独分出来的意义在哪里？中位数如有重复在第3和第4部被分到首尾去了，不会最后紧挨着
# 这个理论上的最优解，现实跑起来TLE， 呵呵
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find median using quick select, T O(n), M O(1)
        k = len(nums) // 2

        def partition(b, e):
            pivot = nums[e]
            cur, fill = b, b
            while cur < e:
                nums[cur], nums[fill] = nums[fill], nums[cur]
                if nums[fill] <= pivot:
                    fill += 1
                cur += 1
            nums[fill], nums[e] = nums[e], nums[fill]
            return fill

        l, r, median = 0, len(nums) - 1, None
        while l <= r:
            pivot = partition(l, r)
            if pivot == k:
                median = nums[k]
                break
            elif pivot < k:
                l = pivot + 1
            else:
                r = pivot - 1
        
        # putting numbers in place based on if the comparison with median
        # nums greater than median will be at odd idx, nums smaller than median will be at even idx
        # if nums[i] > median and i is not odd, switch nums[i], nums[o], o += 2
        # if nums[i] < median and i is not even, switch nums[i], nums[e], e -= 2
        i, n = 0, len(nums)
        o = 1 # odd are peaks
        e = n - 1 if (n - 1) % 2 == 0 else n - 2 # even are valleys
        # note e = 0, o = n-1/n-2 won't work here, 
        # b/c we've done partition so that smaller nums are in left side, they need to go to even idx, so even idx need to start from the end going backwards
        while i < n:
            if nums[i] > median and (i % 2 != 1 or o < i):
                nums[o], nums[i] = nums[i], nums[o]
                o += 2
                continue
            if nums[i] < median and (i % 2 != 0 or e > i):
                nums[e], nums[i] = nums[i], nums[e]
                e -= 2
                continue
            i += 1
        return nums