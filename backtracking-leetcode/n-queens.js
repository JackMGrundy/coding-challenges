/*
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
*/
// 1st attempt 90th percentile
/*
Note: Javascript passes arrays by reference
/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function(n) {

  var createRow = function(x) {
      return ".".repeat(x) + 'Q' + ".".repeat(n-x-1);
  }
  
  var dfs = function(i, path) {
      if (i >= n ) {
          ans.push(path.slice(0));
          return;
      }
      
      for (let j = 0; j < n; j++) {
          if (rows.has(j)) continue;
          if (diagU.has(j-i)) continue;
          if (diagD.has(j+i)) continue;
          rows.add(j); diagU.add(j-i); diagD.add(j+i);
          path.push(createRow(j));
          dfs(i+1, path);
          path.splice(i)
          rows.delete(j);
          diagU.delete(j-i);
          diagD.delete(j+i);
      }
  }
  
  var ans = [],
      rows = new Set(),
      diagU = new Set(),
      diagD = new Set();
  
  dfs(0, []);
  return ans;
};

// 2nd attempt: 78th percentile in speed
// Similar to python, concat returns a new list. That makes things a bit cleaner,
// but we take a performance hit
// 
/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function(n) {

  var createRow = function(x) {
      return ".".repeat(x) + 'Q' + ".".repeat(n-x-1);
  }
  
  var dfs = function(i, path) {
      if (i >= n ) {
          ans.push(path.slice(0));
          return;
      }
      
      for (let j = 0; j < n; j++) {
          if (rows.has(j)) continue;
          if (diagU.has(j-i)) continue;
          if (diagD.has(j+i)) continue;
          rows.add(j); diagU.add(j-i); diagD.add(j+i);
          dfs(i+1, path.concat(createRow(j)));
          rows.delete(j);
          diagU.delete(j-i);
          diagD.delete(j+i);
      }
  }
  
  var ans = [],
      rows = new Set(),
      diagU = new Set(),
      diagD = new Set();
  
  dfs(0, []);
  return ans;
};