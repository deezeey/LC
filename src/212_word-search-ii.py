from typing import List
from collections import defaultdict

# 1.25 first try自己用图+backtracking的方法能过53/64 cases
# 看了解好像用hashmapT也非常不理想
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # dfs backtracking
        # there can be multiple starting point for the same c
        # from each c, run 4 way dfs, if any returns true, return True, if none returns true, go to next c in for loop
        mapper = defaultdict(set)
        res = set()
        ROWS, COLS = len(board), len(board[0])
        move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for r in range(ROWS):
            for c in range(COLS):
                char = board[r][c]
                mapper[char].add((r, c))

        def dfs(r, c, j, used, w):
            for m_r, m_c in move:
                n_r, n_c = r + m_r, c + m_c
                if (0 <= n_r < ROWS and 0 <= n_c < COLS and 
                j < len(w) and
                board[n_r][n_c] == w[j] and
                (n_r, n_c) not in used):
                    if j == len(w) - 1:
                        return True
                    used.add((n_r, n_c))
                    return dfs(n_r, n_c, j + 1, used, w)
            return False
                
        for word in words:
            first_c = word[0]
            if first_c in mapper:
                if len(word) == 1:
                    res.add(word)
                for row, col in mapper[first_c]:
                    used = set()
                    used.add((row, col))
                    if dfs(row, col, 1, used, word):
                        res.add(word)
        return list(res)

# 正解应该用trie，leetcode官方解如下
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word
        
        rowNum, colNum = len(board), len(board[0])
        matchedWords = []
        
        def backtracking(row, col, parent):    
            
            letter = board[row][col]
            currNode = parent[letter]
            
            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)
            
            # Before the EXPLORATION, mark the cell as visited 
            board[row][col] = '#'
            
            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset     
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)
        
            # End of EXPLORATION, we restore the cell
            board[row][col] = letter
        
            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)
        
        return matchedWords 

# 自己半背半抄写了一遍，反正就这样吧，我觉得我下次肯定也还写不出来这个好难写
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        trie_root = {}
        res = []

        # build trie
        for w in words:
            cur = trie_root
            for c in w:
                cur = cur.setdefault(c, {})
            cur["end"] = True
        
        # backtracking func
        def backtrack(r, c, node, prefix):
            char = board[r][c]
            parent = node #要先把parent node记下来方便后面pruning
            if char in node:
                node = node[char]
                board[r][c] = "#"  # 这一行的作用相当于记录visit了
                if "end" in node:
                    res.append(prefix + char)
                    del node["end"] # 这个代表这个词已经check过了，这样如果board里面有两个相同的词的话答案不会重复记录
                for mr, mc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + mr, c + mc
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        backtrack(nr, nc, node, prefix + char)
                board[r][c] = char # recursion 返回以后要把“#”改回去
                if not node: # recursively pruning leaf nodes，没有这个步骤会在63TLE
                    parent.pop(char)

        # run backtracking on all cells:
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in trie_root:
                    backtrack(r, c, trie_root, "")
        
        return res