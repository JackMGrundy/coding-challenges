"""
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
"""
   
# 60ms. 92 percentile in speed
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        validBoards, invalidRows, invalidUpDiag, invalidDownDiag = [], set(), set(), set()
        
        def createRow(i):
            return "."*i + "Q" + "."*(n - i - 1)
        
        def backtrack(column, boardInProgress):
            if n <= column:
                validBoards.append(boardInProgress)
                return
            
            for row in range(n):
                
                if (row in invalidRows) or (row-column in invalidDownDiag) or (row+column in invalidUpDiag):
                    continue
                
                invalidRows.add(row)
                invalidDownDiag.add(row-column)
                invalidUpDiag.add(row+column)
                
                backtrack(column+1, boardInProgress + [createRow(row)])
                
                invalidRows.remove(row)
                invalidDownDiag.remove(row-column)
                invalidUpDiag.remove(row+column)
        
        backtrack(0, [])
        return validBoards


"""
Notes:

This is a standard backtracking problem with 2 important notes:

-) As is typical with backtracking, we want to expore a line of thought and
then be able to unwind it before branching in another direction. In this problem, 
at each level of recursion we are placing a queen in a column. We need to keep track
of what squares we are allowed to place a queen in. This is a function of where we
placed the previous queens. We know that each Queen we placed previously disallows
future use of the row it was placed in. 

The tricky part of this problem and the crux of the answer is how to deal with what
squares have been eliminated due to previous queens' diagonal lines of attack. The trick
is:
    Say we placed a queen in board[3][3]. We are now examining column 5. What diagonal squares
    are disallowed due to the placement in spot 3 or column 3? We cna quickly see that 1,5 and
    5,5 are disallowed. The equation to formalize this is:

    previous spot +- (cur column - prev column) = disallowed spots
 =  previous spot + cur column - prev column = disallowed spot
and previous spot - cur column + prev column = disallowed spot
       3        +     (5    -  3 )  =  5
    And
       3        -     (5    -  3)  =  1
    

    As we're iterating through the grid we are going to always have the current column
    and the current spot we are examining. Thereofre we'd like to rearrange the above equation:

    disallowed spot + cur column = previous spot + previous column
    disallowed spot - cur column = previous spot - previous column

    We maintain two sets, one for "up" diagonals and one for "down" diagonals. At each level,
    after we place a queen in a valid spot, we add spot + column to the "up" set and
    spot - column to the "down" set. Then we recurse. At the next levels or recursion, we can quickly
    check if a cell has been eliminated due to a digonal line of attack. 

    Row are much simpler to keep track of.

-) Next bit, is how to deal with return full boards for answers. It's a great idea to
    pass the entire board in progress down each level. And because list addition makes a new
    list in Python, we can just do "currentboard + [newRow(stuf)]" in each recursive call

"""