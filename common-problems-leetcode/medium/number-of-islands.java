/*
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is 
formed by connecting adjacent lands horizontally or vertically. You may assume all four 
edges of the grid are all surrounded by water.

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
*/


// 99th percentile
class Solution {
    private char[][] g;
    
    public int numIslands(char[][] grid) {
        int numberOfIslandsFound = 0;
        g = grid;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    numberOfIslandsFound++;
                    sinkIsland(i, j);
                }
            }
        }
        return numberOfIslandsFound;
    }
    
    private void sinkIsland(int i, int j) {
        if (i < 0 || i == g.length || j < 0 || j == g[0].length || g[i][j] != '1')
            return;
        g[i][j] = '0';
        sinkIsland(i + 1, j); sinkIsland(i - 1, j); sinkIsland(i, j + 1); sinkIsland(i, j - 1);
        return;
    }
}