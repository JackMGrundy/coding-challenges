/*
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.


Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

 

Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 

Constraints:

-300 <= x, y <= 300
0 <= |x| + |y| <= 300
*/


// 77th percentile bfs
// using pairs
class Solution {
    private final int[][] MOVES = new int[][] {{2, 1}, {1, 2}, {-1, 2}, {-2, 1}, {-2, -1}, {-1, -2}, {1, -2}, {2, -1}};
    
    public int minKnightMoves(int x, int y) {
        x = Math.abs(x);
        y = Math.abs(y);
        
        Queue<Pair<Integer, Integer>> q = new LinkedList();
        Set<Pair<Integer, Integer>> visited = new HashSet();
        Pair<Integer, Integer> start = new Pair(0, 0);
        q.add(start);
        visited.add(start);
        int moves = 0;
        
        while (0 < q.size()) {
            final int size = q.size();
            
            for (int i = 0; i < size; i++) {
                Pair<Integer, Integer> cur = q.remove();
                final int curX = cur.getKey();
                final int curY = cur.getValue();
                if (curX == x && curY == y) return moves;
                
                for (int[] move : MOVES) {
                    final int nextX = curX + move[0];
                    final int nextY = curY + move[1];
                    Pair<Integer, Integer> nextMove = new Pair(nextX, nextY);
                    
                    if (nextX < -2 || nextY < -2) continue;
                    if (1 < nextX - x || 1 < nextY - y) continue;
                    if (visited.contains(nextMove)) continue;
                    
                    visited.add(nextMove);
                    q.add(nextMove);
                }
            }
            
            moves++;
        }
        return -1;
    }
}


// 70th percentile
class Solution {
    private final int[][] MOVES = new int[][] {{2, 1}, {1, 2}, {-1, 2}, {-2, 1}, {-2, -1}, {-1, -2}, {1, -2}, {2, -1}};
    
    public int minKnightMoves(int x, int y) {
        x = Math.abs(x);
        y = Math.abs(y);
        
        Queue<int[]> q = new LinkedList();
        Set<String> visited = new HashSet();
        int[] start = {0, 0};
        q.add(start);
        visited.add("0,0");
        int moves = 0;
        
        while (0 < q.size()) {
            final int size = q.size();
            
            for (int i = 0; i < size; i++) {
                int[] cur = q.remove();
                final int curX = cur[0];
                final int curY = cur[1];
                if (curX == x && curY == y) return moves;
                
                for (int[] move : MOVES) {
                    final int nextX = curX + move[0];
                    final int nextY = curY + move[1];
                    int[] nextMove = { nextX, nextY };
                    
                    if (nextX < -2 || nextY < -2) continue;
                    if (1 < nextX - x || 1 < nextY - y) continue;
                    if (visited.contains(nextX + "," + nextY)) continue;
                    
                    visited.add(nextX + "," + nextY);
                    q.add(nextMove);
                }
            }
            
            moves++;
        }
        return -1;
    }
}


/*
Pairs vs int[2] make basically no difference in performance
they compile down to basically the same thing...

*/