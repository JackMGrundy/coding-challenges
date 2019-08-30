"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""
# bfs. 148ms. 88th percentile.
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        best = 0
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if (i, j) in seen:
                    continue
                elif grid[i][j] == 1:
                    curBest = 0
                    q = collections.deque([(i,j)])
                    seen.add( (i,j) )
                    while q:
                        cI, cJ = q.popleft()
                        curBest += 1
                        
                        if cI+1 < len(grid) and (cI+1,cJ) not in seen and grid[cI+1][cJ]==1:
                            q.append( (cI+1, cJ) )
                            seen.add( (cI+1, cJ) )
                        if cJ+1 < len(grid[0]) and (cI,cJ+1) not in seen and grid[cI][cJ+1]==1:
                            q.append( (cI, cJ+1) )
                            seen.add( (cI, cJ+1) )
                        if  cI-1 >= 0 and (cI-1,cJ) not in seen and grid[cI-1][cJ]==1:
                            q.append( (cI-1, cJ) )
                            seen.add( (cI-1, cJ) )
                        if cJ-1 >= 0 and (cI,cJ-1) not in seen and grid[cI][cJ-1]==1:
                            q.append( (cI, cJ-1) )
                            seen.add( (cI, cJ-1) )
                    
                    best = max(curBest, best)
                            
                else:
                    seen.add( (i,j) )
        
        return best



# recursive dfs. 172ms. 38th percentile.
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(i, j):
            if (len(grid) <= i) or (i < 0) or (len(grid[0]) <= j) or (j < 0) or (grid[i][j] == 0):
                return 0 
            else:
                grid[i][j] = 0
                return 1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)
        
        areas = [ dfs(i,j) for i in range(len(grid)) for j in range(len(grid[0])) ]
        return max(areas) if areas else 0