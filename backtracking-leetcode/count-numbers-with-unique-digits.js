/*
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99
*/
// 1st attempt: 96th percentile in speed
/**
 * @param {number} n
 * @return {number}
 */
var countNumbersWithUniqueDigits = function(n) {
    var bt = function(x) {
        if (x===0) return 0;
        let ans = 9;
        for (let i = 0; i < x-1; i++) ans *= (9-i);
        return ans + bt(x-1);
    }
    return 1+bt(n);
};

// 3rd attempt: 96th percentile in speed
// I have a habit of adding a new recursive fucntion instead of just making the original stub
// recursive
/**
 * @param {number} n
 * @return {number}
 */
var countNumbersWithUniqueDigits = function(n) {
    if (n===0) return 1;
    let ans = 9;
    for (let i = 0; i < n-1; i++) ans *= (9-i);
    return ans+countNumbersWithUniqueDigits(n-1);
};