"""
This question is about implementing a basic elimination algorithm for Candy Crush.

Given a 2D integer array board representing the grid of candy, different positive integers board[i][j] represent different types of candies. A value of board[i][j] = 0 represents that the cell at position (i, j) is empty. The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:

If three or more candies of the same type are adjacent vertically or horizontally, "crush" them all at the same time - these positions become empty.
After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. (No new candies will drop outside the top boundary.)
After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
If there does not exist more candies that can be crushed (ie. the board is stable), then return the current board.
You need to perform the above rules until the board becomes stable, then return the current board.

 

Example:

Input:
board = 
[[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]

Output:
[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]

Explanation: 

 

Note:

The length of board will be in the range [3, 50].
The length of board[i] will be in the range [3, 50].
Each board[i][j] will initially start as an integer in the range [1, 2000].
"""
# 380ms. 12th percentile.
import copy
class Solution:
    streakThreshold = 3
    
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        crushed = True
        while crushed:
            crushed, board = self.crush(board)
            board = self.drop(board)
        
        return board
    

    def crush(self, board):
        squaresToCrush = [ [ False for square in row ] for row in board ]
        originalBoard = copy.deepcopy(board)
        
        # rows
        for y, row in enumerate(board):
            streakCount = 1
            previousValue = None
            for x, currentValue in enumerate(row):
                if currentValue != 0 and previousValue == currentValue and streakCount >= self.streakThreshold:
                    squaresToCrush[y][x] = True
                elif currentValue != 0 and previousValue == currentValue and streakCount < self.streakThreshold:
                    streakCount += 1
                    if streakCount >= self.streakThreshold:
                        for i in range(x-streakCount+1, x+1):
                            squaresToCrush[y][i] = True    
                else:
                    streakCount = 1
                    previousValue = currentValue
        
        # columns
        for x in range(len(board[0])):
            streakCount = 1
            previousValue = None
            for y in range(len(board)):
                currentValue = board[y][x]
                if currentValue != 0 and previousValue == currentValue and streakCount >= self.streakThreshold:
                    squaresToCrush[y][x] = True
                elif currentValue != 0 and previousValue == currentValue and streakCount < self.streakThreshold:
                    streakCount += 1
                    if streakCount >= self.streakThreshold:
                        for i in range(y-streakCount+1, y+1):
                            squaresToCrush[i][x] = True  
                else:
                    streakCount = 1
                    previousValue = currentValue
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                if squaresToCrush[y][x]:
                    board[y][x] = 0
        
        return (True, board) if originalBoard != board else (False, board)
    
            
    
    def drop(self, board):
        
        for x in range(len(board[0])):
            tail = runner = len(board)-1
            while runner >= 0 and tail >= 0:
                while tail >= 0 and board[tail][x] != 0:
                    tail -= 1
                runner = tail
                while runner >= 0 and board[runner][x] == 0:              
                    runner -= 1
                
                while runner >= 0 and tail >= 0 and board[tail][x] == 0 and board[runner][x] != 0:
                    board[tail][x], board[runner][x] = board[runner][x], board[tail][x]
                    tail -= 1
                    runner -= 1
        
        return board
                
                
                
            
            
# 208ms 61st percentile 
class Solution:
    streakThreshold = 3
    
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        crushed = True
        while crushed:
            crushed, board = self.crush(board)
            if crushed:
                board = self.drop(board)
        
        return board
    
    
    def crush(self, board):
        squaresToCrush = [ [ False for square in row ] for row in board ]
        crushed = False
        
        # rows
        for y, row in enumerate(board):
            streakCount = 1
            previousValue = None
            for x, currentValue in enumerate(row):
                if board[y][x]==0 or previousValue != currentValue:
                    streakCount = 1
                    previousValue = currentValue
                elif streakCount >= self.streakThreshold:
                    squaresToCrush[y][x] = True
                elif streakCount < self.streakThreshold:
                    streakCount += 1
                    if streakCount >= self.streakThreshold:
                        for i in range(x-streakCount+1, x+1):
                            squaresToCrush[y][i] = True    
                            crushed = True

        # columns
        for x in range(len(board[0])):
            streakCount = 1
            previousValue = None
            for y in range(len(board)):
                currentValue = board[y][x]
                if board[y][x]==0 or previousValue != currentValue:
                    streakCount = 1
                    previousValue = currentValue
                elif streakCount >= self.streakThreshold:
                    squaresToCrush[y][x] = True
                elif streakCount < self.streakThreshold:
                    streakCount += 1
                    if streakCount >= self.streakThreshold:
                        for i in range(y-streakCount+1, y+1):
                            squaresToCrush[i][x] = True 
                            crushed = True
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                if squaresToCrush[y][x]:
                    board[y][x] = 0
        
        return (crushed, board)
    
            
    
    def drop(self, board):
        
        for x in range(len(board[0])):
            tail = runner = len(board)-1
            while runner >= 0 and tail >= 0:
                while tail >= 0 and board[tail][x] != 0:
                    tail -= 1
                runner = tail
                while runner >= 0 and board[runner][x] == 0:              
                    runner -= 1
                
                while runner >= 0 and tail >= 0 and board[tail][x] == 0 and board[runner][x] != 0:
                    board[tail][x], board[runner][x] = board[runner][x], board[tail][x]
                    tail -= 1
                    runner -= 1
        
        return board
                



# 208ms. 61st percentile
# cleaner
class Solution:
    streakThreshold = 3
    
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        crushed = True
        while crushed:
            crushed, board = self.crush(board)
            if crushed:
                board = self.drop(board)
        return board
    
    def crush(self, board):
        squaresToCrush = [ [ 0 for square in row ] for row in board ]
        crushed = False
        
        # rows
        for y, row in enumerate(board):
            for x, currentValue in enumerate(row[:len(row)-2]):
                if board[y][x] != 0 and board[y][x] == board[y][x+1] == board[y][x+2]:
                    squaresToCrush[y][x], squaresToCrush[y][x+1], squaresToCrush[y][x+2] = 1, 1, 1
                    crushed = True
        
        # columns
        for x in range(len(board[0])):
            for y in range(len(board[:len(board)-2])):
                if board[y][x] != 0 and board[y][x] == board[y+1][x] == board[y+2][x]:
                    squaresToCrush[y][x], squaresToCrush[y+1][x], squaresToCrush[y+2][x] = 1, 1, 1
                    crushed = True
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                if squaresToCrush[y][x] == 1:
                    board[y][x] = 0
        
        return (crushed, board)

    
    def drop(self, board):
        for x in range(len(board[0])):
            tail = len(board)-1
            for runner in range(len(board)-1, -1, -1):
                if board[runner][x] > 0:
                    board[tail][x] = board[runner][x]
                    tail -= 1
            for i in range(tail, -1, -1):
                board[i][x] = 0

        return board