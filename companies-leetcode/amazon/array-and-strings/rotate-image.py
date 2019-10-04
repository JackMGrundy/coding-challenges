"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""

# 40ms. 82 percentile.
# Not super readable...
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return None
        
        for topLeftY in range(len(matrix)//2):
            
            for topLeftX in range(topLeftY, len(matrix)-topLeftY-1):
                topLeftValue = matrix[topLeftY][topLeftX]
                matrix[topLeftY][topLeftX] = matrix[len(matrix)-1-topLeftX][topLeftY]
                matrix[len(matrix)-1-topLeftX][topLeftY] = matrix[len(matrix)-1-topLeftY][len(matrix)-1-topLeftX]
                matrix[len(matrix)-1-topLeftY][len(matrix)-1-topLeftX] = matrix[topLeftX][len(matrix)-1-topLeftY]
                matrix[topLeftX][len(matrix)-1-topLeftY] = topLeftValue



# 36ms. 96 percentile.
# Better
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for topLeftY in range(len(matrix)//2):
            for topLeftX in range(topLeftY, len(matrix)-topLeftY-1):
                topLeftValue = matrix[topLeftY][topLeftX]
                matrix[topLeftY][topLeftX] = matrix[~topLeftX][topLeftY]
                matrix[~topLeftX][topLeftY] = matrix[~topLeftY][~topLeftX]
                matrix[~topLeftY][~topLeftX] = matrix[topLeftX][~topLeftY]
                matrix[topLeftX][~topLeftY] = topLeftValue



# ove python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)//2):
            for j in range(i, len(matrix[0]) - i - 1):
                matrix[i][j],  matrix[~j][i],  matrix[~i][~j], matrix[j][~i] = \
                matrix[~j][i], matrix[~i][~j], matrix[j][~i],  matrix[i][j]