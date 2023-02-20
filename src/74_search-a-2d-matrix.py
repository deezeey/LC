from typing import List

# 12.13 first try，不难，只不过需要知道matrix转换index的trick而已
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = (l + r) // 2
            ri, ci = mid // n, mid % n
            if matrix[ri][ci] == target:
                return True
            if matrix[ri][ci] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

# 1.5 复习自己写
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        
        while l <= r:
            mid = (l + r) // 2
            cur = matrix[mid // n][mid % n]
            if cur == target:
                return True
            elif cur < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False