from typing import List

# 2.18 frist try自己写了一个小时才写出来。
# 就是思路清晰但是细节不清晰所以需要不停修改bug
# T O(log(n!)) M O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[ROWS - 1][COLS - 1]:
            return False
        # diagonal gives left & up boundary, first row gives right boundary, first col gives bottom boundary
        # binary search to find the first diagonal cell that's greater than target, that will be our leftmost and upmost boundary
        l, r = [0,0], [ROWS - 1, COLS - 1]
        while l <= r:
            l_r, l_c, r_r, r_c = l[0], l[1], r[0], r[1]
            if matrix[l_r][l_c] == target or matrix[r_r][r_c] == target:
                return True
            mid_r = (l_r + r_r) // 2
            mid_c = (l_c + r_c) // 2
            if matrix[mid_r][mid_c] == target:
                return True
            if matrix[mid_r][mid_c] > target:
                r = [mid_r, mid_c]
            else:
                l = [mid_r, mid_c]
            if r[0] - l[0] <= 1 and r[1] - l[1] <= 1: # 一开始写的是or，就过不了
                break
        min_r, min_c = r[0], r[1]
        max_r, max_c = ROWS, COLS # 一开始写的是 max_r, max_c = min_r + 1, min_c + 1, 后来debug出来了
        # find the right boundaries
        for row in range(min_r + 1, ROWS):
            if matrix[row][0] > target:
                max_r = row
        for col in range(min_c + 1, COLS):
            if matrix[0][col] > target:
                max_c = col
        # search for target within boundary
        for row in range(min_r, max_r):
            for col in range(COLS):
                if matrix[row][col] == target:
                    return True
        for col in range(min_c, max_c):
            for row in range(ROWS):
                if matrix[row][col] == target:
                    return True
        return False

# 这个是最简单的答案 T O(m + n) M O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        r, c = ROWS - 1, 0
        while r >= 0 and c < COLS:
            if matrix[r][c] > target:
                r -= 1
            elif matrix[r][c] < target:
                c += 1
            else:
                return True
        return False   