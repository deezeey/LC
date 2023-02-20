# 10.10 first try 自己没什么思路，看了neet code后自己写的能submit成功
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        dp = {}
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row == m - 1 and col == n - 1:
                    dp[(row, col)] = 1
                else:
                    dp[(row, col)] = dp.get((row + 1, col), 0) + dp.get((row, col + 1), 0)

        return dp[(0, 0)]


#neetcode的写法。他这个相当于把matrix flip了所以最后return的是row[0]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]


# 11.27 复习自己写，比neet code多用一点点memory
# T O(m*n) M O(m*n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                res[row][col] = res[row - 1][col] + res[row][col - 1]
        
        return res[m-1][n-1]