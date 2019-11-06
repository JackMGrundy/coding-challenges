/*

Given  an  2D  board,  count how many battleships are in it. The battleships are
represented with 'X's, empty slots are represented with '.'s. You may assume the
following rules:                                                                

You receive a valid board, made of only battleships or empty slots.             

Battleships  can only be placed horizontally or vertically. In other words, they
can  only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column),
where N can be of any size.                                                     

At  least  one  horizontal  or vertical cell separates between two battleships -
there are no adjacent battleships.                                              

Example:                                                                        

X..X                                                                            

...X                                                                            

...X                                                                            

In the above board there are 2 battleships.                                     

Invalid Example:                                                                

...X                                                                            

XXXX                                                                            

...X                                                                            

This  is an invalid board that you will not receive - as battleships will always
have a cell separating between them.                                            

Follow up:                                                                      

Could  you do it in one-pass, using only O(1) extra memory and without modifying
the value of the board?                                                         


*/

// 1ms. 94th percentile.
class Solution {
    public int countBattleships(char[][] board) {
        int m = board.length;
        if (m == 0) {
            return 0;
        }
        int n = board[0].length;
        int shipsCount = 0;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == '.') {
                    continue;
                }
                
                if (0 <= i - 1 && board[i - 1][j] == 'X') {
                    continue;
                }
                
                if (0 <= j - 1 && board[i][j - 1] == 'X') {
                    continue;
                }
                
                shipsCount++;
            }
        }
        
        return shipsCount;
    }
}



/*

Notes:

This is almost the num islands problem. The differentiating factors are
A) our inaability to change the board. 
B) there are no adjacent battleships

B is very helpful. It means we never have to deal with something like

. . x x
x x x x

^This would be ambiguous anyways

Ships must be horizontal or vertical. Because ships cannot be adjacet, any time
we see an X, if its neighbors are X, then the cells are all part of the same ship.

This allows us to reframe the problem. Instead we look at the problem as counting
the number of first cells in each ship, where the first cell is the leftmost/topmost
cell.

We can locally confirm that a cell is a first cell by checking if it has neighbors above
or to the left. Both cannot be true because of the no adjacent ships rules. Leftmost/topmost 
cells will have no neighbors. 

This leads us to the answer.

*/