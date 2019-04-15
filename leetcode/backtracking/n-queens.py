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
# 1st attempt: 30th percentile in speed
import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        if n == 0: return res
        # board = [ [ "_" for _ in range(n) ] for _ in range(n) ]
        board = [ [ "." for _ in range(n) ] for _ in range(n) ]
        
        def dfs(board, rowNum):
            if rowNum == n: return
            row = board[rowNum]
            # Check each possible spot in row
            for i in range(n):
                # Square is not precluded by earlier placements
                if row[i]==".":
                    board[rowNum][i]="Q"
                    
                    # Succesful placement of n queens -> save solution
                    if rowNum==n-1: 
                        res.append(copy.deepcopy(board))
                        # print(board)
                        board[rowNum][i]="."
                        
                    # Continue/recurse
                    else:
                        # First flip later impacted squares to "."
                        y = rowNum+1
                        while y < n: # Column
                            if board[y][i]==".":
                                board[y][i] = str(rowNum)
                            y += 1 
                             
                        y = rowNum+1; dx = 1
                        while y < n: # Diagonals
                            if i+dx < n and board[y][i+dx]==".":
                                board[y][i+dx] = str(rowNum)
                            if i-dx >= 0 and board[y][i-dx]==".": 
                                board[y][i-dx] = str(rowNum)
                            y += 1; dx += 1 
                            
                        dfs(board, rowNum+1)
                        
                        # Flip impacted squares back to "#"
                        board[rowNum][i]="."
                        
                        y = rowNum+1
                        while y < n: # Column
                            if board[y][i] == str(rowNum):
                                board[y][i] = "."
                            y += 1 
                            
                        y = rowNum+1; dx = 1
                        while y < n: # Diagonals
                            if i+dx < n and board[y][i+dx] == str(rowNum):
                                board[y][i+dx] = "."
                            if i-dx >= 0 and board[y][i-dx] == str(rowNum): 
                                board[y][i-dx] = "."
                            y += 1; dx += 1
        
        dfs(board, 0)
        # Format
        for x in range(len(res)):
            ans = res[x]
            for i in range(len(ans)):
                ans[i] = ''.join(ans[i])
                for v in range(n):
                    v = str(v)
                    ans[i] = ans[i].replace(v, ".")
            res[x] = ans
            
        return res
            
# attempt 2: 38th percentile. smarter formatting at end
import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        if n == 0: return res
        # board = [ [ "_" for _ in range(n) ] for _ in range(n) ]
        board = [ [ "." for _ in range(n) ] for _ in range(n) ]
        
        def dfs(board, rowNum):
            if rowNum == n: return
            row = board[rowNum]
            # Check each possible spot in row
            for i in range(n):
                # Square is not precluded by earlier placements
                if row[i]==".":
                    board[rowNum][i]="Q"
                    
                    # Succesful placement of n queens -> save solution
                    if rowNum==n-1: 
                        res.append(copy.deepcopy(board))
                        # print(board)
                        board[rowNum][i]="."
                        
                    # Continue/recurse
                    else:
                        # First flip later impacted squares to "."
                        y = rowNum+1
                        while y < n: # Column
                            if board[y][i]==".":
                                board[y][i] = str(rowNum)
                            y += 1 
                             
                        y = rowNum+1; dx = 1
                        while y < n: # Diagonals
                            if i+dx < n and board[y][i+dx]==".":
                                board[y][i+dx] = str(rowNum)
                            if i-dx >= 0 and board[y][i-dx]==".": 
                                board[y][i-dx] = str(rowNum)
                            y += 1; dx += 1 
                            
                        dfs(board, rowNum+1)
                        
                        # Flip impacted squares back to "#"
                        board[rowNum][i]="."
                        
                        y = rowNum+1
                        while y < n: # Column
                            if board[y][i] == str(rowNum):
                                board[y][i] = "."
                            y += 1 
                            
                        y = rowNum+1; dx = 1
                        while y < n: # Diagonals
                            if i+dx < n and board[y][i+dx] == str(rowNum):
                                board[y][i+dx] = "."
                            if i-dx >= 0 and board[y][i-dx] == str(rowNum): 
                                board[y][i-dx] = "."
                            y += 1; dx += 1
        
        dfs(board, 0)
        # Format
        rem = [ str(x) for x in range(n) ]
        for x in range(len(res)):
            ans = res[x]
            for i in range(len(ans)):
                ans[i] = [ "." if x in rem else x for x in ans[i] ]
                ans[i] = ''.join(ans[i])
            res[x] = ans
            
        return res
            


# 3rd attempt: 46th percentile. Reduce casting and smarter formatting.
import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        if n == 0: return res
        # board = [ [ "_" for _ in range(n) ] for _ in range(n) ]
        board = [ [ -1 for _ in range(n) ] for _ in range(n) ]
        
        def dfs(board, rowNum):
            if rowNum == n: return
            row = board[rowNum]
            # Check each possible spot in row
            for i in range(n):
                # Square is not precluded by earlier placements
                if row[i]==-1:
                    board[rowNum][i]="Q"
                    
                    # Succesful placement of n queens -> save solution
                    if rowNum==n-1: 
                        res.append(copy.deepcopy(board))
                        # print(board)
                        board[rowNum][i]=-1
                        
                    # Continue/recurse
                    else:
                        # First flip later impacted squares
                        y = rowNum+1
                        while y < n: # Column
                            if board[y][i]==-1:
                                board[y][i] = rowNum
                            y += 1 
                             
                        y = rowNum+1; dx = 1
                        while y < n: # Diagonals
                            if i+dx < n and board[y][i+dx]==-1:
                                board[y][i+dx] = rowNum
                            if i-dx >= 0 and board[y][i-dx]==-1: 
                                board[y][i-dx] = rowNum
                            y += 1; dx += 1 
                            
                        dfs(board, rowNum+1)
                        
                        # Flip impacted squares back
                        board[rowNum][i]=-1
                        
                        y = rowNum+1
                        while y < n: # Column
                            if board[y][i] == rowNum:
                                board[y][i] = -1
                            y += 1 
                            
                        y = rowNum+1; dx = 1
                        while y < n: # Diagonals
                            if i+dx < n and board[y][i+dx] == rowNum:
                                board[y][i+dx] = -1
                            if i-dx >= 0 and board[y][i-dx] == rowNum: 
                                board[y][i-dx] = -1
                            y += 1; dx += 1
        
        dfs(board, 0)
        # Format
        rem = [ x for x in range(n) ] + [-1]
        for x in range(len(res)):
            for i in range(len(res[x])):
                res[x][i] = [ "." if x in rem else x for x in res[x][i] ]
                res[x][i] = ''.join(res[x][i])
            
        return res


   
# 4th attempt: 88th percentile in speed
"""
The key idea to this problem and the initial solution came quickly. The real learning came from this attempt. 
This
problem is a fantastic illustration of backtracking. 

1) Backtracking is more general than DFS, but often involves DFS as it does here
2) The art is in coming up with a concise representation  of the problem (board in this case), efficiently 
trying a line of thought and efficiently reversing it before trying another path.

The goal is to think of what the absolute simplest representation we can reduce the problem too. Like
finding the minimum state in ract.

In this case...as we march through the columns (or rows equivalently), we don't actually need the whole
board. We can do just fine with 3 columns worth...one for the columns and two for the diagonals.
The key step: say we dropped a king in row 1 of column 1. No say we taking car of row 2. Then the
unavailable diagonal spit is going to be (cur col - prev col) + prev place = (2 - 1) + 1 = 2. Therefore,
we know the diagonal impact of previous placements given the current column number. 

Random notes on bitwise operators:
Recall: & -> bitwise and...so x & 1 is always going to be 1 or 0...so, this is just an obtuse
(but fast) even or odd operator. 
And...>> is bit shifting...so x >> 1 is the same as // 2.

While these can produce speedup, I think the decrease in readbility/maintainabiliy frequently isn't
worth it...a key benefit of python is supposed to be clarity. We might as well use Java or C++ if
speed is so critical. 

Important note on python array referencing:
Note that it's path + [createRow(j)] works in the dfs call, because python makes a new list
when concatenation is used. This is why we don't have to delete anything from the list after the
dfs call. 
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def createRow(j):
            return '.'*j + 'Q' + '.'*(n-j-1)
        
        def dfs(i, path):
            nonlocal ans, rows, diagU, diagD
            if i >= n:
                ans.append(path)
                return
            
            for j in range(n):
                if j in rows: continue
                if j-i in diagU: continue
                if j+i in diagD: continue
                rows.add(j); diagU.add(j-i); diagD.add(j+i)
                dfs(i+1, path + [createRow(j)] )
                rows.remove(j); diagU.remove(j-i); diagD.remove(j+i)
                
        
        ans, rows, diagU, diagD = [], set(), set(), set()
        dfs(0, [])
        return ans


# 5th attempt: 88th percentile in speed
# Interesting that just working with the original list (not using concat to make a new one)
# Doesn't yield a performance benefit. 
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def createRow(j):
            return '.'*j + 'Q' + '.'*(n-j-1)
        
        def dfs(i, path):
            nonlocal ans, rows, diagU, diagD
            if i >= n:
                ans.append(path[:])
                return
            
            for j in range(n):
                if j in rows: continue
                if j-i in diagU: continue
                if j+i in diagD: continue
                rows.add(j); diagU.add(j-i); diagD.add(j+i)
                path += [createRow(j)]
                dfs(i+1, path)
                del path[i]
                rows.remove(j); diagU.remove(j-i); diagD.remove(j+i)
                
        
        ans, rows, diagU, diagD = [], set(), set(), set()
        dfs(0, [])
        return ans