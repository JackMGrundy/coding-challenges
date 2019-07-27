/*
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
*/

// 1st attempt: 0ms, 99th percentile in speed
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> answer = new ArrayList<Integer>();
        int L = matrix.length;
        if (L==0) {
            return answer;
        }
        int W = matrix[0].length;
        int totalNumElements = L * W;
        int numElementsProcessed = 0;
        
        int topBoundary = 0;
        int rightBoundary = W;
        int bottomBoundary = L;
        int leftBoundary = 0;
        
        while (numElementsProcessed < totalNumElements) {
            
            // Top row
            for (int i = leftBoundary; i < rightBoundary; i++) {
                answer.add(matrix[topBoundary][i]);
                numElementsProcessed++;
            }
            topBoundary++;
            if (numElementsProcessed == totalNumElements) {
                return answer;
            }
            
            
            // Right column
            rightBoundary--;
            for (int i = topBoundary; i < bottomBoundary; i++) {
                answer.add(matrix[i][rightBoundary]);
                numElementsProcessed++;
            }
            if (numElementsProcessed == totalNumElements) {
                return answer;
            }
            
            
            // Bottom row
            bottomBoundary--;
            for (int i = rightBoundary-1; i >= leftBoundary; i--) {
                answer.add(matrix[bottomBoundary][i]);
                numElementsProcessed++;
            }
            if (numElementsProcessed == totalNumElements) {
                return answer;
            }
            
            
            // Left column
            for (int i = bottomBoundary-1; i >= topBoundary; i--) {
                answer.add(matrix[i][leftBoundary]);
                numElementsProcessed++;
            }
            leftBoundary++;
            if (numElementsProcessed == totalNumElements) {
                return answer;
            }
            
        }
        

        return answer;
    }
}