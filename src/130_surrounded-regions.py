from typing import List
from collections import deque
# 1.24 first try，可能状态不对思路不清晰，没写出来，感觉逻辑乱七八糟的
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # if X add to visited, if O and by boundary add to bad
        # if O and not by boundary, add to q, visited and run BFS
        # BFS check 4 neis, if X, add to visited, if O and not in bad, add to q and visited, if in bad, mark entire region is invalid and do not add to q
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        o_outlet = set()

        for r in (0, ROWS-1):
            for c in (0, COLS-1):
                if board[r][c] == "0":
                    o_outlet.add((r, c))
                else:
                    visited.add((r, c))

        for r in range(1, ROWS-1):
            for c in range(1, COLS-1):
                if board[r][c] in visited:
                    continue
                elif board[r][c] == "O" and (r, c) not in o_outlet:
                    q = deque()
                    region = set()
                    can_flip = True
                    q.append((r, c))
                    visited.add((r, c))
                    while q:
                        row, col = q.popleft()
                        region.add((row, col))
                        for m_r, m_c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            nu_row, nu_col = row + m_r, col + m_c
                            if nu_row < 0 or nu_row >= ROWS or nu_col < 0 or nu_col >= COLS:
                                continue
                            if (nu_row, nu_col) in o_outlet:
                                can_flip = False
                                continue
                            if (nu_row, nu_col) not in visited:
                                if (nu_row, nu_col) not in o_outlet:
                                    visited.add((nu_row, nu_col))
                                if board[nu_row][nu_col] == "O":
                                    q.append((nu_row, nu_col))
                    if can_flip:
                        for row, col in region:
                            board[row][col] = "X"
                elif board[r][c] == "X":
                    visited.add((r, c))

        return board

# neetcode 解法非常简单, 3pass
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # start from the boundaries, run DFS, mark all the connected Os to Hs
        # mark all the rest Os as Xs
        # mark all the Hs back to Os
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "H"
            for m_r, m_c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + m_r, c + m_c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in (0, ROWS-1) or c in (0, COLS-1)):
                    dfs(r, c)
        
        for r in range(1, ROWS-1):
            for c in range(1, COLS-1):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "H":
                    board[r][c] = "O"
        
        return board