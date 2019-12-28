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


#include <vector>
#include <queue>
#include <utility>
#include <iostream>

class Solution {
// BFS solution. 12ms 92nd percentile.
public:
    int numIslandsBFS(std::vector<std::vector<char>>& grid) {
        int n = grid.size(), m = n ? grid[0].size() : 0, numberOfIslandsSunk = 0, offsets[] = {0, 1, 0, -1, 0};

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '1') {
                    numberOfIslandsSunk++;
                    std::queue<std::pair<int, int>> q;
                    grid[i][j] = '0';
                    q.push({i, j});
                    while (!q.empty()) {
                        std::pair<int, int> current = q.front();
                        q.pop();
                        for (int k = 0; k < 4; k++) {
                            int neighborI = current.first + offsets[k], neighborJ = current.second + offsets[k + 1];
                            if (0 <= neighborI && neighborI < n && 0 <= neighborJ && neighborJ < m && grid[neighborI][neighborJ] == '1') {
                                grid[neighborI][neighborJ] = '0';
                                q.push({neighborI, neighborJ});
                            }
                        }
                    }
                }
            }
        }
    
        return numberOfIslandsSunk;
    } 




// DFS solution. 12ms. 92nd percentile: 
public:
    int numIslandsDFS(std::vector<std::vector<char>>& grid) {
        int n = grid.size(), m = n ? grid[0].size() : 0, numberOfIslandsSunk = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '1') {
                    numberOfIslandsSunk++;
                    sinkIsland(grid, i, j);
                }
            }
        }

        return numberOfIslandsSunk;
    }

private:
    void sinkIsland(std::vector<std::vector<char>>& grid, int i, int j) {
        int n = grid.size(), m = n ? grid[0].size() : 0;
        if (0 <= i && i < n && 0 <= j && j < m && grid[i][j] == '1') {
            grid[i][j] = '0';

            sinkIsland(grid, i - 1, j);
            sinkIsland(grid, i + 1, j);
            sinkIsland(grid, i, j - 1);
            sinkIsland(grid, i, j + 1);
        }
    }
};




int main(int argc, const char* argv[]) {
    std::vector<std::vector<char>> grid {{'1','1','1','1','0'},{'1','1','0','1','0'},{'1','1','0','0','0'},{'0','0','0','0','0'}};
    Solution s;
    int result = s.numIslandsBFS(grid); 
    std::cout << "BSF result: \n" << result << "\n\n";

    grid = {{'1','1','1','1','0'},{'1','1','0','1','0'},{'1','1','0','0','0'},{'0','0','0','0','0'}};
    result = s.numIslandsDFS(grid);
    std::cout << "DFS result: \n" << result << "\n\n";
    return 0;
}

/*
Notes:

Note the offsets trick for dealing with neighbors in BFS. Compact trick.

*/