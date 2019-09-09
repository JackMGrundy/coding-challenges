"""
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
"""

# Cleanest. 356ms. 75 percentile.
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, curCharIndex):
            if curCharIndex == len(word):
                return True
            
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[curCharIndex]:
                temp = board[i][j]
                board[i][j] = "*"
                
                matched = dfs(i+1, j, curCharIndex+1) or dfs(i-1, j, curCharIndex+1) or dfs(i, j+1, curCharIndex+1) or dfs(i, j-1, curCharIndex+1)
                
                board[i][j] = temp
                return matched
            else:
                return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False

# Fastest. 232ms. 98th percentile.
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        def dfs(board, j, i,  word):
            temp = board[j][i]
            board[j][i] = "#"
            if len(word)==0: 
                return True
            if (i > 0) and (board[j][i-1]==word[0]):
                if dfs(board, j, i-1, word[1:]):
                    return True
            if (i < n-1) and (board[j][i+1]==word[0]):
                if dfs(board, j, i+1, word[1:]):
                    return True
            if (j > 0) and (board[j-1][i]==word[0]):
                if dfs(board, j-1, i, word[1:]):
                    return True
            if (j < m-1) and (board[j+1][i]==word[0]):
                if dfs(board, j+1, i, word[1:]):
                    return True
            board[j][i] = temp
            return False
        
        for j in range(m):
            for i in range(n):
                if board[j][i]==word[0] and dfs(board, j, i, word[1:]):
                    return True
        return False

"""
Notes:

Intuition:
There are some cool idea to take away from this. You can think of each recursive call
as an additional condition that must be true in order for the whole process to be true.
...the first recursive dfs call can be thought of as a long string of additional if statements. 

Also note the backtracking nature of this. In the first call, say the first if statement is evaluated to 
True...then we are going to do a dfs search down this line of thought until we miss. If we do, we'll
switch the square back to not-visited (i.e. not "#"), and then back up until we're at a call where
we can trigger another true dfs call. 
"""