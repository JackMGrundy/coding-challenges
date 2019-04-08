/*
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
*/
// 1st attempt: 91st percentile in speed
/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
  let m = board.length;
  let n = board[0].length;
  var dfs = function(board, j, i, word) {
      let temp = board[j][i];
      board[j][i] = "#";
      if (word.length==0) return true
      if ( (i > 0) && (board[j][i-1]==word[0]) ) {
          if ( dfs(board, j, i-1, word.slice(1, word.length)) ) return true
      }
      if ( (i < n-1) && (board[j][i+1]==word[0]) ) {
          if ( dfs(board, j, i+1, word.slice(1, word.length)) ) return true
      }
      if ( (j > 0) && (board[j-1][i]==word[0]) ) {
          if ( dfs(board, j-1, i, word.slice(1, word.length)) ) return true
      }
      if ( (j < m-1) && (board[j+1][i]==word[0]) ) {
          if ( dfs(board, j+1, i, word.slice(1, word.length)) ) return true
      }
      board[j][i] = temp;
      return false;
  }
  
  for (let j = 0; j < m; j++) {
      for (let i = 0; i < n; i++) {
          if (word[0]==board[j][i] && dfs(board, j, i, word.slice(1, word.length))) return true
      }
  }
  return false
};