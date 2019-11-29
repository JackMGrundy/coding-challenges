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

// 4ms. 98 percentile.
// Recursive
class Solution {
    
    public List<List<Integer>> pacificAtlantic(int[][] matrix) {
        if (matrix.length == 0) {
            return new ArrayList<>();
        }
        
        int N = matrix.length;
        int M = matrix[0].length;
        
        boolean[][] canReachPacific = new boolean[N][M];
        boolean[][] canReachAtlantic = new boolean[N][M];
        
        for (int i = 0; i < N; i++) {
            dfs(i, 0, -1, canReachPacific, matrix, N, M);
            dfs(i, M - 1, -1, canReachAtlantic, matrix, N, M);
        }
        
        for (int j = 0; j < M; j++) {
            dfs(0, j, -1, canReachPacific, matrix, N, M);
            dfs(N - 1, j - 1, -1, canReachAtlantic, matrix, N, M);
        }
        
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (canReachPacific[i][j] && canReachAtlantic[i][j]) {
                    List<Integer> result = new ArrayList<Integer>();
                    result.add(i);
                    result.add(j);
                    results.add( result );
                }
            }
        }
            
        return results;
    }
    
    private void dfs(int i, int j, int parentHeight, boolean[][] reachable, int[][] matrix, int N, int M) {
        if ( !(0 <= i && i < N && 0 <= j && j < M) ) {
            return;
        }
        
        if (matrix[i][j] < parentHeight) {
            return;
        }
        
        if (reachable[i][j]) {
            return;
        }
        
        reachable[i][j] = true;
        dfs(i + 1, j, matrix[i][j], reachable, matrix, N, M);
        dfs(i - 1, j, matrix[i][j], reachable, matrix, N, M);
        dfs(i, j + 1, matrix[i][j], reachable, matrix, N, M);
        dfs(i, j - 1, matrix[i][j], reachable, matrix, N, M);
    }
}





// 10ms. 23 percentile.
// Recursive...slow manual management of Tuple class and stack...
class Tuple {
    int i;
    int j;
    
    public Tuple(int i, int j) {
        this.i = i;
        this.j = j;
    }
    
}

class Solution {
    int[][] neighborDeltas = { {0, 1}, {0, -1}, {1, 0}, {-1, 0} };
    
    public List<List<Integer>> pacificAtlantic(int[][] matrix) {
        if (matrix.length == 0) {
            return new ArrayList<>();
        }
        
        int N = matrix.length;
        int M = matrix[0].length;
        
        boolean[][] canReachPacific = new boolean[N][M];
        boolean[][] canReachAtlantic = new boolean[N][M];
        
        for (int i = 0; i < N; i++) {
            dfs(i, 0, canReachPacific, matrix, N, M);
            dfs(i, M - 1, canReachAtlantic, matrix, N, M);
        }
        
        for (int j = 0; j < M; j++) {
            dfs(0, j, canReachPacific, matrix, N, M);
            dfs(N - 1, j, canReachAtlantic, matrix, N, M);
        }
        
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (canReachPacific[i][j] && canReachAtlantic[i][j]) {
                    ArrayList<Integer> result = new ArrayList<Integer>();
                    result.add(i);
                    result.add(j);
                    results.add( result );
                }
            }
        }
            
        return results;
    }
    
    private void dfs(int startI, int startJ, boolean[][] reachable, int[][] matrix, int N, int M) {
        Stack<Tuple> stack = new Stack<Tuple>();
        stack.push(new Tuple(startI, startJ));
        
        while (0 < stack.size()) {
            Tuple current = stack.pop();
            int i = current.i;
            int j = current.j;
            reachable[i][j] = true;
            
            for (int[] deltas : neighborDeltas) {
                int nI = i + deltas[0];
                int nJ = j + deltas[1];
                if (0 <= nI && nI < N && 0 <= nJ && nJ < M &&
                    !reachable[nI][nJ] &&
                    matrix[i][j] <= matrix[nI][nJ]) {
                    stack.push( new Tuple(nI, nJ) );
                }
            }
        }
    }
}


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