from typing import List
from collections import deque

# 1.15 first try和200 number of islands几乎一样，15分钟写出来了
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_r, max_c = len(grid), len(grid[0])
        MOVE = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        max_area = 0

        for r in range(max_r):
            for c in range(max_c):
                if (r, c) in visited or grid[r][c] == 0:
                    continue
                q = deque()
                q.append((r, c))
                area = 0
                while q:
                   cur_r, cur_c = q.popleft()
                   if (cur_r, cur_c) in visited:
                       continue
                   visited.add((cur_r, cur_c))
                   area += 1
                   for m_r, m_c in MOVE:
                       new_r, new_c = cur_r + m_r, cur_c + m_c
                       if (0 <= new_r < max_r and 0 <= new_c < max_c and
                            grid[new_r][new_c] == 1 and
                            (new_r, new_c) not in visited):
                            q.append((new_r, new_c))
                max_area = max(max_area, area)
        
        return max_area

# neetcode用的dfs，代码更简洁但TM不好。应该是call stack占用了额外的资源
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area