from typing import List
# 3.8 first try 能过 142/265 cases，思路是对的但是没注意到细节
# 碰到nums = [1,3,2]挂了。我的output[2,3,1]但结果应该是[2,1,3]
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # still a valid permutation of the same array
        # lexicographically larger than cur arrangement
        # swapping digit, cur d will be swapped with a strictly rightmost larger d strictly from its right
        # if new d comes from its left, then it will become lexicographically smaller
        # for nums[i] what is the next digit that's greater than nums[i] in range(i+1, :)
        
        # 1 pass find the first decreasing num from right
        N = len(nums)
        i, target = N - 1, -1
        while i > 0:
            if nums[i - 1] < nums[i]:
                target = i - 1
                break
            i -= 1
        # if we can't find such a num, then its stritcly decreasing from left to right, we change it to strictly increasing
        if not i:
            nums.sort()
            return nums
        # 2 pass find the first digit greater than prev found num and swap them
        j = N - 1
        while j > 0:
            if nums[j] > nums[target]:
                nums[j], nums[target] = nums[target], nums[j]
                return nums
            j -= 1

# 其实就差reverse所有target以右的部分以保证lexicographical最小
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # helper func
        def _reverse(s, e):
            while s <= e:
                nums[s], nums[e] = nums[e], nums[s]
                s += 1
                e -= 1
        
        # 1 pass find the first decreasing num from right
        N = len(nums)
        i, target = N - 1, -1
        while i > 0:
            if nums[i - 1] < nums[i]:
                target = i - 1
                # swap with rightmost larger digit than target
                j = N - 1
                while nums[j] <= nums[target]:
                    j -= 1
                nums[j], nums[target] = nums[target], nums[j]
                # reverse the digit after swapped position, so it's in smallest lexicographical order
                _reverse(target+1, N-1)
                return nums
            i -= 1
        if i == 0:
            _reverse(0, N-1)
        return nums