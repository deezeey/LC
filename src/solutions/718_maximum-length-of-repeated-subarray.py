from typing import List

# 2D DP T O(M x N) M O(M x N)
# def findLength(nums1: List[int], nums2: List[int]) -> int:
#     if not nums1 or not nums2:
#         return 0
#     # instantiate a matrix of (m x n)
#     rows, cols = len(nums1), len(nums2)
#     max_len = 0
#     dp = [[0] * cols for row in range(rows)]

#     # fill in first row and first column
#     for i in range(rows):
#         for j in range(cols):
#             if nums1[i] == nums2[j]:
#                 dp[i][j] = 1
#                 max_len = 1

#     # if nums1[row] == nums2[col], dp[row][col] = matrix[row - 1][col - 1] + 1, else 0
#     for r in range(1, rows):
#         for c in range(1, cols):
#             if nums1[r] == nums2[c]:
#                 max_len = max(max_len, dp[r][c])

#     # max cell in matrix is result
#     return max_len

# sliding window T O m*n M O 1
def findLength(nums1: List[int], nums2: List[int]) -> int:
		m = len(nums1)
		n = len(nums2)

		maxLen = 0

		# slide one array over the other from left to right
		for a in range(-(n-1), m): # a is the position diff between array nums1 and nums2 when they're stacked together
			cnt = 0
			for j in range(n):
				i = a + j
				if i < 0:
					continue
				elif i >= m:
					break
				elif nums1[i] == nums2[j]:
					cnt = cnt + 1
					maxLen = max(maxLen, cnt)
				else:
					cnt = 0

		return maxLen


def testEmpty():
    nums1, nums2 = [1, 2, 3], []
    assert findLength(nums1, nums2) == 0
    
def testNormal():
    nums1, nums2 = [1,2,3,2,8], [5,6,1,4,7]
    assert findLength(nums1, nums2) == 1

def testNormal2():
    nums1, nums2 = [0, 0, 0, 0], [0, 0, 0, 0]
    assert findLength(nums1, nums2) == 4

def testNormal3():
    nums1, nums2 = [1, 2, 3, 4], [3, 2, 4, 5, 2, 3]
    assert findLength(nums1, nums2) == 2

def testNoResult():
    nums1, nums2 = [1, 2, 3], [4, 5, 6]
    assert findLength(nums1, nums2) == 0
