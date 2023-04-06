from typing import List

# 10.28 first try，backtracking基础题，直接看答案
# neetcode写的代码虽然简单但是很难理解执行逻辑
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            print("subset before append:", subset)
            if i >= len(nums):
                res.append(subset.copy())
                print(res)
                return
            # decision to include nums[i]
            print("include i:", i)
            subset.append(nums[i])
            dfs(i + 1)
            # decision NOT to include nums[i]
            print("not include i:", i)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

# call stack print出来是以下这样，这个执行顺序我真的很难理解。。。
# https://zhuanlan.zhihu.com/p/78214435 an article which might be helpful

# subset before append: []  <---- recursion deep dive start
# include i: 0
# subset before append: [1]
# include i: 1
# subset before append: [1, 2]
# include i: 2
# subset before append: [1, 2, 3]  <----- hit base case, append to result and first "adding" recursion reached end
# [[1, 2, 3]]

# not include i: 2  <----- backtracking at "include i: 2 with [1, 2]" stack of recursion, it popped 3 from subset
# subset before append: [1, 2] <---- after 3 is popped, dfs(3) is called again in the second recursion 
# [[1, 2, 3], [1, 2]]  <---- this recursion hits base case, append to result and return

# not include i: 1  <---- call stack returned to "include i: 1 with [1]" and continue to its backtracking, b/c "include i: 2" finished everything in its deep dive, this popped 2
# subset before append: [1]  <--- after 2 is popped, dfs(2) is called again in the second recursion
# include i: 2 <--- dfs(2) will append 3 to subset [1] and call dfs(3) with subset [1, 3], which hits the base case and append
# subset before append: [1, 3]
# [[1, 2, 3], [1, 2], [1, 3]]
# not include i: 2  <--- backtracking at "include i: 2 with [1]" stack of recursion, it popped 3 from subset
# subset before append: [1] <--- after 3 is popped, dfs(3) is called again in the second recursion
# [[1, 2, 3], [1, 2], [1, 3], [1]] <--- this recursion hits base case, returned and append to result

# not include i: 0 <--- call stack returned to "include i:0 with []" and continue to its backtracking, b/c "include i:1" finished everything in its deep dive, this popped 1
# subset before append: [] <--- after 1 is popped, dfs(1) is called again in the second recursion
# include i: 1 <---- dfs(1) will append 2 to subset [] and call dfs(2) with subset [2], 
# subset before append: [2]
# include i: 2 <---- dfs(2) will append 3 to subset [2] and call dfs(3) with subset [2, 3], which hits the base case and append
# subset before append: [2, 3] <----- it hit base case  append to result
# [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3]]
# not include i: 2 <---- backtracking at "include i: 2 with subset [2, 3]" stack of recursion, it popped 3 from subset
# subset before append: [2] <--- after 3 is popped, dfs(3) is called again in the second recursion
# [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2]] <--- this recursion hits base case, returned and append to result
# not include i: 1 <---- backtracking at "include i: 1 with subset [2]" stack of recursion, it popped 2 from subset
# subset before append: []
# include i: 2+
# subset before append: [3]
# [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3]]
# not include i: 2
# subset before append: []
# [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]


# 九章的另一种回溯办法， decision tree的build办法和neet code稍微不同
# 回溯的核心在于recursion function后面要跟一个回溯来撤销处理结果（in combination case就是remove，del，pop这种操作）
# 因此可以看到即便neet code和九章build tree方法不一样，但是recursion后都跟了pop或者del这种东西
# 以下先看没有回溯（即del statement)的错误代码产生的call stack
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], nums]

        res = []

        def dfs(i, subset):
            res.append(subset.copy())
            if i == len(nums):
                return
            for j in range(i, len(nums)):
                print("j in list:", j, list(range(i, len(nums))))
                subset.append(nums[j])
                print("subset:", subset)
                dfs(j+1, subset)
        
        dfs(0, [])
        return res
# j in list: 0 [0, 1, 2] <---- 起始dfs, 1st for loop 0 in [0, 1, 2]
# subset: [1]
# j in list: 1 [1, 2] <---- 1st recursion dfs, 1st for loop 1 in [1, 2]
# subset: [1, 2]
# j in list: 2 [2] <---- 2nd recursion dfs, the only for loop. inside which it calls the 3rd recursion, which will hit base case return and print nothing
# subset: [1, 2, 3]
# j in list: 2 [1, 2] <---- 1st recursion dfs, 2nd for loop 2 in [1, 2]
# subset: [1, 2, 3, 3]

# j in list: 1 [0, 1, 2] <---- 起始dfs, 2nd for loop 1 in [0, 1, 2]
# subset: [1, 2, 3, 3, 2]
# j in list: 2 [2] <----  1st recursion dfs, only for loop 2 in [2]
# subset: [1, 2, 3, 3, 2, 3]

# j in list: 2 [0, 1, 2] <---- 起始dfs, 3rd for loop 2 in [0, 1, 2]. 这个再call recursion, j+1 = 3直接hit base case并return
# subset: [1, 2, 3, 3, 2, 3, 3]


# 再看正确代码，有了del语句之后的call stack, 白板画了call stack图看手机拍的照片更易理解
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], nums]

        res = []

        def dfs(i, subset):
            res.append(subset.copy())
            if i == len(nums):
                return
            for j in range(i, len(nums)):
                print("j in list:", j, list(range(i, len(nums))))
                subset.append(nums[j])
                print("subset:", subset)
                dfs(j+1, subset)
                del subset[-1]
                print("subset after del:", subset)
        
        dfs(0, [])
        return res
# j in list: 0 [0, 1, 2] <---- 起始dfs, 1st for loop 0 in [0, 1, 2], it adds 1 to subset
# subset: [1]
# j in list: 1 [1, 2] <---- 1st recursion dfs, 1st for loop 1 in [1, 2], it adds 2 to subset.
# subset: [1, 2]
# j in list: 2 [2] <---- 2nd recursion dfs, the only for loop. it adds 3 to subset. inside which it calls the 3rd recursion, which will hit base case return and print nothing
# subset: [1, 2, 3]
# subset after del: [1, 2] <---- still inside 2nd recursion dfs, 因为3rd recursion hit the base case, 这时2nd recursion会执行recursion func后面的回溯语句，即 del 3
# subset after del: [1] <---- still inside 1st recursion dfs, 1st for loop 1 in [1, 2], 2nd recursion 回溯完毕了即执行完成，回到1st recursion的recursion call后面的code，即回溯语句，此时del 2
# j in list: 2 [1, 2] <---- 1st recursion dfs, 2nd for loop 2 in [1, 2], it adds 3 to the subset, inside which it calls next recursion with j+1 = 3, which hits base case.
# subset: [1, 3]
# subset after del: [1] <--- still inside 1st recursion dfs, 2nd for loop 2 in [1, 2], 因为recursion hit base case而执行回溯， del 3
# subset after del: []  

# j in list: 1 [0, 1, 2]
# subset: [2]
# j in list: 2 [2]
# subset: [2, 3]
# subset after del: [2]
# subset after del: []
# j in list: 2 [0, 1, 2]
# subset: [3]
# subset after del: []


# 11.29 复习自己写。不知咋的就很快写出来了。可能是刚做了17题的缘故
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, path):
            if i == len(nums) - 1:
                res.append(path)
                return
            backtrack(i + 1, path)
            backtrack(i + 1, path + [nums[i]])
        
        backtrack(-1, [])
        return res