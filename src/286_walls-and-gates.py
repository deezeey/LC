from typing import List
from collections import deque

# 1.24 first try, 经过debug自己28min写出来了但是T不怎么好
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # find inf by the 0s and push to q
        # run bfs, each level has distance +1
        ROWS, COLS = len(rooms), len(rooms[0])
        move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        dist = 0

        def expandQ(r, c):
            for m_r, m_c in move:
                n_r, n_c = r + m_r, c + m_c
                if n_r < 0 or n_c < 0 or n_r == ROWS or n_c == COLS:
                    continue
                if rooms[n_r][n_c] == 2147483647 and (n_r, n_c) not in q: #一开始漏了(n_r, n_c) not in q
                    q.append((n_r, n_c))

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    expandQ(r, c)
        
        while q:
            dist += 1
            for _ in range(len(q)):
                row, col = q.popleft()
                rooms[row][col] = dist
                expandQ(row, col)

        return rooms

# neetcode解法和我一样分层BFS
class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def walls_and_gates(self, rooms: List[List[int]]):
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = deque()

        def addRooms(r, c):
            if (
                min(r, c) < 0
                or r == ROWS
                or c == COLS
                or (r, c) in visit
                or rooms[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRooms(r + 1, c)
                addRooms(r - 1, c)
                addRooms(r, c + 1)
                addRooms(r, c - 1)
            dist += 1