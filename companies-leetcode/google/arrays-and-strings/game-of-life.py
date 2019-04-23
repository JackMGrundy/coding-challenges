"""
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
"""
# 70th percentile
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        neighbors = [ [ 0 for _ in range(n) ] for x in range(m) ]
        
        # Iterate through cells
        for j in range(m):
            for i in range(n):

                # Count neighbors in a square around the cell
                for j_inner in range(max(0, j-1), min(m, j+2)):
                    for i_inner in range(max(0, i-1), min(n, i+2)):
                        if j_inner == j and i_inner == i: continue
                        if board[j_inner][i_inner]==1:
                            neighbors[j][i] += 1
        
        # Apply update
        for j in range(m):
            for i in range(n):
                # cell is alive
                if board[j][i] == 1:
                    if neighbors[j][i] < 2 or neighbors[j][i] > 3:
                        board[j][i] = 0
                # cell is dead
                else:
                    if neighbors[j][i] == 3:
                        board[j][i] = 1