/*
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
*/
// 1st attempt: 93rd percentile in speed
/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    const ans = [];
    var backtrack = function(s='', l=0, r=0) {
        if (l + r === 2 * n) ans.push(s);
        if (l < n) backtrack(s+'(', l+1, r);
        if (r < l) backtrack(s+')', l, r+1);
    }
    
    backtrack();
    return ans;
};