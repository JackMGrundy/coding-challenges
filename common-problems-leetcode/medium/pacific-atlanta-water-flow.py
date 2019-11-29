"""
Given  an  m x n matrix of non-negative integers representing the height of each
unit  cell in a continent, the "Pacific ocean" touches the left and top edges of
the matrix and the "Atlantic ocean" touches the right and bottom edges.         

Water can only flow in four directions (up, down, left, or right) from a cell to
another one with height equal or lower.                                         

Find  the  list of grid coordinates where water can flow to both the Pacific and
Atlantic ocean.                                                                 

Note:                                                                           

The order of returned grid coordinates does not matter.                         

Both m and n are less than 150.                                                 

                                                                                

Example:                                                                        

Given the following 5x5 matrix:                                                 

  Pacific ~   ~   ~   ~   ~                                                     

       ~  1   2   2   3  (5) *                                                  

       ~  3   2   3  (4) (4) *                                                  

       ~  2   4  (5)  3   1  *                                                  

       ~ (6) (7)  1   4   5  *                                                  

       ~ (5)  1   1   2   4  *                                                  

          *   *   *   *   * Atlantic                                            

Return:                                                                         

[[0,  4],  [1,  3],  [1,  4],  [2,  2],  [3, 0], [3, 1], [4, 0]] (positions with
parentheses in above matrix).                                                   

                                                                                

Accepted                                                                        

55.5K                                                                           

Submissions                                                                     

143.2K                                                                          

"""
# 312ms. 81 percentile.
from collections import deque
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        
        N, M = len(matrix), len(matrix[0])
        canReachPacific = [ [ False for _ in range(M) ] for _ in range(N) ]
        canReachAtlantic = [ [ False for _ in range(M) ] for _ in range(N) ]
        
        def dfs(startI, startJ, reachable):
            stack = [ (startI, startJ) ]
            while stack:
                i, j = stack.pop()
                reachable[i][j] = True
                neighbors = [ (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1) ]

                for neighborI, neighborJ in neighbors:
                    if 0 <= neighborI < N and 0 <= neighborJ < M \
                        and not reachable[neighborI][neighborJ] \
                        and matrix[i][j] <= matrix[neighborI][neighborJ]:
                        stack.append( (neighborI, neighborJ) )

        for column in range(M):
            dfs(0, column, canReachPacific)
            dfs(N-1, column, canReachAtlantic)
        
        for row in range(N):
            dfs(row, 0, canReachPacific)
            dfs(row, M - 1, canReachAtlantic)
        
        # Might be a bit more readable for most readers to have a double for loop...but I personally
        # like this more.
        return [ [i, j] for i in range(N) for j in range(M) if canReachAtlantic[i][j] and canReachPacific[i][j] ]


"""
Notes:

We could run a dfs from every cell to identify if it can reach both oceans.
This timeouts though. So the goal is to cut down on the number of dfs calls.
To do this we can run one from each ocean edge instead. So now we have 4N calls instead of O(N^2)
To make it easier to read, I made a 2d array for each ocean that records which cells
can reach that ocean.
You could save some space by just making 1 2d array and incrementing cells by 1 for
each ocean that can be reached

"""