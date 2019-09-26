"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""
# 36ms. 97 percentile. Space reduction approach.
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        i, j = len(matrix) - 1, 0
        
        while 0 <= i and j < len(matrix[0]):
            if matrix[i][j] == target:
                return True
            elif target < matrix[i][j]:
                i -= 1
            else:
                j += 1
        
        
        return False


"""
Notes:

There are a few different approaches to this:

1) Space reduction  O(N + M) Time. O(1) Space
Pretty amazing algo
[1, 4, 7, 11,15]
[2, 5, 8, 12,19]
[3, 6, 9, 16,22]
[10,13,14,17,24]
[18,21,23,26,30]

Say we want to find 8. Start at the bottom left. 18 > 8, so go down a row.
10 > 8. Go down a row. 3 < 8. Go right a column...following this pattern gets you to 8.

If you end up out of bounds then the value wasn't found.

Why does this work? 

Rule: if the current value is bigger than the target, drop a row. This can
never prune the answer, because all the values to the right of current value are bigger
than it.

Rule: if the current value is smaller than the target, increase the column. This only
prunes the values above current value in the column. We know these must also be smaller
than the target, so no problem. 


"""