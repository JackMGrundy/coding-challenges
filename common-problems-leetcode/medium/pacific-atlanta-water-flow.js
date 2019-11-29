/*
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

*/

// 104ms. 74 percentile.
/**
 * @param {number[][]} matrix
 * @return {number[][]}
 */
var pacificAtlantic = function(matrix) {
    if (matrix.length === 0) {
        return [] 
    }
    
    const N = matrix.length;
    const M = matrix[0].length;
    
    let canReachPacific = [...Array(N)].map(_ => Array(M).fill(false));
    let canReachAtlantic = [...Array(N)].map(_ => Array(M).fill(false));
    
    let dfs = function(startI, startJ, reachable) {
        let stack = [ [startI, startJ] ];
        
        while (0 < stack.length) {
            let [i, j] = stack.pop();
            reachable[i][j] = true;
            
            let neighbors = [ [i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1] ];
            for ( [nI, nJ] of neighbors ) {
                if ( 0 <= nI && nI < N && 0 <= nJ && nJ < M &&
                     !reachable[nI][nJ] &&
                     matrix[i][j] <= matrix[nI][nJ]) {
                    stack.push( [nI, nJ] );
                }
            }
        }
    }

    for (let j = 0; j < M; j++) {
        dfs(0, j, canReachPacific);
        dfs(N - 1, j, canReachAtlantic);
    }
    
    for (let i = 0; i < N; i++) {
        dfs(i, 0, canReachPacific);
        dfs(i, M - 1, canReachAtlantic);
    }
    
    let canReachPacificAndAtlantic = [];
    for (let i = 0; i < N; i++) { 
        for (let j = 0; j < M; j++) {
            if (canReachPacific[i][j] && canReachAtlantic[i][j]) {
                canReachPacificAndAtlantic.push( [i, j] );
            }
        }
    }
    
    return canReachPacificAndAtlantic;
};

/*
Notes:

We could run a dfs from every cell to identify if it can reach both oceans.
This timeouts though. So the goal is to cut down on the number of dfs calls.
To do this we can run one from each ocean edge instead. So now we have 4N calls instead of O(N^2)
To make it easier to read, I made a 2d array for each ocean that records which cells
can reach that ocean.
You could save some space by just making 1 2d array and incrementing cells by 1 for
each ocean that can be reached

*/