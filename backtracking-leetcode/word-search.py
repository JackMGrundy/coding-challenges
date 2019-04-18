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
# Attempt 1: passes 85/87 test case and then timeouts on the big ones
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        res = False
        
        def inRange(y, x, j, i):
            return ( j >= 0 and j < y and i >= 0 and i < x )
        
        def validNeighbors(y, x, j, i):
            neighbors = [ (j+1, i), (j-1, i), (j, i+1), (j, i-1) ]
            res = []
            for neighbor in neighbors:
                jx, ix = neighbor
                if inRange(y, x, jx, ix):
                    res.append(neighbor)
            return res
        
        
        def search(jc, ic, cur):
            nonlocal res
            # Matched all the letters in the word
            if cur==len(word):
                res = True
            # Keep matching
            else:
                # Check all valid neighbors
                neighbors = validNeighbors(m, n, jc, ic)
                for neighbor in neighbors:
                    jn, ji = neighbor
                    # If the neighbor is a match and not already visited, recurse
                    if board[jn][ji]==word[cur] and (jn, ji) not in visited:
                        visited.add( (jn, ji) )
                        search(jn, ji, cur+1)
                # Ended recursion. Back track and remove cur from visited
                visited.remove( (jc, ic) )

        
        # Iterate through squares on board
        for i in range(n):
            for j in range(m):
                visited = set()
                
                if word[0]==board[j][i]:
                    visited.add( (j, i) )
                    search(j, i, 1)
        
        return res

# 2nd attempt: 16th percentile in speed. Cut off unneccessary search.
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        res = False
        
        def inRange(y, x, j, i):
            return ( j >= 0 and j < y and i >= 0 and i < x )
        
        def validNeighbors(y, x, j, i):
            neighbors = [ (j+1, i), (j-1, i), (j, i+1), (j, i-1) ]
            res = []
            for neighbor in neighbors:
                jx, ix = neighbor
                if inRange(y, x, jx, ix):
                    res.append(neighbor)
            return res
        
        
        def search(jc, ic, cur):
            nonlocal res
            if res: return
            # Matched all the letters in the word
            if cur==len(word):
                res = True
            # Keep matching
            else:
                # Check all valid neighbors
                neighbors = validNeighbors(m, n, jc, ic)
                for neighbor in neighbors:
                    jn, ji = neighbor
                    # If the neighbor is a match and not already visited, recurse
                    if board[jn][ji]==word[cur] and (jn, ji) not in visited:
                        visited.add( (jn, ji) )
                        search(jn, ji, cur+1)
                # Ended recursion. Back track and remove cur from visited
                visited.remove( (jc, ic) )

        
        # Iterate through squares on board
        for i in range(n):
            for j in range(m):
                visited = set()
                
                if word[0]==board[j][i]:
                    visited.add( (j, i) )
                    search(j, i, 1)
        
        return res


# 3rd attempt: 16th percentile in speed. No diff between nonlocal and class variable
class Solution:
    res = False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        def inRange(y, x, j, i):
            return ( j >= 0 and j < y and i >= 0 and i < x )
        
        def validNeighbors(y, x, j, i):
            neighbors = [ (j+1, i), (j-1, i), (j, i+1), (j, i-1) ]
            valid = []
            for neighbor in neighbors:
                jx, ix = neighbor
                if inRange(y, x, jx, ix):
                    valid.append(neighbor)
            return valid
        
        
        def search(jc, ic, cur):
            if self.res: return
            # Matched all the letters in the word
            if cur==len(word):
                self.res = True
            # Keep matching
            else:
                # Check all valid neighbors
                neighbors = validNeighbors(m, n, jc, ic)
                for neighbor in neighbors:
                    jn, ji = neighbor
                    # If the neighbor is a match and not already visited, recurse
                    if board[jn][ji]==word[cur] and (jn, ji) not in visited:
                        visited.add( (jn, ji) )
                        search(jn, ji, cur+1)
                # Ended recursion. Back track and remove cur from visited
                visited.remove( (jc, ic) )

        
        # Iterate through squares on board
        for i in range(n):
            for j in range(m):
                visited = set()
                
                if word[0]==board[j][i]:
                    visited.add( (j, i) )
                    search(j, i, 1)
        
        return self.res

# Attempt 4: 63rd percentile. Cleaning up the neighbor selection sped things up
class Solution:
    res = False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        def validNeighbors(y, x, j, i):
            valid = []
            if i > 0:
                valid.append( (j, i-1) )
            if i < x-1:
                valid.append( (j, i+1) )
            if j > 0:
                valid.append( (j-1, i) )
            if j < y-1:
                valid.append( (j+1, i) )
            return valid
        
        
        def search(jc, ic, cur):
            if self.res: return
            # Matched all the letters in the word
            if cur==len(word):
                self.res = True
            # Keep matching
            else:
                # Check all valid neighbors
                neighbors = validNeighbors(m, n, jc, ic)
                for neighbor in neighbors:
                    jn, ji = neighbor
                    # If the neighbor is a match and not already visited, recurse
                    if board[jn][ji]==word[cur] and (jn, ji) not in visited:
                        visited.add( (jn, ji) )
                        search(jn, ji, cur+1)
                # Ended recursion. Back track and remove cur from visited
                visited.remove( (jc, ic) )

        
        # Iterate through squares on board
        for i in range(n):
            for j in range(m):
                visited = set()
                
                if word[0]==board[j][i]:
                    visited.add( (j, i) )
                    search(j, i, 1)
        
        return self.res

# Attempt 5: 95th percentile in speed. Cleaner
"""
Intuition:
There are some cool idea to take away from this. You can think of each recursive call
as an additional condition that must be true in order for the whole process to be true.
...the first recursive dfs call can be thought of as a long string of additional if statements. 

Also note the backtracking nature of this. In the first call, say the first if statement is evaluated to 
True...then we are going to do a dfs search down this line of thought until we miss. If we do, we'll
switch the square back to not-visited (i.e. not "#"), and then back up until we're at a call where
we can trigger another true dfs call. 
"""
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
       