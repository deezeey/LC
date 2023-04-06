from typing import List

# 9.25 自己的解，pass了但写的感觉很不elegant
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row_count = len(image)
        col_count = len(image[0])
        cur_color = image[sr][sc]
        if sr < 0 or sc < 0 or sr >= row_count or sc >= col_count or cur_color == color:
            return image
        image[sr][sc] = color
        
        if sr - 1 >= 0 and image[sr-1][sc] == cur_color:
            self.floodFill(image, sr - 1, sc, color)
        if sr + 1 < row_count and image[sr+1][sc] == cur_color:
            self.floodFill(image, sr + 1, sc, color)
        if sc - 1 >= 0 and image[sr][sc-1] == cur_color:
            self.floodFill(image, sr, sc - 1, color)
        if sc + 1 < col_count and image[sr][sc+1] == cur_color:
            self.floodFill(image, sr, sc + 1, color)
        
        return image


# 9.25 参考九章找了个优雅的写法。T O(n) M O(n) from recursion stack
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row_count = len(image)
        col_count = len(image[0])
        cur_color = image[sr][sc]
        if image[sr][sc] == color:
            return image
        
        def dfs(row, col):
            if not 0 <= row < row_count or not 0 <= col < col_count or image[row][col] != cur_color:
                return
            image[row][col] = color
            [dfs(row + x, col + y) for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]] # <--- list comprehension跑recursion有点灵性
        
        dfs(sr, sc)
        
        return image


# 11.17 复习自己写，可能今天状态不好不知道咋地没写出来。[[2,2,2],[2,2,0],[2,0,1]]是正确答案我return了[[1,1,1],[1,2,0],[1,0,2]]
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row_max, col_max = len(image), len(image[0])
        origin = image[sr][sc]

        def fillCell(row, col):
            if row < 0 or row >= row_max or col < 0 or col >= col_max or image[row][col] != origin:
                return
            image[row][col] = color
            for dir in dirs:  # <--- 问题出在这个for loop上，换成九章那样的list comprehension跑recursion就能过
                row += dir[0]  # <--- 找到问题了， 不要乱用 += 啊！！
                col += dir[1]
                fillCell(row, col)
        
        fillCell(sr, sc)
        return image


# 1.12 复习自己写，九章那样写recursion比较简短，但是我自己这个效率更高
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r_max, c_max = len(image) - 1, len(image[0]) - 1
        batch = [[sr, sc]]
        s_clr = image[sr][sc]
        visited = set() # 不需要visited也行但visited提升效率
        move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while batch:
            sr, sc = batch.pop()
            image[sr][sc] = color
            for m in move:
                mr, mc = m
                nr, nc = sr + mr, sc + mc
                if (nr < 0 or nc < 0 or nr > r_max or nc > c_max or 
                    (nr, nc) in visited or
                    image[nr][nc] != s_clr):
                    continue
                else:
                    image[nr][nc] = color
                    visited.add((nr, nc))
                    batch.append([nr, nc])
        
        return image