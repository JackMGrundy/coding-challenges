/*
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
*/

// 1st attempt: 59th percentile
/**
 * @param {number} n
 * @return {number}
 */
var numSquares = function(n) {
    let dp = [0, 1, 2, 3];
    let biggestSquare;
    
    for (let i = 4; i < n+1; i++) {
        biggestSquare = 1;
        let temp = Number.MAX_SAFE_INTEGER;
        while ( biggestSquare ** 2 <= i ) {
            temp = Math.min( temp, dp[ i - biggestSquare ** 2]+1 );
            biggestSquare += 1;
        }
        dp.push(temp);
    }
    
    return dp[n];
};


// 2nd attempt: 98th percentile
// same as above, but only extend array when needed
/**
 * @param {number} n
 * @return {number}
 */
const dp = [0, 1, 2, 3];
var numSquares = function(n) {
    let biggestSquare;
        
    for (let i = dp.length; i < n+1; i++) {
        biggestSquare = 1;
        let temp = Number.MAX_SAFE_INTEGER;
        while ( biggestSquare ** 2 <= i ) {
            temp = Math.min( temp, dp[ i - biggestSquare ** 2]+1 );
            biggestSquare += 1;
        }
        dp.push(temp);
    }
    
    return dp[n];
};