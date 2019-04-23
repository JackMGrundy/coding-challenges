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
class Solution {
  public void gameOfLife(int[][] board) {
      int m = board.length;
      int n = board[0].length;
      int[][] neighbors = new int[m][n];
      
      // Loop through cells
      for (int j = 0; j < m; j++) {
          for (int i = 0; i < n; i++) {
              
              // Loop through square around cell
              for (int inner_j = Math.max(0, j-1); inner_j < Math.min(m, j+2); inner_j++) {
                  for (int inner_i = Math.max(0, i-1); inner_i < Math.min(n, i+2); inner_i++) {
                      if (j == inner_j && i == inner_i) continue;
                      if (board[inner_j][inner_i]==1) neighbors[j][i]++;
                  }
              }
          }
      }
      
      // Apply update
      for (int j = 0; j < m; j++) {
          for (int i = 0; i < n; i++) {
              // Cell is alive
              if (board[j][i]==1) {
                  if (neighbors[j][i] < 2 || neighbors[j][i] > 3) board[j][i] = 0;
              }
              // Cell is dead
              else {
                  if (neighbors[j][i]==3) board[j][i] = 1;
              }
          }
      }
  }
}