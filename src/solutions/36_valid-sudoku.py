from typing import List
from collections import defaultdict

# 12.04 first try，submission failed因为我iterate thru row col的方式不对
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # sub box valid = no repetitve nums in 9 cells
        # entire grid valid = a num can't appear in the same cell in two sub boxes
        s, e = 0, 2
        cell_hash = defaultdict(set)

        while e <= 8:
            sub_box_vals = set()
            for row in range(s, e + 1):
                for col in range(s, e + 1):
                    d = board[row][col]
                    if d == ".":
                        continue
                    orig_row, orig_col = row % 3, col % 3
                    # check if sub box valid
                    if d in sub_box_vals:
                        print("sub box invalid", row, col)
                        return False
                    # check if entire grid is valid
                    if d in cell_hash[(orig_row, orig_col)]:
                        print("grid invalid at", row, col)
                        return False
                    sub_box_vals.add(d)
                    cell_hash[(orig_row, orig_col)].add(d)
                    print(cell_hash)
            s += 3
            e += 3

        return True

# 加了一个while loop这下iterate thru的方式是对的但是submission仍然fail
# [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# 我print的显示grid invalid at 6 1, 这个位置和 3, 4的6是重叠啊为啥expect true呢？
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # sub box valid = no repetitve nums in 9 cells
        # entire grid valid = a num can't appear in the same cell in two sub boxes
        row_s, row_e = 0, 2
        cell_hash = defaultdict(set)

        while row_e <= 8:
            col_s, col_e = 0, 2
            sub_box_vals = set()
            while col_e <= 8: 
                for row in range(row_s, row_e + 1):
                    for col in range(col_s, col_e + 1):
                        d = board[row][col]
                        if d == ".":
                            continue
                        orig_row, orig_col = row % 3, col % 3
                        # check if sub box valid
                        if d in sub_box_vals:
                            return False
                        # check if entire grid is valid
                        if d in cell_hash[(orig_row, orig_col)]:
                            return False
                        sub_box_vals.add(d)
                        cell_hash[(orig_row, orig_col)].add(d)
                col_s += 3
                col_e += 3
            row_s += 3
            row_e += 3

        return True


# 后来看了下solution解释发现我阅读理解没做好
# 这题只要求0-9每个row和0-9每一行没有重复数字，以及每个subbox没有重复数字。并不是说需要比较subbox的同一cell是不是出现过同一数字
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # sub box valid = no repetitve nums in 9 cells
        # row valid + col valid
        row_s, row_e = 0, 2
        row_hash = defaultdict(set)
        col_hash = defaultdict(set)

        while row_e <= 8:
            col_s, col_e = 0, 2
            while col_e <= 8:
                sub_box_vals = set()
                for row in range(row_s, row_e + 1):
                    for col in range(col_s, col_e + 1):
                        d = board[row][col]
                        if d == ".":
                            continue
                        # check if sub box valid
                        if d in sub_box_vals:
                            return False
                        # check row, col is valid
                        if d in row_hash[row] or d in col_hash[col]:
                            return False
                        sub_box_vals.add(d)
                        row_hash[row].add(d)
                        col_hash[col].add(d)
                col_s += 3
                col_e += 3
            row_s += 3
            row_e += 3

        return True


# neetcode因为一开始就看懂了题目所以写的更简洁
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # key = (r // 3, c // 3) 这个东西是square的编号，(0, 0), (0, 1)，(0, 2), (1, 0) etc..

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

# 12.08 复习
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = defaultdict(set)
        col_hash = defaultdict(set)
        cell_hash = defaultdict(set)

        for r in range(0, 9):
            for c in range(0, 9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in row_hash[r] or
                board[r][c] in col_hash[c] or
                board[r][c] in cell_hash[(r // 3, c // 3)]
                ):
                    return False
                row_hash[r].add(board[r][c])
                col_hash[c].add(board[r][c])
                cell_hash[(r // 3, c // 3)].add(board[r][c])
        
        return True

#  1.2 复习
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = [set() for _ in range(9)]
        col_hash = [set() for _ in range(9)]
        box_hash = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                box_id = (r // 3, c // 3)
                if val == ".":
                    continue
                if (val in row_hash[r] or 
                    val in col_hash[c] or
                    val in box_hash[box_id]):
                    return False
                row_hash[r].add(val)
                col_hash[c].add(val)
                box_hash[box_id].add(val)
        
        return True