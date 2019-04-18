/*
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
*/
// 1st attempt: 15th percentile in speed
/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function(n, k) {
    if (k > n) return [];
    
    var bt = function(s, k, n, ans) {
        if (k===0) {
            res.push(ans);
            return;
        }
        
        for (let i=s; i < n+1; i++ ) {
            bt(i+1, k-1, n, ans.concat(i));
        }
    }
    
    var res = [];
    bt(1, k, n, []);
    return res;
    
};


// 2nd attempt: 25th percentile in speed
/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function(n, k) {
    if (k > n) return [];
    
    var bt = function(s, k, n, ans) {
        if (k===0) {
            res.push(JSON.parse(JSON.stringify(ans)));
            return;
        }
        
        for (let i=s; i < n+1; i++ ) {
            ans.push(i)
            bt(i+1, k-1, n, ans);
            ans.splice(ans.length-1);
        }
    }
    
    var res = [];
    bt(1, k, n, []);
    return res;
    
};

// 3rd attempt: 78th percentile in speed
// huge speedup from pop instead of splice. Intuitively makes sense,
// splice allocates a new list
/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function(n, k) {
    if (k > n) return [];
    
    var bt = function(s, k, n, ans) {
        if (k===0) {
            res.push(JSON.parse(JSON.stringify(ans)));
            return;
        }
        
        for (let i=s; i < n+1; i++ ) {
            ans.push(i)
            bt(i+1, k-1, n, ans);
            ans.pop();
        }
    }
    var res = [];
    bt(1, k, n, []);
    return res;
};


// 4th attempt: 96th percentile in speed
// Index trick
/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function(n, k) {
    if (k > n) return [];
    
    var bt = function(s, k, n, ans) {
        if (k===0) {
            res.push(JSON.parse(JSON.stringify(ans)));
            return;
        }
        
        for (let i=s; i < n-k+2; i++ ) {
            ans.push(i)
            bt(i+1, k-1, n, ans);
            ans.pop();
        }
    }
    
    var res = [];
    bt(1, k, n, []);
    return res;
};


// 5th attempt: 99th percentile in speed
// Slice instead of JSON method deep copy
/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function(n, k) {
    if (k > n) return [];
    
    var bt = function(s, k, n, ans) {
        if (k===0) {
            res.push(ans.slice());
            return;
        }
        
        for (let i=s; i < n-k+2; i++ ) {
            ans.push(i)
            bt(i+1, k-1, n, ans);
            ans.pop();
        }
    }
    
    var res = [];
    bt(1, k, n, []);
    return res;
    
};