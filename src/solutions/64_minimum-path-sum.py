from typing import List
from functools import lru_cache

# 3.8 first try自己写出来了DFS + memoization
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # top left + bottom right is a constant, we just need to consider the cells on the path
        # we have to iterate thru all cells at least onces to get all possible sums
        # if we can only move down or right, it means we can't go back so we do not need visited set
        # possibly DFS + memoization?
        # res of a cell is cell val + min(res of its 2 neis)
        ROWS, COLS = len(grid), len(grid[0])
        if ROWS == 1 or COLS == 1:
            return sum([sum(row) for row in grid])

        dirs = [(0, 1), (1, 0)]
        @lru_cache(maxsize=None)
        def _minPathToBottomRight(r, c):
            if r == ROWS - 1 and c == COLS - 1:
                return grid[r][c]
            res = []
            for m_r, m_c in dirs:
                new_r, new_c = r + m_r, c + m_c
                if 0 <= new_r < ROWS and 0 <= new_c < COLS:
                    res.append(_minPathToBottomRight(new_r, new_c))
            return grid[r][c] + min(res)
        
        return _minPathToBottomRight(0, 0)

# 想了想inplace 的2D DP其实更好。
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if r == ROWS - 1 and c == COLS - 1:
                    continue
                if r == ROWS - 1:
                    grid[r][c] = grid[r][c] + grid[r][c + 1]
                elif c == COLS - 1:
                    grid[r][c] = grid[r][c] + grid[r + 1][c]
                else:
                    grid[r][c] = grid[r][c] + min(grid[r][c + 1], grid[r + 1][c])

        return grid[0][0]