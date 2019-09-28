"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
Accepted
146K
Submissions
375.3K
"""
# 88ms. 89 percentile.
from collections import deque, defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, columns, squares, blanks = defaultdict(set), defaultdict(set), defaultdict(set), deque([])
        for i in range(len(board)):
            for j in range(len(board[0])):
                value = board[i][j]
                if value == ".":
                    blanks.append( (i, j) )
                else:
                    rows[i].add(value)
                    columns[j].add(value)
                    squares[ (i//3, j//3) ].add(value)

        def backtrack():
            if len(blanks) == 0:
                return True
            
            i, j = blanks[0]
            sq = (i//3, j//3)
            for value in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                if (value not in rows[i]) and (value not in columns[j]) and (value not in squares[sq]):
                    board[i][j] = value
                    rows[i].add(value)
                    columns[j].add(value)
                    squares[sq].add(value)
                    blanks.popleft()
                    if backtrack():
                        return True
                    else:
                        board[i][j] = "."
                        rows[i].discard(value)
                        columns[j].discard(value)
                        squares[sq].discard(value)
                        blanks.appendleft( (i,j) )
            
            return False
        
        backtrack()

"""
Notes:

Backtracking

There's no trick to this. It's just standard backtracking. The challenge is to make an
answer that's concise and performant.

My favorite way so far:

Make a set for every row and for every column. These sets records what numbers have been
seen in the rows and columns. For the squares, we make 9 sets as well. We map an element
to a square usign its (column // 3, row // 3)
During the preprocessing we initialize all these sets by iterating over all the squares 
and updating accordingly.

We also initialize a deque of all the blank squares and call it visit

For the backtracking:
    If visit is empty, we must have an answer.

    Else, popleft from the deque to get the cell we want to visit.
    This gives us the row and the column. To get the square, we can just int divide 
    the row and column by 3...yields an identifying tuple. 

    From there on out its straight backtracking. For each value, 1 to 9, we try to spin
    up a recursive call. If placing the value in the square doesn't violate any constraints,
    we update the row, column, and square sets. And we recurse.

    During the unwinding part, we just undo the updates to the sets. And because we're using
    a deque for visit, we can easily add the spot back to visit.

Ojala
"""