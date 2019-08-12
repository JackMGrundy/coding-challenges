/*
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
*/

// 1st attempt: 99th percentile. 52 ms. 
/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    if (grid === null || grid.length === 0) {
        return 0;
    }
    
    let identifyIsland = function(i, j) {
        if (0 <= i && i < grid.length && 0 <= j && j < grid[0].length && grid[i][j]==='1') {
            grid[i][j] = '0';
            
            identifyIsland(i+1, j);
            identifyIsland(i-1, j);
            identifyIsland(i, j+1);
            identifyIsland(i, j-1);
            
            return 1;
        }
        return 0;
    }
    
    let res = 0;
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            res += identifyIsland(i, j);
        }
    }
    
    return res;
};