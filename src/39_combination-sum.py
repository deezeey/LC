from typing import List

# 10. 05 first try. 第一次做back tracking，毫无头绪，neetcode讲解看懂了但是代码为什么这么写完全想不通
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # 两种base case一个是得到了一种解法return, 一个是确定当前path错误不用再往下走return
            if total == target:
                res.append(cur.copy())  # <---- list是mutable的，所以如果直接append cur，later when cur is updated, the appended version of cur is also going to change. 还有.copy()现在可能不work了，可以用append(cur[:])
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i]) # <------ make the choice
            # print("appended:", i, cur, total + candidates[i])
            dfs(i, cur, total + candidates[i]) # <----- go make next choice
            cur.pop()  # <------ backtracking if recursion reaches the end
            # print("popped:", i + 1, cur, total)
            dfs(i + 1, cur, total) # <----- 回溯之后重新走另一条路

        dfs(0, [], 0)
        return res

# 以下是print out的结果，结合print理解一下
# appended: 0 [2] 2
# appended: 0 [2, 2] 4
# appended: 0 [2, 2, 2] 6
# appended: 0 [2, 2, 2, 2] 8  <---- total > target, return and pop 2
# popped: 1 [2, 2, 2] 6
# appended: 1 [2, 2, 2, 3] 9  <---- total > target, return and pop 3
# popped: 2 [2, 2, 2] 6
# appended: 2 [2, 2, 2, 6] 12  <---- total > target, return and pop 6
# popped: 3 [2, 2, 2] 6
# appended: 3 [2, 2, 2, 7] 13  <---- total > target, return and pop 7
# popped: 4 [2, 2, 2] 6  <---- i>= len(candidates), return and pop 2
# popped: 1 [2, 2] 4 <---- how the fxxk did i and total change here?
# appended: 1 [2, 2, 3] 7
# popped: 2 [2, 2] 4
# appended: 2 [2, 2, 6] 10
# popped: 3 [2, 2] 4
# appended: 3 [2, 2, 7] 11
# popped: 4 [2, 2] 4
# popped: 1 [2] 2
# appended: 1 [2, 3] 5
# appended: 1 [2, 3, 3] 8
# popped: 2 [2, 3] 5
# appended: 2 [2, 3, 6] 11
# popped: 3 [2, 3] 5
# appended: 3 [2, 3, 7] 12
# popped: 4 [2, 3] 5
# popped: 2 [2] 2
# appended: 2 [2, 6] 8
# popped: 3 [2] 2
# appended: 3 [2, 7] 9
# popped: 4 [2] 2
# popped: 1 [] 0
# appended: 1 [3] 3
# appended: 1 [3, 3] 6
# appended: 1 [3, 3, 3] 9
# popped: 2 [3, 3] 6
# appended: 2 [3, 3, 6] 12
# popped: 3 [3, 3] 6
# appended: 3 [3, 3, 7] 13
# popped: 4 [3, 3] 6
# popped: 2 [3] 3
# appended: 2 [3, 6] 9
# popped: 3 [3] 3
# appended: 3 [3, 7] 10
# popped: 4 [3] 3
# popped: 2 [] 0
# appended: 2 [6] 6
# appended: 2 [6, 6] 12
# popped: 3 [6] 6
# appended: 3 [6, 7] 13
# popped: 4 [6] 6
# popped: 3 [] 0
# appended: 3 [7] 7
# popped: 4 [] 0


# another one, I think this is the best one which is easiest to understand
# 排序之后不需回溯，比起neet code的回溯写法，这种排序后dfs的写法效率更高
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(remain, cur):
            print("dfs(", remain, ", ", cur, ")")
            # base case
            if remain == 0:
                res.append(cur)
                return # return会让[2, 2, 3] 变成[2, 3]，即结束[2, 2, x]第三位的这个for loop，不会check[2, 2, 6]之类的，直接回归上一层recursion，即两位的for loop[2, x]
            
            for num in candidates:
                if num > remain:
                    break  # break会让[2, 2, 2] 变成 [2, 2, 3] 即在原位置choose another option，still inside the same for loop
                if cur and num < cur[-1]: # <--- 这样找到了[2, 2, 3]以后dfs(4, [3])就不会再check 2了
                    continue
                else:
                    dfs(remain - num, cur + [num])
        
        dfs(target, [])
        return res

# candidates = [2, 3, 6, 7], target = 7的call stack
# dfs( 7 ,  [] )
# dfs( 5 ,  [2] )
# dfs( 3 ,  [2, 2] )
# dfs( 1 ,  [2, 2, 2] ) <--- num > remain, break, continue the for loop with 3 as the 3rd element
# dfs( 0 ,  [2, 2, 3] ) <--- with 3 as the 3rd element, recursion reached base case and returned, continue the for loop with 3 as the 2nd element
# dfs( 2 ,  [2, 3] ) <--- num < cur[-1], so it won't go to dfs(0, [2, 3, 2]), it would continue the for loop with  3 as the 1st element
# dfs( 4 ,  [3] )
# dfs( 1 ,  [3, 3] ) <--- num > remain, break, continue the for loop with 6 as the 1st element
# dfs( 1 ,  [6] ) <--- num > remain, break, continue the for loop with 7 as the 1st element
# dfs( 0 ,  [7] ) <--- reached base case directly and added to res


# DP solution
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        dp = [[] for _ in range(target+1)]
        for t in range(1, target+1):  #dp[t] saves all combinations have t sum
            for i in candidates:
                if i > t: break   #from now on, all sum > t, break out
                if i == t: dp[t].append([i]); break  #the element value equals to current target t
                #to ensure no duplicate, the later coming item should be strictly greater than previous ones, make the result a asc sequence. 
                dp[t].extend(path + [i] for path in dp[t-i] if i >= path[-1])
        return dp[-1]


# 11.29 复习自己写。自己画完decision tree以后写出来了。但是经历了一点点曲折一开始我想for i in range然后把2个recursion放在for loop里这样不work的。
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, target, path):
            if target == 0:
                res.append(path[:])
                return
            if i >= len(candidates) or target < 0:
                return
            
            backtrack(i, target - candidates[i], path + [candidates[i]])
            backtrack(i + 1, target, path)
        
        backtrack(0, target, [])
        return res