from typing import List

# 10.09 first try。自己的思路是对的，move in dir till the end and then shrink the corner
# 和leet code的思路一样，但是我没想好terminate operation的条件，代码还没work，累了去睡觉了
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        number_of_elements = rows * cols
        row_end, col_end = len(matrix) - 1, len(matrix[0]) - 1
        moving_dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        corners = [[0, col_end], [row_end, col_end], [row_end, 0], [1, 0]]
        dir_index = 0
        res = []

        def reachEnd(row, col, dir_index, corners):
            match dir_index:
                case 0:
                    return col == corners[0][1]
                case 1:
                    return row == corners[1][0]
                case 2:
                    return col == corners[2][1]
                case 3:
                    return row == corners[3][0]
        
        def moveCorner(dir_index, corners):
            match dir_index:
                case 0: 
                    corners[0][0] += 1
                    corners[0][1] -= 1
                case 1:
                    corners[1][0] -= 1
                    corners[1][1] -= 1
                case 2:
                    corners[2][0] -= 1
                    corners[2][0] += 1
                case 3:
                    corners[3][0] += 1
                    corners[3][1] += 1
            return corners

        row = col = 0
        for _ in range(number_of_elements): # <---- 自己写的没有想好terminate loop的条件
            while not reachEnd(row, col, dir_index, corners):
                row += moving_dir[dir_index][0]
                col += moving_dir[dir_index][1]
                print(row, col)
                res.append(matrix[row][col])
            dir_index += 1 if dir_index < 3 else 0
            corners = moveCorner(dir_index, corners)


# neetcode的解法，kinda双重双指针
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0]) # 0, 4
        t, b = 0, len(matrix) # 0, 3
        res = []

        while l < r and t < b:
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1

            for i in range(t, b):
                res.append(matrix[i][r - 1])
            r -= 1

            if not (l < r and t < b): # <--- 这个地方要特别注意，看似和while loop条件重复但是如果没有这个部分，当只剩一行或一列时候会出问题
                # 之所以把这个break放在往右和往下之后，因为往右之后t变了不会影响往下，但往下的也走完之后，t和r都变了，此时高度宽度都变了所以必须重新判断
                # 注意不要漏了逻辑判断的括号！
                break

            for i in range(r - 1, l - 1, -1):
                res.append(matrix[b - 1][i])
            b -= 1            

            for i in range(b - 1, t - 1, -1):
                res.append(matrix[i][l])
            l += 1

        return res
        

# 另一个使用stack pop的思路，这个思路后来自己通过观察example数列也想到了但是没有自己尝试写
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        while matrix:
            ret += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
            if matrix:
                ret += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret


# 11.05 复习，记得思路但是自己没写出来代码，写成了4 while loops inside 1 while loop。
# 复习自己默写的stack pop解法
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # (0,0), (0,1), (0,2), (1,2), (2,2), (2,1), (2,0), (1,0), (1,1)
        res = []

        while matrix:
            # left -> right
            res.extend(matrix.pop(0))
            # top -> bottom
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            # right -> left
            while matrix and matrix[-1]:
                res.append(matrix[-1].pop())
            if matrix:
                del matrix[-1]
            # bottom -> top
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        
        return res

# 12.13复习自己写，卡着点33分钟写出来了，但是很多off by one error改了很久
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        b, r = len(matrix) - 1, len(matrix[0]) - 1
        l, t = 0, 0
        res = []

        while l <= r and t <= b:
            for col in range(l, r + 1):
                res.append(matrix[t][col])
            t += 1
            for row in range(t, b + 1):
                res.append(matrix[row][r])
            r -= 1
            if t > b or l > r:
                break
            for col in range(r, l - 1, -1):
                res.append(matrix[b][col])
            b -= 1
            for row in range(b, t - 1, -1):
                res.append(matrix[row][l])
            l += 1
        
        return res
