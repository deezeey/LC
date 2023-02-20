from typing import List

def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort() #sort很重要一定要sort
    N, res = len(nums), []
    for i in range(N):
        if i > 0 and nums[i] == nums[i-1]: #从index 1开始，如果此数和前数相同，要skip
            i += 1
        else:
            target = 0 - nums[i] #确定了nums[i],三数之和变两数之和
            s = i + 1
            e = N - 1
            while s < e:
                if nums[s] + nums[e] == target:
                    res.append([nums[i], nums[s], nums[e]])
                    s += 1
                    while s < e and nums[s] == nums[s-1]: #如果下一个nums[s]和前数相同，直接skip，因为这个nums[s]的答案已经被记录过了
                    # 注意这里如果写 s < e - 1的话，碰到[0,0,0,0]这个case，结果会是[[0,0,0], [0,0,0]]而不是[0,0,0]
                        s += 1
                elif nums[s] + nums[e] < target: #因为是sort过的，所以我们可以靠移动前后指针来找sum to target的数
                    s += 1
                else:
                    e -= 1
    return res

# 9.24 复习自己错误的解1
def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    N = len(nums)
    res = []
    for i in range(N):
        if i > 0 and nums[i] == nums[i-1]:
            i += 1
        else:
            fixed = nums[i]
            target = 0 - fixed
            l, r = i+1, N-1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([fixed, nums[l], nums[r]])
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
                l += 1 # <----- 错就错在这个 l+=1摆错了位置
    return res

# 9.25 复习自己错误的解2
def threeSum(self, nums: list[int]) -> list[list[int]]:
    nums.sort()
    N = len(nums)
    res = []
    for i in range(N):
        if i > 0 and nums[i] == nums[i-1]:
            i += 1
        else:
            fixed = nums[i]
            target = 0 - fixed
            l, r = i+1, N-1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([fixed, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1]: # <---- 错在这里忘记l < r，这个while loop没有给l限制最大boundary，最大boundary应该是nums的最右端，即r
                        l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
    return res


# 11.04 复习，这题真感觉我就是背下来的。
# while loop解决two sum问题是 O(n),外层iterate thru nums,所以3sum是n * O(n)即 O（n^2), sort是 O(nlogn)但是这个只做一遍且小于n^2所以还是O(n^2)
# 空间是O(1) 因为我们只maintain了res本身
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # [-4,-1,-1,0,1,2]
        nums.sort()
        N = len(nums)
        res = []

        for i, num in enumerate(nums):
            if i >= 1 and num == nums[i-1]:
                continue
            if num > 0:
                break   # <--- 看别人这个break加的好聪明，学到了
            target = -num
            l, r = i + 1, N - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1

        return res  

# 12.12 复习自己写的不知道如何去重。。。example test case会return [[-1,0,1],[0,-1,1],[-1,-1,2],[2,-1,-1],[1,-1,0]]
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        visited = set()
        for i in range(len(nums)):
            hold = nums[i]
            if hold in visited:  # 不需要initiate visited，只要nums[i] == nums[i - 1] continue就好
                continue
            visited.add(hold)
            target = 0 - hold
            ans = set()
            l, r = 0, len(nums) - 1 # 这个是错的 l应该是i + 1
            while l < r:
                if l == i: # 如果把l设置成i + 1的话这两个if continue都不用写了
                    l += 1
                    continue
                if r == i:
                    r -= 1
                    continue
                if nums[l] + nums[r] == target:
                    ans.add((hold, nums[l], nums[r]))
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
            res.update(ans)
        return list(res)

# 12.15 复习自己写，不知道可能是蒙对的，大概就是背下来的
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            n = nums[i]
            target = 0 - n
            l, r = i + 1, len(nums) - 1
            while l < r:
                if l > i + 1 and nums[l] == nums[l - 1]:
                    l += 1
                    continue
                if nums[l] + nums[r] == target:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return res

# 1.9 复习自己写，不知道怎的蒙对了？
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0

        while i < len(nums) - 2:
            hold = nums[i]
            target = 0 - hold
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([hold, nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1

            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
        
        return res