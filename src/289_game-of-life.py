from typing import List
from collections import Counter
# 2.21 first try自己大概40分钟写出来的3 pass。感觉不是很优但是跑出来数据还可以
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # live_nei < 2, live -> die
        # live_nei > 3, live -> die
        # live_nei in (2, 3), live ->live
        # live_nei != 3, dead -> dead
        # live_nei == 3, dead -> live

        # if dead we only need to consider live_nei == 3, if so, it came alive, if not, it dies
        # if live we need to check if live_nei in (2, 3), if so, do not change, if not, it dies

        # update the cells to be (0/1, 0/1) where first num is original state of live/death, 2nd is switching state or not
        # 2nd pass we update the matrix back accoring to 2nd num
        
        # iterate thru all the cells to get live nei counts
        # update cell val according to live nei counts
        # iterate thru the cells again to set new cell vals
        ROWS, COLS = len(board), len(board[0])
        def count_live_neis(row, col):
            moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
            res = 0
            for m_r, m_c in moves:
                new_r, new_c = row + m_r, col + m_c
                if not 0 <= new_r < ROWS or not 0 <= new_c < COLS or board[new_r][new_c][0] == 0:
                    continue
                else:
                    res += 1
            return res

        for r in range(ROWS):
            for c in range(COLS):
                board[r][c] = [board[r][c], 0]

        for r in range(ROWS):
            for c in range(COLS):
                neis = count_live_neis(r, c)
                if (board[r][c][0] == 0 and neis == 3) or (board[r][c][0] == 1 and (neis < 2 or neis > 3)): #一开始漏掉了neis<2 or neis >3的括号找了半天bug
                    board[r][c][1] = 1
                else:
                    continue

        for r in range(ROWS):
            for c in range(COLS):        
                if board[r][c][1] == 1:
                    board[r][c] = int(not board[r][c][0])
                else:
                    board[r][c] = board[r][c][0]


# 正解是1变0了，就暂时放一个-1进去，表示原来是1，但是negative了所以现在死了
# 0变1了，就放个2进去，magnitue != 1表示原来是死的，positive表示现在活了

# follow up如果matrix是inifinte的话你怎么优化
# If we have an extremely sparse matrix, it would make much more sense to actually save the location of only the live cells and then apply the 4 rules accordingly using only these live cells.
def gameOfLifeInfinite(self, live):
    ctr = Counter((I, J)
                              for i, j in live
                              for I in range(i-1, i+2)
                              for J in range(j-1, j+2)
                              if I != i or J != j)
    return {ij
            for ij in ctr
            if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}

def gameOfLife(self, board):
    live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
    live = self.gameOfLifeInfinite(live)
    for i, row in enumerate(board):
        for j in range(len(row)):
            row[j] = int((i, j) in live)