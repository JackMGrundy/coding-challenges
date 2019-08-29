/*
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
*/

// 64ms. 93rd percentile.
/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalSquare = function(matrix) {
    if (matrix.length === 0) {
        return 0;
    }
    
    let dp = Array(matrix[0].length+1).fill(0);
    let best = 0;
    let prevSquare = 0;
    for (let j = 1; j < matrix.length+1; j++) {
        for (let i = 1; i < matrix[0].length+1; i++) {
            let temp = dp[i];
            if (matrix[j-1][i-1] === '1') {
                dp[i] = Math.min(dp[i], dp[i-1], prevSquare)+1;
                best = Math.max(best, dp[i]);
            } else {
                dp[i] = 0;
            }
            prevSquare = temp;
        }
    }
    
    return best*best;
};