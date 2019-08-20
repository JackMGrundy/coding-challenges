/*
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
*/
// 44ms. 97th percentile.
/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    let pascalsTriangle = [ [1], [1, 1]];
    
    for (let i = 2; i < numRows; i++) {
        let previousRow = pascalsTriangle[pascalsTriangle.length-1];
        let currentRow = [1];
        for (let j = 0; j < previousRow.length-1; j++) {
            currentRow.push(previousRow[j]+previousRow[j+1]);
        }
        currentRow.push(1);
        pascalsTriangle.push(currentRow);
    }
    
    return pascalsTriangle.slice(0, numRows);
};