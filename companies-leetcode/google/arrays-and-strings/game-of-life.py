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
# 32ms. 98 percentile. In place.
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        livingInLastRoundCases = [1, 2, 3]
        # deadInLastRoundCases   = [0, 4]
        nextRoundLivingCases = [2, 4]
        nextRoundDeadCases = [0, 1, 3]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                numNeighbors = 0
                for neighbor in [(i-1,j), (i+1,j), (i,j-1), (i,j+1), (i-1,j-1), (i+1,j+1), (i+1,j-1), (i-1,j+1)]:
                    nI, nJ = neighbor
                    if 0 <= nI < len(board) and 0 <= nJ < len(board[0]) and board[nI][nJ] in livingInLastRoundCases:
                        numNeighbors += 1
                
                if board[i][j] == 1 and numNeighbors in [0, 1]:
                    board[i][j] = 1
                elif board[i][j] == 1 and numNeighbors in [2, 3]:
                    board[i][j] = 2
                elif board[i][j] == 1 and 3 < numNeighbors:
                    board[i][j] = 3
                elif board[i][j] == 0 and numNeighbors == 3:
                    board[i][j] = 4
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in nextRoundLivingCases:
                    board[i][j] = 1
                elif board[i][j] in nextRoundDeadCases:
                    board[i][j] = 0

"""
Notes:

We make two passes. For each cell, we record which of the five case (the four given plus the fifth catch all) the square is. If we are looking at a 
cell with neighbors that have already been updated, we can deduce if the neighbor was alive in the last roow by looking at what case it was labeled
with...the first, second and third cases given indicate that the cell was alive in the last round. Coincidentally, a "1" also indicates it was
previously alive, so we can just check if the cell has a 1, 2, or 3 to deduce if the cell is a living neighbor. After labeling all the cells with what case
they were, we can do anothing pass over the board to fill in the final values. 

"""