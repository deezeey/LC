from typing import List
import heapq

# 11.10 first try, max heap. 
# 时间分析：heapify用到O(n), heappop了k次是klogn 所以是O(n + klogn)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = None
        nums = [-num for num in nums]
        heapq.heapify(nums)
        for _ in range(k):
            res = -heapq.heappop(nums)
        return res

# 看了neet code以后默写的quick select
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n)
#   - Worst Case: O(n^2)
# Extra Space Complexity: O(1)
# QuickSelect algorithm is O(n) on average because it uses the QuickSort partitioning mechanism to divide the input array into smaller sub-arrays, 
# and it only recurses on one of the sub-arrays, reducing the problem size by roughly half in each iteration. 
# This results in an average-case runtime of O(n).
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # edge case
        if len(nums) == 1:
            return nums[0]

        def partition(vectors, left, right):
            fill, pivot = left, vectors[right]
            for i in range(left, right):
                if vectors[i] <= pivot:  # <---一开始这里写成了 <，是个很要命的错误
                    vectors[fill], vectors[i] = vectors[i], vectors[fill]
                    fill += 1
            vectors[fill], vectors[right] = vectors[right], vectors[fill]
            return fill
        
        l, r = 0, len(nums) - 1
        k = len(nums) - k

        while l < r:
            fill = partition(nums, l, r)
            if fill < k:
                l = fill + 1
            elif fill > k:
                r = fill - 1
            else:
                break
        
        return nums[k]  # <-- 一开始return了nums[fill], 跑不过 nums = [2, 1], k = 1的case,
        # 因为那个case只有一个while循环，k是1，但是一次partition之后，fill=0，进入 if fill < k: l = fill + 1判断语句，
        # l = 1, 那么l == r所以不再继续下一个while loop。已经被sort成【1，2】了。但fill = 0, k = 1


# 11.30复习自己写还是只记得heap的方法。
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapify it takes O(n)
        # then pop k times
        nums = [-1 * num for num in nums]
        heapq.heapify(nums)
        res = None
        for _ in range(k):
            res = -1 * heapq.heappop(nums)
        return res


# 12.12 复习自己总算记得quick select怎么写了
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def partition(s, e):
            pivot = nums[e]
            p, fill = s, s
            while p < e:
                if nums[p] < pivot:
                    nums[p], nums[fill] = nums[fill], nums[p]
                    p += 1
                    fill += 1
                else:
                    p += 1
            nums[fill], nums[e] = nums[e], nums[fill]
            return fill
        
        def quick_select(l, r):
            while l <= r:
                pivot_idx = partition(l, r)
                if pivot_idx == k:
                    return nums[k]
                elif pivot_idx > k:
                    r = pivot_idx - 1
                else:
                    l = pivot_idx + 1
        
        return quick_select(0, len(nums) - 1)


# 1.1 复习只记得怎么写partition了忘了其实要binary search的，这个会stack overflow
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def partition(nums):
            pivot = len(nums) - 1
            cur, fill = 0, 0
            while cur < len(nums) - 1:
                if nums[cur] < nums[pivot]:
                    nums[cur], nums[fill] = nums[fill], nums[cur]
                    fill += 1
                cur += 1
            nums[pivot], nums[fill] = nums[fill], nums[pivot]
            return fill # index of the pivot num after partiton

        while True:
            fill = partition(nums)
            if fill == k:
                break
                
        return nums[fill]
        
        
# 看了一眼原来写的代码，补上了binary search的部分
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def partition(s, e):
            pivot = e
            cur, fill = s, s
            while cur < e:
                if nums[cur] < nums[pivot]:
                    nums[cur], nums[fill] = nums[fill], nums[cur]
                    fill += 1
                cur += 1
            nums[pivot], nums[fill] = nums[fill], nums[pivot]
            return fill # index of the pivot num after partiton

        l, r = 0, len(nums) - 1
        while l <= r: #很重要这里一定要是 <=， <的话在nums只有1个数或者2个数时候不work
            fill = partition(l, r)
            if fill == k:
                return nums[fill]
            elif fill < k:
                l = fill + 1
            else:
                r = fill - 1 

# 1.9 复习写了30min写出来了
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def partition(b, e) -> int:
            cur, fill = b, b
            pivot = nums[e]
            while cur < e:
                nums[cur], nums[fill] = nums[fill], nums[cur]
                if nums[fill] <= pivot:  #一开始这里写成了nums[cur] <= pivot找了半天bug
                    fill += 1
                cur += 1
            nums[fill], nums[e] = nums[e], nums[fill]
            return fill
        
        l, r = 0, len(nums) - 1
        while l <= r:
            res = partition(l, r)
            if res == k:
                return nums[res]
            elif res > k:
                r = res - 1
            else:
                l = res + 1