from typing import List

# 03.04 first try自己想的解，TLE了，当然肯定没这么简单
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # [5, 2, 4, 6, 1, 1] 
        # iterate from right to left, if nums[i + 1] < nums[i]: then res[i] = len(nums) - 1 - i
        # while nums[i + 1] >= nums[i], swap them, res[i] = len(nums) - 1 - final_idx
        N = len(nums)
        res = [0] * N
        i = N - 2
        while i >= 0:
            if nums[i + 1] < nums[i]:
                res[i] = N - 1 - i
            else:
                j = i
                while j + 1 < N and nums[j + 1] >= nums[j]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    j += 1
                res[i] = N - 1 - j
            i -= 1
        return res

# 自己写了个quick sort后来发现理解错题目了，问的不是总共有多少个数比当前数字小而是右边有多少个比当前数字小
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # [5, 2, 4, 6, 1, 1] 
        # if we use quick sort?
        # dict to store {num: res}
        # do quick sort with a base idx, returned pos + base is res for this pivot num
        # and then everything to its left has base as cur_base, everything to its right has base of res + 1
        # partition func needs to record the count of nums = pivot, res of pivot will be base + fill pos - dupe count
        # right part partition base = fill pos + 1, left part partition base = prev base
        res_hash = {}
        def _partition(arr: List[int], base: int) -> None:
            if not arr:
                return
            if len(arr) == 1:
                res_hash[arr[0]] = base
                return
            pivot = arr[-1]
            i, fill, dupe_cnt = 0, 0, 0
            while i < len(arr) - 1:
                if arr[i] <= pivot:
                    if arr[i] == pivot:
                        dupe_cnt += 1
                    arr[i], arr[fill] = arr[fill], arr[i]
                    fill += 1
                i += 1
            arr[i], arr[fill] = arr[fill], arr[i]
            res_hash[pivot] = base + fill - dupe_cnt
            _partition(arr[:fill], base)
            _partition(arr[fill+1:], base+ fill + 1)

        _partition(nums[::], 0)
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = res_hash[nums[i]]
        return res


# 官方正解merge sort, T O(nlogn) M O(n)
# basic idea是在merge 2个array的时候，如果把某些数字插入到另一个数字前面了，那么它们肯定是在此数字右边的比他更小的数字，即可计入res
# 如果下一个最小来自右边arr，直接append，来自左边arr，append左边之前要计算一下右边目前已经append了多少个，即右边的idx-mid
# 有点难理解，可以带入[4, 2, 5, 6, 1, 1]的例子自己过一遍
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [[v, i] for i, v in enumerate(nums)]  # record value and index
        result = [0] * n

        def merge_sort(arr, left, right):
            # merge sort [left, right) from small to large, in place
            if right - left <= 1:
                return
            mid = (left + right) // 2
            merge_sort(arr, left, mid)
            merge_sort(arr, mid, right)
            merge(arr, left, right, mid)

        def merge(arr, left, right, mid):
            # merge [left, mid) and [mid, right)
            i = left  # current index for the left array
            j = mid  # current index for the right array
            # use temp to temporarily store sorted array
            temp = []
            while i < mid and j < right:
                if arr[i][0] <= arr[j][0]:
                    # j - mid numbers jump to the left side of arr[i]
                    result[arr[i][1]] += j - mid  #这里为什么不是直接+1而是 j - mid需要好好想一想，带入[[4][2, 5]]的例子自己过一遍
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1
            # when one of the subarrays is empty
            while i < mid:
                # j - mid numbers jump to the left side of arr[i]
                result[arr[i][1]] += j - mid
                temp.append(arr[i])
                i += 1
            while j < right:
                temp.append(arr[j])
                j += 1
            # restore from temp
            for i in range(left, right):
                arr[i] = temp[i - left]

        merge_sort(arr, 0, n)

        return result
    
# 自己默写了一遍merge sort
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        N = len(nums)
        for i, v in enumerate(nums):
            nums[i] = [v, i]
        res = [0] * N
        def _mergeSort(l, r): # [l, r)
            if r - l <= 1:
            # if nums has only 1 element it means the res will just be 0
                return
            m = l + (r - l) // 2
            # mergesort left & right part in place then merge 2 sorted parts
            _mergeSort(l, m)
            _mergeSort(m, r)
            _merge(l, m, r)

        # while merging counting the nums jumped from right to left
        def _merge(left, mid, right):
            sorted_arr = []
            i, j = left, mid
            while i < mid and j < right:
                if nums[i][0] <= nums[j][0]:
                # nums from right arr naturally falls to the right of any number from left arr
                # if next smallest comes from left arr, count how many nums from right arr jumped before it
                    res[nums[i][1]] += j - mid
                    sorted_arr.append(nums[i])
                    i += 1
                else:
                # if next smallest comes from right arr, append directly
                    sorted_arr.append(nums[j])
                    j += 1
            # handle leftovers from single arr
            while i < mid:
                res[nums[i][1]] += j - mid
                sorted_arr.append(nums[i])
                i += 1
            while j < right:
                sorted_arr.append(nums[j])
                j += 1
            # update original nums using merged sorted arr
            for k in range(left, right):
                nums[k] = sorted_arr[k - left]
            
        _mergeSort(0, N)
        return res