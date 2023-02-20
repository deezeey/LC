from typing import List
from collections import deque

# 1.25 first try， 12分钟写出来了，好像挺简单？
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # turning col to row in reverse order
        ROWS, COLS = len(matrix), len(matrix[0])
        ordered = deque()

        for c in range(COLS):
            for r in range(ROWS)[::-1]:
                ordered.append(matrix[r][c])

        for r in range(ROWS):
            for c in range(COLS):
                matrix[r][c] = ordered.popleft()

        return matrix

# 正解是一个想到头大的 in place rotation， 
# trick是先存第一个cell的值，然后不要吧第一个cell存第二个cell，而是从最后一个往第一个空的cell倒着填，这样只用存一个temp var
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l): # 这一行为什么是range(r - l)至关重要, i是一个step数
                t, b = l, r
                topleft = matrix[t][l + i]
                # bot left to top left
                matrix[t][l + i] = matrix[b - i][l]
                # bot right to bot left
                matrix[b - i][l] = matrix[b][r - i]
                # top right to bot right
                matrix[b][r - i] = matrix[t + i][r]
                # top left to top right
                matrix[t + i][r] = topleft
            l += 1
            r -= 1
        return matrix