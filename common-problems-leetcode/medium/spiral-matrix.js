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
// 1st attempt: 98th percentile in speed
/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    if (matrix.length===0) return [];
    let left = 0;
    let right = matrix[0].length;
    let bottom = matrix.length;
    let top = 0;
    let count = 0;
    let total = matrix[0].length * matrix.length;
    res = [];
    
    let i, j
    while (true) {
        for (i = left; i < right; i++) {
            res.push(matrix[top][i]);
            count++;
            if (count >= total) return res;
        }
        right--;
        
        for (j = top+1; j < bottom; j++) {
            res.push(matrix[j][right])
            count++;
            if (count >= total) return res;
        }
        bottom--;
        
        for (i = right-1; i >= left; i--) {
            res.push(matrix[bottom][i]);
            count++;
            if (count >= total) return res;
        }
        left++;
        
        for (let j = bottom-1; j > top; j--) {
            res.push(matrix[j][left-1]);
            count++;
            if (count >= total) return res;
        }
        top++;
    }
};