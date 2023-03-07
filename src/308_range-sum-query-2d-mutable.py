from typing import List
# 03.04 first try自己的思路如下comment，可以进一步优化的地方是也做一个vertical的sum，如果sumRegion是行比较多就sum列，如果是列比较多就sum行
# 这个能过但是不是正解，正解根本不想存initial matrix？
# 更近一步是存当前cell为bottom right，[0][0]为top left的prefix sum，然后用右下sum减掉右上 - 1 sum和左下 - 1 sum再把左上 - 1 sum加回来
class NumMatrix:
    # we can keep the l->r, incremental sum at each cell
    # if top left is [1, 1], bottom right is [2, 2] then row 1 sum = [1, 2] incre_sum - cell [1, 0] incre_sum, row 2 sum = cell [2, 2] - cell[2, 0]
    # updating a cell will affect all the cells rightwards, including itself
    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        self.ROWS = len(matrix)
        self.COLS = len(matrix[0])
        for r in range(self.ROWS):
            cur_sum = 0
            for c in range(self.COLS):
                cur_sum += self.mat[r][c]
                self.mat[r][c] = [self.mat[r][c], cur_sum]

    def update(self, row: int, col: int, val: int) -> None:
        prev = self.mat[row][col][0]
        change = val - prev
        self.mat[row][col][0] = val
        while col < self.COLS:
            self.mat[row][col][1] += change
            col += 1

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for r in range(row1, row2 + 1):
            to_subtract = 0 if col1 == 0 else self.mat[r][col1 - 1][1]
            res += self.mat[r][col2][1] - to_subtract
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)


# 正解是Binary Indexed Tree懒得看了，考到了就拉倒
