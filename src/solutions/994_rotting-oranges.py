from typing import List
from collections import deque


# 10.05 first try，我自己写出来了！！虽然用了比较长时间，可能50分钟。。。但是我写出来了！可能因为刚刚做了200 number of islands所以BFS比较熟
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rotten = set()
        fresh_count = 0
        infected = set()

        # go thru each cell to find the position of 2s, and these will become our starting points, count the 1s
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh_count += 1
                if grid[row][col] == 2:
                    rotten.add((row, col))
        
        # infect the fresh ones using a bfs function, count the loop
        def bfs(batch: List[tuple]):
            queue = deque()
            queue.append(batch)
            nonlocal minutes
            while queue:
                batch = queue.popleft()
                next_batch = set()
                infected.update(batch)
                for row, col in batch:
                    for dr, dc in directions:
                        r, c = row + dr, col + dc
                        if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in infected:
                            infected.add((r, c))
                            next_batch.add((r, c))
                if next_batch:
                    queue.append(next_batch)
                    minutes += 1

        bfs(rotten)

        # check if all fresh ones were infected
        return minutes if len(infected - rotten) == fresh_count else -1


# neet code的BFS, 思路一样但他写的更加简洁
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c)) # <--- 到这一步为止和我做的事儿都一样，只是他直接把rotten等同于queue了

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):  # <--- 假如初始值有3个烂橙子我们要保证3个都被pop出来
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # if in bounds and nonrotten, make rotten
                    # and add to q
                    if (
                        row in range(ROWS)
                        and col in range(COLS)
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2  # <--- 他直接改原grid而没有记录infected cells
                        q.append((row, col))
                        fresh -= 1 # <--- 他直接令fresh -= 1而没有比较fresh和infected
            time += 1
        return time if fresh == 0 else -1


# 11.20 复习自己写
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 1）find all rotten oranges
        # 2) using bfs to infect the fresh oranges and count the min
        # 3) compare count of fresh oranges with initial count after mission complete

        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        rotten_cells = []
        fresh_count = 0
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten_cells.append((r, c))
                if grid[r][c] == 1:
                    fresh_count += 1

        while rotten_cells and fresh_count:
            for _ in range(len(rotten_cells)):
                r, c = rotten_cells.pop(0)
                for dir in DIRS:
                    new_r, new_c = r + dir[0], c + dir[1]
                    if (0 <= new_r < ROWS and 0 <= new_c < COLS and
                        grid[new_r][new_c] == 1):
                        grid[new_r][new_c] = 2
                        fresh_count -= 1
                        rotten_cells.append((new_r, new_c))
            time += 1

        return time if fresh_count == 0 else -1

# 1.13 复习20分钟写好了
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        max_r, max_c = len(grid), len(grid[0])
        move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time = -1
        q = deque()
        visited = set()
        fresh = 0

        # find all the 2s as starting points
        for row in range(max_r):
            for col in range(max_c):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append((row, col))
                    visited.add((row, col))
        if not fresh:
            return 0

        # start to count the time and rotting the 1s
        while q:
            time += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for mr, mc in move:
                    nr = r + mr
                    nc = c + mc
                    if (0 <= nr < max_r and 0 <= nc < max_c and 
                        grid[nr][nc] == 1 and 
                        (nr, nc) not in visited):
                        fresh -= 1
                        q.append((nr, nc))
                    visited.add((nr, nc))
        
        return time if not fresh else -1