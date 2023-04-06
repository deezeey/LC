from typing import List

# 10.03 first try 有思路并且思路和DP的正确解法一样，但是不熟悉matrix的traverse代码实现，写不出来了
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        width, height = len(mat), len(mat[0])
        x = y = 0 # starting point (val == 0) indices
        res = [[999]*width for _ in range(height)]

        # find the starting point
        i = j = 0
        while True:
            if mat[i][j] == 0:
                res[i][j] = 0
                x, y = i, j
                break
            else:
                continue
            if i < width - 1:
                i += 1
            if j < height - 1:
                j += 1

        while x < width and y < height:
            if mat[x][y] == 0:
                res[x][y] = 0
            else:
                res[x+1][y], res[x-1][y], res[x][y-1], res[x][y+1] = res[x][y] + 1
            # 后面想不出怎么写了。。。。


# 看了同思路的九章写法尝试自己重新code一遍，跑不出报错
from collections import deque
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows, cols = len(mat), len(mat[0])
        res = [[0] * cols for row in range(rows)]
        filled_cells = deque()

        # find all cells with distance 0
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    filled_cells.append((i, j))
                else:
                    res[i][j] = -1
        
        # check & update adjacent cells starting from the 0 cells
        steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # for (i, j) in filled_cells:  # <---- 跑这一行时候报错 RuntimeError: deque mutated during iteration
        # !!!只需把上面那行改成如下while loop，所以for loop不可以修改自己使用的iterative obj，但while可以!!!
        while filled_cells:
            i, j = filled_cells.popleft()
            for step in steps:
                new_i = i + step[0]
                new_j = j + step[1]
                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue
                if res[new_i][new_j] >= 0:
                    continue
                res[new_i][new_j] = res[i][j] + 1
                filled_cells.append((new_i, new_j))
        
        return res

# 11.17 复习,还记得思路但是跑出来是错的答案。还是动手写之前自己思路没有完全理清。
# 这题是最适合用bfs做的，dfs反而不适合。因为我们找到一群起始点以后多点开花每个点只check外层一圈是最合适的
# dfs就是多个点一个点开花越开越大，这不make sense

# 九章思路：整体是一个带剪枝的BFS。每个起始点为root，4个邻居就是4个children。
# 当然children的children其中有一个肯定是当前root所以我们需要记录访问。
# 1）找到所有的起始点(即0)标记结果为0，其他所有点暂时标记结果为-1
# 2）用一个q记录所有的出发点，每次pop一个出发点，check相邻位置  <---- 自己没有想到用q做bfs而是想到dfs
# 3）如果邻居是0或者大于1即代表之前已经算过它的结果，且我们新算的结果是不可能比之前算的要小（因为从0出发的） <---- 这一步想清楚很重要，自己写的dfs每次计算都在找最小neighbor
# 4）把邻居坐标append到q，方便未来check邻居的邻居
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # if a cell is 0 then distance is 0
        # if a cell is next to a 0 then distance is 1
        # a cell's distance is its neighbor's distance + 1
        max_row, max_col = len(mat), len(mat[0])
        res = [[-1] * max_col] * max_row # <--- 这个解把这行换成下面也能跑过12/50 test cases, 最后case13还是会报错就是了
        start_row, start_col = max_row + 1, max_col + 1
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = []

        for i in range(max_row):
            for j in range(max_col):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    start_row, start_col = i, j
                else:
                    continue 

        def dfs(row, col):
            if not ( 0 <= row < max_row and 0 <= col < max_col ) or (row, col) in visited:
                return
            if mat[row][col] != 0:
                neighbors_res = []
                for dir in dirs:
                    if 0 <= row + dir[0] < max_row and 0 <= col + dir[1] < max_col:
                        neighbors_res.append(res[row + dir[0]][col + dir[1]])
                neighbors_res = filter(lambda n: n >= 0, neighbors_res)
                neighbor_min = min(neighbors_res)  #这就代表我自己的思路是没有想清楚整个遍历的顺序。从0开始渲染并且用的是bfs的话，不需要找最小neighbor。
                print(row, col, neighbor_min)
                res[row][col] = neighbor_min + 1
            visited.append((row, col))
            for dir in dirs:
                dfs(row + dir[0], col + dir[1])

        dfs(start_row, start_col)

        return res

# 按九章写了一遍不知为何跑出来还是错误的答案。 T O(n) 因为是遍历每个cell。 M也是 O(n)因为visited deque最坏情况store all the cells if everything's 0
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        max_row, max_col = len(mat), len(mat[0])
        res = [[0] * max_col] * max_row  # <---- 找了一万年为什么这个跑出来是错的，原来这样写不行必须要像下面那样写
        # res = [[0] * max_col for row in range(max_row)]
        visited = deque()

        for i in range(max_row):
            for j in range(max_col):
                if mat[i][j] == 0:
                    visited.append((i, j))
                else:
                    res[i][j] = -1 

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while visited:
            row, col = visited.popleft()
            for dir in dirs:
                new_row, new_col = row + dir[0], col + dir[1]
                if not (0 <= new_row < max_row and 0 <= new_col < max_col):
                    continue
                if res[new_row][new_col] >= 0:
                    continue
                res[new_row][new_col] = res[row][col] + 1
                visited.append((new_row, new_col))

        return res

# 1.12 复习居然还是没写出来，思路是对的但是return了[[0, 0, 0], [0, inf, 0], [0, 0, 0]]
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        res = [[float("inf")] * col for _ in range(row)]
        sr, sc = 0, 0

        # find a starting cell with val 0
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    sr, sc = r, c
                    break
        
        # update res matrix
        batch = [(sr, sc)]
        visited = []
        while batch:
            r, c = batch.pop()
            neighbor_min = float("inf")
            for mr, mc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + mr, c + mc
                if not 0 <= nr < row or not 0 <= nc < col or (nr, nc) in visited:
                    continue
                else:
                    neighbor_min = min(neighbor_min, res[nr][nc])
                    batch.append((nr, nc))
            res[r][c] = 0 if mat[r][c] == 0 else neighbor_min + 1
            visited.append((r, c))
        
        return res

# 稍微改了下能过test case但是在[[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]] return wrong answer
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        res = [[float("inf")] * col for _ in range(row)]
        sr, sc = 0, 0

        # find a starting cell with val 0
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    sr, sc = r, c
                    break
        
        # update res matrix
        batch = deque()
        batch.append((sr, sc))
        visited = set()
        while batch:
            r, c = batch.popleft()
            neighbor_min = float("inf")
            for mr, mc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + mr, c + mc
                if not 0 <= nr < row or not 0 <= nc < col:
                    continue
                else:
                    neighbor_min = min(neighbor_min, res[nr][nc])
                    if (nr, nc) not in visited:
                        batch.append((nr, nc))
            res[r][c] = 0 if mat[r][c] == 0 else neighbor_min + 1
            visited.add((r, c))
        
        return res

# 默写了一遍九章的答案。出了一个bug
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        max_r, max_c = len(mat), len(mat[0])
        res = [[0] * max_c for _ in range(max_r)]
        visited = deque()  # 为什么一定要用deque，因为我们iterate的顺序很重要一定要先处理所有0周边的cell把他们弄成1，再处理1周边的cell把他们弄成2

        for r in range(max_r):
            for c in range(max_c):
                if mat[r][c] == 0:
                    visited.append((r, c))
                else:
                    res[r][c] = -1
        
        while visited:
            r, c = visited.popleft()
            for mr, mc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + mr, c + mc
                if not 0 <= nr < max_r or not 0 <= nc < max_c:
                    continue
                if (nr, nc) in visited: # 这个会造成stack overflow因为visited会pop呀
                # 这行要改成 if res[nr][nc] >= 0
                    continue
                res[nr][nc] = res[r][c] + 1
                visited.append((nr, nc))
                
        return res