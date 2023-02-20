from typing import List
# 1.26 first try题都看不懂
# 先要明白queen怎样可以attack，queen可以走8方向，上下左右和斜着走都可以
# 很容易想到她们得在不同的row和col上，然后她们还得在不同的positive和negative的diagnal上
# 有个判定diagnal的trick，只要 r - c = same constant,这两个cell就在同一个negative diagnal上，然后只要 r + c = same constant就在同一个positive diagnal上
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # r + c
        negDiag = set() # r - c
        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                # board needs to be processed so that each row is string instead of array
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in col or r + c in posDiag or r - c in negDiag:
                    continue
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                backtrack(r + 1) # place the next row's queen
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)
        return res

