from typing import List
from collections import defaultdict, Counter

# 10.30 first try 自己试着写了一下，能pass 2个case但在 board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"时候fail
# 两个问题
# 1) 因为只做过遇到base case append res的题，不知道遇到certain base case如何停止全部的recursion。
# 2) 如果本cell以及周围4个cell都不是desired letter，如何move onto next recursion
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        used = []
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row_max, col_max = len(board), len(board[0])

        # if is the letter we're looking for, push to used, modify word, search 4 dirs for next letter
        # if not the letter we're looking for, search 4 dirs for the current letter until we find desired letter
        # if not the letter and none of 4 dirs is the letter we're looking for, backtrack to prev letter(pop last used letter)

        def dfs(row, col, word):
            # base case
            # print(row, col, board[row][col])
            print(used, word)
            if board[row][col] != word[0]:
                return
            if not word:
                return True

            if board[row][col] == word[0]:
                print("found letter", word[0], " at:", row, col)
                word = word[1:]
                used.append((row, col))

            for dir in dirs:
                row += dir[0]
                col += dir[1]
                print("next check", row, col)
                if (row, col) not in used and row < row_max and col < col_max:
                    dfs(row, col, word)
                    row -= dir[0]
                    col -= dir[1]

        dfs(0, 0, word)

        return len(used) == len(word)


# 看了neet code以后写的，能过test case但是submission time exceeded
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW_MAX, COL_MAX = len(board), len(board[0])
        used = set()
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(row, col, word):
            # print("next check", row, col)
            # print("new word:", word)
            # base case
            if not word:
                return True
            if ((row, col) in used or
                row < 0 or col < 0 or 
                row >= ROW_MAX or col >= COL_MAX or
                board[row][col] != word[0]):
                    return False
            else:
                # print("found letter", word[0], " at:", row, col)
                used.add((row, col))
                res = []
                for dir in dirs:
                    res.append(dfs(row + dir[0], col + dir[1], word[1:]))
                used.remove((row, col))  # <--- 一开始漏了这行，迟迟过不了，基本上意思是recursion回退上一层之后你不能标记这层的cell是用过的，否则其它路也会走不通了
                if any(res):
                    return True
                else:
                    return False

        for row in range(ROW_MAX):
            for col in range(COL_MAX):
                if dfs(row, col, word):
                    return True
        
        return False


# neet code写的，如果他没有那个prevent TLE的部分，他也会time exceeded
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (
                min(r, c) < 0
                or r >= ROWS
                or c >= COLS
                or word[i] != board[r][c]
                or (r, c) in path
            ):
                return False
            path.add((r, c))
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            path.remove((r, c))
            return res

        # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        # 解释一下上面那行，map(Counter, board)会产生一个list of counters
        # sum([<list of counters>], counter()) 是用到了sum func的第二个start parameter（第一个param是iterable这不用说)， set start to empty counter可以避免TypeError
        # 这好像是sum多个counter结果到一个counter的固定用法。如果board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], sum的结果会是Counter({'E': 3, 'A': 2, 'C': 2, 'S': 2, 'B': 1, 'F': 1, 'D': 1})
        # 然后因为word里面可能有不在board里面的字母，所以我们的counter dict可能没有word[0]或者word[-1] as key. 所以我们需要turn this counter（which is already a dict) into a default dict
        # You can construct a defaultdict from dict, by passing the dict as the second argument. first param "int" will set default value 0 when missing key is queried.
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
            
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False


# 11.29 复习自己写又是碰到第二个"SEE"的case跑不过 
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        used = set()

        # need to check if cell matches current word[i]
        # if not, backtrack
        # if is, i += 1 and check neighbors for next word[i]

        def backtrack(i, r, c):
            # if used / out of boundary /is not word[i], return bad base case
            if ((r, c) in used or r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[i]):
                return False
            # if i is the last idx of word, return good base case
            if i == len(word) - 1 and board[r][c] == word[i]:
                return True
            # if is word[i], add to used, move to next recursion
            used.add((r, c))
            for dir in dirs:
                if backtrack(i + 1, r + dir[0], c + dir[1]):
                    return True
            used.remove((r, c)) # <--- 一开始忘了这行
            return False
        
        # starting = []
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if board[r][c] == word[0]:
        #             starting.append((r, c))
        
        # for r, c in starting:
        #     if backtrack(0, r, c):
        #         return True
        #     return False

        for r in range(ROWS):  # <--- 修改成这样能pass test case
            for c in range(COLS):
                if backtrack(0, r, c):
                    return True