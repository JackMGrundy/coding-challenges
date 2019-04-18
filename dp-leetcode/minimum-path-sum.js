/*
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
*/

// 1st attempt: 99th percentile in speed
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    let m = grid.length,
        n = grid[0].length;
    
    var dp = [];
    for (let i = 0; i < m; i++) {
        dp[i] = grid[i].slice();
    }
    for (i = 1; i < n; i++) {
        dp[0][i] += dp[0][i-1];
    }
    
    for (let y = 1; y < m; y++) {
        dp[y][0] += dp[y-1][0];
        for (let x = 1; x < n; x++) {
            dp[y][x] += Math.min( dp[y-1][x], dp[y][x-1] );
        }
    }
    
    return dp[m-1][n-1];
};