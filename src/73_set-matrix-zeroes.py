from typing import List

# 1.30 first try这题好像很简单？
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        target_r, target_c = set(), set()

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    target_r.add(r)
                    target_c.add(c)

        for r in range(ROWS):
            for c in range(COLS):
                if r in target_r or c in target_c:
                    matrix[r][c] = 0
                    
        return matrix

# 看了下neetcode他也是这么写的，先找到r和c代号再重新iterate thru一遍