from typing import List
from collections import defaultdict

# 1.15 first try。自己思路是清晰的但是50分钟了写不出来，一开始用BFS写但是考虑到nei的res要return给原cell就换成了DFS，但是又无法靠visited解决path问题
# 可能这题是BFS + DFS的结合？就是既要用到queue又要用到recursion的？
# 想了一会儿为什么这个不work。因为这个dfs的base case本质上只有右上左下两个cell，所以return回去代表所有cell都必须经由这两个cell入海才行
# 但是实际情况，一个cell可以不用能够流到这两个cell其中之一，经由分别两条路线入海也是可以的，而不是一定要经由这两个能同时access两个大洋的cell
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # check from border cells and go inside
        # left and top border cells need to have path go right or down and vice versa

        # how to define a cell water can flow into both oceans?
        # touches border means flowing into ocean
        # condition 1: any of the 4 nei of a cell that satisfies: 1) height <= cell h 2) it's already marked ok, then cell is ok
        # condition 2: BFS need to find (-1, x) or (x, -1) and (max_r, x) or (x, max_c)
        # condition 3: all 4 nei of a cell that satisfies: 1) height <= cell h 2) it's already marked ok, then cell is ok
        # BFS function returns true (add to ok) if condition 1 or condition 2 is satisfied, else return false and add to not_ok

        max_r, max_c = len(heights), len(heights[0])
        MOVE = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ok = set()
        not_ok = set()
        visited = set()

        def dfs(r, c) -> bool:
            if (r, c) in not_ok:
                return False
            if (r, c) in ok:
                return True
            visited.add((r, c))
            if (r == 0 and c == max_c - 1) or (r == max_r - 1 and c == 0):
                ok.add((r, c))
                return True
            neihgbors = set()
            for m_r, m_c in MOVE:
                new_r, new_c = r + m_r, c + m_c
                if (0 <= new_r < max_r and 0 <= new_c < max_c and
                    (new_r, new_c) not in visited and
                    heights[new_r][new_c] <= heights[r][c]):
                    neihgbors.add((new_r, new_c))
            if not neihgbors:
                not_ok.add((r, c))
                return False
            return any([dfs(nei_r, nei_c) for nei_r, nei_c in neihgbors])
        
        for r in range(max_r):
            for c in range(max_c):
                dfs(r, c)
            
        return list(ok)


# neetcode用了两个set来记录有access的cells然后check double existence。。。
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res

# 自己头铁硬是想写DFS。这个真的almost work。但是！唯一的例外是！
# 如果有在border上的cell会直接被判定只能access一个ocean，因为他们是base case
# 但是他们其实有可能也能access both ocean的。
# 如何解决这个问题是个麻烦
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        max_r, max_c = len(heights), len(heights[0])
        MOVE = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit = defaultdict(str)

        def dfs(r, c) -> bool:
            # base case
            if (r, c) in visit:
                return visit[(r, c)]
            if (r, c) == (0, max_c - 1) or (r, c) == (max_r - 1, 0):
                visit[(r, c)] = 'all'
                return 'all'
            if r == 0 or c == 0:
                visit[(r, c)] = 'pac'
                return 'pac'
            if r == max_r - 1 or c == max_c - 1:
                visit[(r, c)] = 'atl'
                return 'atl'

            nei_res = []
            for m_r, m_c in MOVE:
                new_r, new_c = r + m_r, c + m_c
                if (0 <= new_r < max_r and 0 <= new_c < max_c and
                    heights[new_r][new_c] <= heights[r][c] and 
                    visit[(r, c)] != 'none'):
                    nei_res.append(dfs(new_r, new_c))
            if not nei_res:
                visit[(r, c)] = 'none'
                return 'none'
            if 'all' in nei_res or ('pac' in nei_res and 'atl' in nei_res):
                visit[(r, c)] = 'all'
                return 'all'
            elif all(res == 'atl' for res in nei_res):
                visit[(r, c)] = 'atl'
                return 'atl'
            else:
                visit[(r, c)] = 'pac'
                return 'pac'
        
        for r in range(max_r):
            for c in range(max_c):
                dfs(r, c)
            
        return [k for k, v in visit.items() if v == 'all']

# 贼心不死还想试，结果test case能过但是submit第6个跑不过
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # valid neighbor definition: 1) within boundary, 2) height of it <= cur cell height
        # for all the valid neighbors, run dfs on them, if the recursion returning result satisfies any of below
        # 1) one of the valid neighbors has access to both ocean
        # 2) in the neighbors, some can access atl and some can access pacific
        # then cur cell can access both ocean

        max_r, max_c = len(heights), len(heights[0])
        MOVE = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit = defaultdict(str)

        def dfs(r, c) -> bool:
            # base case
            if (r, c) in visit:
                return visit[(r, c)]
            if (r, c) == (0, max_c - 1) or (r, c) == (max_r - 1, 0):
                visit[(r, c)] = 'all'
                return 'all'
            if r == 0 or c == 0:
                visit[(r, c)] = 'pac'
                return 'pac'
            if r == max_r - 1 or c == max_c - 1:
                visit[(r, c)] = 'atl'
                return 'atl'

            nei_res = []
            for m_r, m_c in MOVE:
                new_r, new_c = r + m_r, c + m_c
                if (0 <= new_r < max_r and 0 <= new_c < max_c and
                    heights[new_r][new_c] <= heights[r][c] and 
                    visit[(r, c)] != 'none'):
                    nei_res.append(dfs(new_r, new_c))
            if not nei_res:
                visit[(r, c)] = 'none'
                return 'none'
            if 'all' in nei_res or ('pac' in nei_res and 'atl' in nei_res):
                visit[(r, c)] = 'all'
                return 'all'
            elif all(res == 'atl' for res in nei_res):
                visit[(r, c)] = 'atl'
                return 'atl'
            else:
                visit[(r, c)] = 'pac'
                return 'pac'
        
        for r in range(max_r):
            for c in range(max_c):
                dfs(r, c)
        
        # b/c we used cells on the border as base case, so they were never be able to be 'all'.
        # now we need to check again to correct their result
        res = [k for k, v in visit.items() if v == 'all']
        new_res = set()
        for r, c in res:
            for m_r, m_c in MOVE:
                new_r, new_c = r + m_r, c + m_c
                if (0 <= new_r < max_r and 0 <= new_c < max_c and
                    heights[new_r][new_c] >= heights[r][c] and
                    (new_r in (0, max_r - 1) or new_c in (0, max_c - 1))):
                    new_res.add((new_r, new_c))
        return res + list(new_res)

# 最后放弃了按neetcode的思路写了一遍
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        MOVE = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        atl, pac = set(), set()
        res = []

        def dfs(r, c, visit, prev_h):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visit or heights[r][c] < prev_h:
                return
            visit.add((r, c))
            for m_r, m_c in MOVE:
                n_r, n_c = r + m_r, c + m_c
                dfs(n_r, n_c, visit, heights[r][c])
        
        for col in range(COLS):
            dfs(0, col, pac, heights[0][col])
            dfs(ROWS - 1, col, atl, heights[ROWS - 1][col])
        for row in range(ROWS):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, COLS - 1, atl, heights[row][COLS - 1])
            
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])
        return res