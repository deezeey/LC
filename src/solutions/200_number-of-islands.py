from collections import deque
from typing import List

# 10.05 first try, 自己没想出来解法，看了neet code的bfs尝试自己代码实现
# test case可以跑过但是submit之后遇到[["1","1","1"],["0","1","0"],["1","1","1"]] 这个case我的res return了2，实际应该是1
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque() # <--- 问题出在这里，queue应在bfs func 内部被instantiate

        def bfs(r, c):
            while queue:
                r, c = queue.popleft()
                visited.add((r, c))
                for rd, cd in directions:
                    r += rd
                    c += cd
                    if ((r < rows and r >= 0) and
                    (c < cols and c >= 0) and
                    grid[r][c] == "1" and
                    (r, c) not in visited):
                        queue.append((r, c))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    queue.append((row, col))
                    bfs(row, col)
                    islands += 1

        return islands


# 又改进了一下代码，遇到[["1","1","1"],["0","1","0"],["1","1","1"]] 这个case我的res 还是return了2，因为在bfs(2,1)时无论怎样访问不到(2,0)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            queue = deque()
            visited.add((r, c))
            queue.append((r, c))
            while queue:
                r, c = queue.popleft()  # <--- 应该改成 row， col = queue.popleft()

                for rd, cd in directions:
                    r += rd  # <---- 一开始对比neet code代码觉得一模一样实在想不通怎么回事，最后终于发现
                    c += cd  # <---- 这里是修改了r, c的值，其实这里应该写 r = row + rd， c = row + cd
                    if ((r in range(rows)) and
                    (c in range(cols)) and
                    grid[r][c] == "1" and
                    (r, c) not in visited):
                        visited.add((r, c))
                        queue.append((r, c))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1

        return islands


# neet code代码
class SolutionBFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited=set()
        islands=0

        def bfs(r,c):
             q = deque()
             visited.add((r,c))
             q.append((r,c))
           
             while q:
                 row,col = q.popleft()
                 directions= [[1,0],[-1,0],[0,1],[0,-1]]
               
                 for dr,dc in directions:
                     r,c = row + dr, col + dc
                     if (r) in range(rows) and (c) in range(cols) and grid[r][c] == '1' and (r ,c) not in visited:
                       
                         q.append((r , c ))
                         visited.add((r, c ))

        for r in range(rows):
             for c in range(cols):
               
                 if grid[r][c] == "1" and (r,c) not in visited:
                     bfs(r,c)
                     islands +=1 

        return islands

# 11.20 复习自己写，这个能pass 37 out of 49 cases
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if any of the neighbors on its 4 dirs is 1, the same island expands
        # if all the neighbors are either 0 or are in visited or out of boundary, we conclude the island

        max_row, max_col = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0
        visited = []  # <--- visited 用set可以节省空间
        land_q = []
        
        for row in range(max_row):
            for col in range(max_col):
                if (row, col) not in visited and grid[row][col] == "1":
                    land_q.append((row, col))
                    # print("new land:", (row, col))
                    # print("concluded land:", visited)
                    while land_q:
                        row, col = land_q.pop(0)
                        visited.append((row, col))
                        for dir in dirs:
                            new_row, new_col = row + dir[0], col + dir[1]
                            if (new_row < 0 or new_row >= max_row or new_col < 0 or new_col >= max_col or
                                (new_row, new_col) in visited or 
                                grid[new_row][new_col] == "0"
                                ):
                                continue
                            else:
                                land_q.append((new_row, new_col))
                    res += 1

        return res

# 改进了一下还是只能pass 37 cases
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if any of the neighbors on its 4 dirs is 1, the same island expands
        # if all the neighbors are either 0 or are in visited or out of boundary, we conclude the island

        max_row, max_col = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0
        visited = set()
        
        for row in range(max_row):
            for col in range(max_col):
                if (row, col) not in visited and grid[row][col] == "1":
                    land_q = [(row, col)]
                    visited.add((row, col))
                    print("new land:", (row, col))
                    print("concluded land:", visited)
                    while land_q:
                        row, col = land_q.pop(0)
                        for dir in dirs:
                            new_row, new_col = row + dir[0], col + dir[1]
                            if (new_row in range(max_row) and new_col in range(max_col) and
                                (new_row, new_col) not in visited and
                                grid[new_row][new_col] == "1"
                                ):
                                land_q.append((new_row, new_col))
                                visited.add((new_row, new_col))
                    res += 1

        return res


# 我真的是不明白为什么把bfs function body写在两个for loop里面就跑不过第37个case但是单独写成function再call就可以
# 因为双重for loop里用了r,c就不可以再在while batch里用r, c了！！！
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited=set()
        islands=0

        # def bfs(r,c):
        #      q = deque()
        #      visited.add((r,c))
        #      q.append((r,c))
           
        #      while q:
        #          row,col = q.popleft()
        #          directions= [[1,0],[-1,0],[0,1],[0,-1]]
               
        #          for dr,dc in directions:
        #              r,c = row + dr, col + dc
        #              if (r) in range(rows) and (c) in range(cols) and 
        #              grid[r][c] == '1' and 
        #              (r ,c) not in visited:
                       
        #                  q.append((r , c ))
        #                  visited.add((r, c ))

        for r in range(rows):
            for c in range(cols):
               
                if grid[r][c] == "1" and (r,c) not in visited:
                    #  bfs(r,c)
                    q = deque()
                    visited.add((r,c))
                    q.append((r,c))
                
                    while q:
                        row,col = q.popleft()
                        directions= [[1,0],[-1,0],[0,1],[0,-1]]
                    
                        for dr,dc in directions:
                            r,c = row + dr, col + dc
                            if ((r) in range(rows) and (c) in range(cols) and 
                            grid[r][c] == '1' and 
                            (r ,c) not in visited):
                            
                                q.append((r , c ))
                                visited.add((r, c ))
                    islands +=1 

        return islands



# dfs version
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != "1":
                return
            grid[r][c] = "#"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
                
        return count

# 1.12 复习还是跑不过第37个case
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r_max, c_max = len(grid), len(grid[0])
        visited = set()
        res = 0
        batch = deque()
        for r in range(r_max): 
            for c in range(c_max):
                # 双重for loop里用了r,c就不可以再在while batch里用r, c了！！！
                if grid[r][c] == "0" or (r, c) in visited:
                    continue
                batch.append((r, c))
                res += 1
                while batch:
                    r, c = batch.popleft()
                    visited.add((r, c))
                    for mr, mc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr, nc = r + mr, c + mc
                        if (not 0 <= nr < r_max or not 0 <= nc < c_max or
                            (nr, nc) in visited or
                            grid[nr][nc] == "0"):
                            continue
                        batch.append((nr, nc))
        return res

# 37 case到底有啥问题!!
# 看 pic dir里面的200bug，我把res+=1之前的每个(r,c)都用红圈圈圈起来，这些是我找到的岛。
# 蓝色圈圈的岛都没被我的res找到。比如index（1，13)这块land， 当我在for r in r_max：for c in c_max的双重for loop里print (r,c）时，这个cell从未出现过。这不合常理。
# 检查了半天发现。因为 双重for loop里用了r c 变量，在while batch loop里被修改了。重名变量导致了双重for loop无法完整iterate thru所有cells。
[["1","0","0","1","1","1","0","1","1","0","0","0","0","0","0","0","0","0","0","0"],
 ["1","0","0","1","1","0","0","1","0","0","0","1","0","1","0","1","0","0","1","0"],
 ["0","0","0","1","1","1","1","0","1","0","1","1","0","0","0","0","1","0","1","0"],
 ["0","0","0","1","1","0","0","1","0","0","0","1","1","1","0","0","1","0","0","1"],
 ["0","0","0","0","0","0","0","1","1","1","0","0","0","0","0","0","0","0","0","0"],
 ["1","0","0","0","0","1","0","1","0","1","1","0","0","0","0","0","0","1","0","1"],
 ["0","0","0","1","0","0","0","1","0","1","0","1","0","1","0","1","0","1","0","1"],
 ["0","0","0","1","0","1","0","0","1","1","0","1","0","1","1","0","1","1","1","0"],
 ["0","0","0","0","1","0","0","1","1","0","0","0","0","1","0","0","0","1","0","1"],
 ["0","0","1","0","0","1","0","0","0","0","0","1","0","0","1","0","0","0","1","0"],
 ["1","0","0","1","0","0","0","0","0","0","0","1","0","0","1","0","1","0","1","0"],
 ["0","1","0","0","0","1","0","1","0","1","1","0","1","1","1","0","1","1","0","0"],
 ["1","1","0","1","0","0","0","0","1","0","0","0","0","0","0","1","0","0","0","1"],
 ["0","1","0","0","1","1","1","0","0","0","1","1","1","1","1","0","1","0","0","0"],
 ["0","0","1","1","1","0","0","0","1","1","0","0","0","1","0","1","0","0","0","0"],
 ["1","0","0","1","0","1","0","0","0","0","1","0","0","0","1","0","1","0","1","1"],
 ["1","0","1","0","0","0","0","0","0","1","0","0","0","1","0","1","0","0","0","0"],
 ["0","1","1","0","0","0","1","1","1","0","1","0","1","0","1","1","1","1","0","0"],
 ["0","1","0","0","0","0","1","1","0","0","1","0","1","0","0","1","0","0","1","1"],
 ["0","0","0","0","0","0","1","1","1","1","0","1","0","0","0","1","1","0","0","0"]]

# 改完可以通过37但会在39 TLE
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r_max, c_max = len(grid), len(grid[0])
        visited = set()
        res = 0
        for row in range(r_max):
            for col in range(c_max):
                if grid[row][col] == "1" and (row, col) not in visited:
                    batch = deque()
                    batch.append((row, col))
                    res += 1
                    while batch:
                        r, c = batch.popleft()
                        visited.add((r, c))
                        for mr, mc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = r + mr, c + mc
                            if (not 0 <= nr < r_max or not 0 <= nc < c_max or
                                (nr, nc) in visited or
                                grid[nr][nc] == "0"):
                                continue
                            batch.append((nr, nc))
                            visited.add((nr, nc)) # 没有这行会TLE
        return res