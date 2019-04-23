/*
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
*/
// 100th percentile
/**
 * @param {number[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var gameOfLife = function(board) {
  let m = board.length,
      n = board[0].length;

  let neighbors = Array.from({length : m}, 
                          () => Array.from({length: n}, () => 0));
  
  // Iterate through cells
  for (let j = 0; j < m; j++) {
      for (let i = 0; i < n; i++) {
          // Iterate through square around cell
          for (let j_inner = Math.max(0, j-1); j_inner < Math.min(j+2, m); j_inner++) {
              for (let i_inner = Math.max(0, i-1); i_inner < Math.min(i+2, n); i_inner++) {
                  if (j_inner==j && i_inner==i) continue;
                  if (board[j_inner][i_inner]===1) neighbors[j][i]++;
              }
          }
      }
  }

  // Apply rules
  for (let j = 0; j < m; j++) {
      for (let i = 0; i < n; i++) {
          // Cell is alive
          if (board[j][i]===1) {
              if (neighbors[j][i] < 2 || neighbors[j][i] > 3) board[j][i] = 0;
          }
          // Cell is dead
          else {
              if (neighbors[j][i]===3) board[j][i] = 1;
          }
      }
  }
};