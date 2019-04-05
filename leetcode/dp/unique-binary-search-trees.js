/*
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
*/
// 1st attempt: 92nd percentile
/**
 * @param {number} n
 * @return {number}
 */
var numTrees = function(n) {
    var dp = new Array(n+1).fill(0);
    dp[0] = 1;
    for (let i = 1; i < n+1; i++) {
        for (let j = 0; j < i; j++) {
            dp[i] += dp[j]*dp[i-1-j];
        }
    }
    return dp[n];
};