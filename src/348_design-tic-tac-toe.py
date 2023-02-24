from collections import defaultdict

# 2.22 first try这题好像不是很难，官方最优解也是这个思路
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.sum_hash = defaultdict(int)

    def move(self, row: int, col: int, player: int) -> int:
        val = -1 if player == 1 else 1
        n = self.n
        if row == col: # neg diag
            self.sum_hash["neg_diag"] += val
            if abs(self.sum_hash["neg_diag"]) == n: return player
        if row + col == n - 1: # pos diag
            self.sum_hash["pos_diag"] += val
            if abs(self.sum_hash["pos_diag"]) == n: return player
        row_key, col_key = "row" + str(row), "col" + str(col)
        self.sum_hash[row_key] += val
        self.sum_hash[col_key] += val
        if abs(self.sum_hash[row_key]) == n or abs(self.sum_hash[col_key]) == n: return player
        return 0
        
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

# define winning state
# if after the move, we see 3 or -3 in any row, col, or diagonal
# define how to mark a cell
# -1 for player 1
# 1 for player 2

# hash map for pos_diag, neg_diag, row 0 ~ (n-1), col 0 ~ (n-1)