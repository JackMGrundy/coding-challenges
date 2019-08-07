/*
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.

Example:

Input: n = 3, k = 2
Output: 6
Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:

            post1  post2  post3      
 -----      -----  -----  -----       
   1         c1     c1     c2 
   2         c1     c2     c1 
   3         c1     c2     c2 
   4         c2     c1     c1  
   5         c2     c1     c2
   6         c2     c2     c1
Accepted
41,106
Submissions
113,416
*/ 
// 1st attempt: 26th percentile
/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var numWays = function(n, k) {
    if (k===0 || n===0) return 0;
    if (n < 3 ) return k ** n;
    let a = 1,
        arr = k;
    for (let i = 2; i < n; i++) {
        a = arr - a;
        arr = arr*(k-1) + a;
    }
    return arr*k;
};

// 2nd attempt. 52ms. 60t percentile. 
/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var numWays = function(n, k) {
    if (n === 0 || k === 0 || (n > 2 && k === 1)) {
        return 0;
    }
    if (n === 1) {
        return k;
    }
    let s = k*k;
    let a = k;
    let b;
    for (let i = 2; i < n; i++) {
        b = a;
        a = s - b;
        s = b*(k-1) + a*k;
    }
    
    return s;
};