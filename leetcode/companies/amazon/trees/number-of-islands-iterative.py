"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def processIsland(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j]=='1': 
                grid[i][j] = '0'
                map(processIsland, (i, i, i-1, i+1), (j-1, j+1, j, j))
                return(1)
            return(0)
        
        res = sum( [processIsland(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j]=='1'] )
        return(res)