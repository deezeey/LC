from typing import List
from functools import lru_cache

# DFS + memoization
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS, COLS = len(matrix), len(matrix[0])
        res = 0
        @lru_cache(maxsize=None)
        def _getPathLenFromCell(r: int, c: int):
            path = 1
            for m_r, m_c in dirs:
                new_r, new_c = r + m_r, c + m_c
                if 0 <= new_r < ROWS and 0 <= new_c < COLS and matrix[new_r][new_c] > matrix[r][c]: 
                    # 因为是strictly increasing path，所以我们不可能走回头路，因此不需要visited来记录已走路径
                    path = max(path, _getPathLenFromCell(new_r, new_c) + 1)
            return path
        
        for row in range(ROWS):
            for col in range(COLS):
                res = max(res, _getPathLenFromCell(row, col))
        return res