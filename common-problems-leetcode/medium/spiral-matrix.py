"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
# 1st attempt: 71st percentile in speed
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []

        totalNumElements = len(matrix) * len(matrix[0])
        numElementsProcessed = 0
        answer = []
        
        topBoundary = 0
        rightBoundary = len(matrix[0])
        bottomBoundary = len(matrix)
        leftBoundary = 0
        while numElementsProcessed < totalNumElements:
            
            # Top row
            for ele in range(leftBoundary, rightBoundary):
                answer.append(matrix[topBoundary][ele])
                numElementsProcessed += 1
            topBoundary += 1
            if numElementsProcessed==totalNumElements: 
                return answer
            
            # Right column
            rightBoundary -= 1
            for ele in range(topBoundary, bottomBoundary):
                answer.append(matrix[ele][rightBoundary])
                numElementsProcessed += 1
            if numElementsProcessed==totalNumElements: 
                return answer
            
            # Bottom row
            bottomBoundary -= 1
            for ele in range(rightBoundary-1, leftBoundary-1, -1):
                answer.append(matrix[bottomBoundary][ele])
                numElementsProcessed += 1
            if numElementsProcessed==totalNumElements: 
                return answer
            
            # Left column
            for ele in range(bottomBoundary-1, topBoundary-1, -1):
                answer.append(matrix[ele][leftBoundary])
                numElementsProcessed += 1
            leftBoundary += 1
            if numElementsProcessed==totalNumElements: 
                return answer
        