from typing import List
from math import floor, sqrt

# 2.22 first try，自己的解能过 46/86 cases碰到[[1,3,5],[6,7,12],[11,14,14]]挂了，应该return5，我return了6，自己没有考虑到[0,2]的数字是可能会比[1,1]大的
# 所以是不能row和col同时>=标的cell
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # square, row/col ascending, duplicates allowed
        n = len(matrix)
        if k == 1:
            return matrix[0][0]
        if k >= n ** 2:
            return matrix[n-1][n-1]
        i = floor(sqrt(k))
        k = k - i ** 2
        row_j, col_j, res = 0, 0, 0
        while k > 0:
            row_cell = matrix[i][col_j]
            col_cell = matrix[row_j][i]
            if row_cell <= col_cell:
                res = row_cell
                col_j += 1
            else:
                res = col_cell
                row_j += 1
            k -= 1
        return res

# Start the binary search with start = matrix[0][0] and end = matrix[N-1][N-1]
# Find the middle of the start and the end. This middle number is NOT necessarily an element in the matrix.
# Count all the numbers smaller than or equal to middle in the matrix. As the matrix is sorted, we can do this in O(N)O(N)O(N). Note that this is determining the size of the left-half of the array.
# While counting, we need to keep track of the smallest number greater than the middle (let’s call it R) and at the same time the biggest number less than or equal to the middle (let’s call it L). These two numbers will be used to adjust the number range for the binary search in the next iteration.
# If the count is equal to K, L will be our required number as it is the biggest number less than or equal to the middle, and is definitely present in the matrix.
# If the count is less than K, we can update start = R to search in the higher part of the matrix
# If the count is greater than K, we can update end = L to search in the lower part of the matrix in the next iteration.
# 这个别人写的解是从右上角开始count的
class Solution:
    def countSmallerThanMid(self, matrix, mid_value, num_of_rows):
        column = num_of_rows - 1
        row = 0
        count = 0
        while column >= 0 and row < num_of_rows:
            if matrix[row][column] > mid_value:
                column -= 1
            else:
                count += column + 1
                row += 1
        
        return count

    def kthSmallest(self, matrix, k):
        num_of_rows = len(matrix)
        min_value = matrix[0][0]
        max_value = matrix[-1][-1]

        while min_value < max_value:
            mid_value = min_value + int((max_value - min_value) / 2)
            if self.countSmallerThanMid(matrix, mid_value, num_of_rows) < k:
                min_value = mid_value + 1
            else:
                max_value = mid_value
        return min_value
    
# 自己实现一遍 binary search.
class Solution:
    def countLeftHalf(self, matrix, target):
        n = len(matrix)
        r, c = n - 1, 0
        count, left_max, right_min = 0, matrix[0][0], matrix[n-1][n-1]
        while r >= 0 and c < n:
            if matrix[r][c] <= target:
                left_max = max(left_max, matrix[r][c])
                count += r + 1
                c += 1
            else:
                right_min = min(right_min, matrix[r][c])
                r -= 1
        return count, left_max, right_min

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_val, max_val = matrix[0][0], matrix[n-1][n-1]

        while min_val < max_val:
            mid_val = min_val + (max_val - min_val) // 2
            left_size, left_end, right_begin = self.countLeftHalf(matrix, mid_val)
            if left_size == k:
                return left_end
            elif left_size > k:
                max_val = left_end
            else:
                min_val = right_begin
        return min_val # 一开始漏了这行过不了[[1, 2], [3, 3]]，k = 3的case。因为最后min_val = max_val = 3