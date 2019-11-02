/*
Given  a  2D  matrix  matrix,  find the sum of the elements inside the rectangle
defined  by  its  upper  left  corner (row1, col1) and lower right corner (row2,
col2).                                                                          

Range Sum Query 2D                                                              

The  above  rectangle  (with the red border) is defined by (row1, col1) = (2, 1)
and (row2, col2) = (4, 3), which contains sum = 8.                              

Example:                                                                        

Given matrix = [                                                                

  [3, 0, 1, 4, 2],                                                              

  [5, 6, 3, 2, 1],                                                              

  [1, 2, 0, 1, 5],                                                              

  [4, 1, 0, 1, 7],                                                              

  [1, 0, 3, 0, 5]                                                               

]                                                                               

sumRegion(2, 1, 4, 3) -> 8                                                      

sumRegion(1, 1, 2, 2) -> 11                                                     

sumRegion(1, 2, 2, 4) -> 12                                                     

Note:                                                                           

You may assume that the matrix does not change.                                 

There are many calls to sumRegion function.                                     

You may assume that row1 ≤ row2 and col1 ≤ col2.                                

Accepted                                                                        

86K                                                                             

Submissions                                                                     

246.9K                                                                          

*/
// Approach 2: 80ms. 83 percentile in speed
/**
 * @param {number[][]} matrix
 */
var NumMatrix = function(matrix) {
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[0].length; j++) {
            if (0 < i) {
                matrix[i][j] += matrix[i - 1][j];
            }
            if (0 < j) {
                matrix[i][j] += matrix[i][j - 1]
            }
            if (0 < i && 0 < j) {
                matrix[i][j] -= matrix[i - 1][j - 1]
            }
        }
    }
    this.matrix = matrix;
};

/** 
 * @param {number} row1 
 * @param {number} col1 
 * @param {number} row2 
 * @param {number} col2
 * @return {number}
 */
NumMatrix.prototype.sumRegion = function(row1, col1, row2, col2) {
    let result = this.matrix[row2][col2]
    
    if (0 <= col1 - 1) {
        result -= this.matrix[row2][col1 - 1];
    }
    
    if (0 <= row1 - 1) {
        result -= this.matrix[row1 - 1][col2];
    }
    
    if (0 <= col1 - 1 && 0 <= row1 - 1) {
        result += this.matrix[row1 - 1][col1 - 1];
    }
    
    return result
};

/** 
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = new NumMatrix(matrix)
 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
 */




/*
Notes:
A few approaches:


1) Simple dp way
Initialize a dp array where each row is simply a cumulative sum
To do a query, iterate through the rows of the relevant section, subtracting
the value in the column after the section from the first column in the section. 

M = num rows
N = num cols
Time per query: O(M)
Precomputation: O(M*N)

Space: O(M*N)




2) Somewhat more complicated but still simple dp way
Instead of calculating the cumulative sums row wise, calculate it as the sum of the
square stretching from (0,0) to the current cell.

Later, say we're completing a query whose corners are at A, B, C, D...

We have:  Sum(ABCD) = Sum(0D) - Sum(0B) - Sum(0C) + Sum(0A)
Where 0 represents the top left corner

Precomputation time complexity: O(M*N)
Time per query: O(1)
Space complexity: O(M*N)


^For this problem, this is the best answer. Note that this works because we don't
have to make changes. If we had to make changes to the array, we would have to MN 
work every time a change was made and we would be in trouble. 





3) Fancy 2D segment tree approach
This is slower for processing queries, but it can handle modifications. 

Processing Query : O(logN*logM)
Modification Query: O(2N*logN*logM)
Space Complexity : O(4*M*N)

TODO: Not diving into all the details of this...

*/