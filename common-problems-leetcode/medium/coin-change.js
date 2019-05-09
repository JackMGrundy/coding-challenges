/*
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.

Accepted
185,162
Submissions
618,159
*/
// 99th percentile 80ms
/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    let dp = new Array(amount+1).fill(Number.MAX_SAFE_INTEGER);
    dp[0] = 0;
    
    coins.forEach(coin => {
        for (let i = coin; i < amount+1; i++) {
            dp[i] = Math.min(dp[i], dp[i-coin]+1);
        }
    })
    
    return dp[amount] < Number.MAX_SAFE_INTEGER ? dp[amount] : -1;
};