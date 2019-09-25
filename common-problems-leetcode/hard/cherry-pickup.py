"""
In a N x N grid representing a field of cherries, each cell is one of three possible integers.

 

0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.
 

Your task is to collect maximum number of cherries possible by following the rules below:

 

Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.
 

 

Example 1:

Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
Output: 5
Explanation: 
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
 

Note:

grid is an N by N 2D array, with 1 <= N <= 50.
Each grid[i][j] is an integer in the set {-1, 0, 1}.
It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.
 

Accepted
12.8K
Submissions
41.2K
"""

# Top down approach
# 832ms. 60 percentile.
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        N = len(grid)
        memo = [ [ [None for i in range(N)] for j in range(N) ] for k in range(N) ]
        
        def fillDp(r1, c1, c2):
            r2 = r1 + c1 - c2
            
            # Out of bounds
            if r1 == N or c1 == N or r2 == N or c2 == N:
                return -float("inf")
            # Thorn in the way
            elif grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -float("inf")
            # Hit the bootom right corner
            # Note that if one person did, and we're not out of bounds,
            # that means the other person successfully got to the bottom right too
            elif r1 == c1 == N-1:
                return grid[r1][c1]
            elif memo[r1][c1][c2] is not None:
                return memo[r1][c1][c2]
            else:
                # Counter the cherries in current cells
                ans = grid[r1][c1]
                if (r1, c1) != (r2, c2):
                    ans += grid[r2][c2]
                
                ans += max( fillDp(r1+1, c1, c2), fillDp(r1+1, c1, c2+1), \
                            fillDp(r1, c1+1, c2), fillDp(r1, c1+1, c2+1)  )
            
                memo[r1][c1][c2] = ans
                return ans
            
        return max(0, fillDp(0, 0, 0))


# 576. 95 percentile.
# This is the kind of moment that makes me love python. Built in lru_cache decorator
# boosts this like no other.
from functools import lru_cache
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        N = len(grid)
        
        @lru_cache(maxsize=None)
        def fillDp(r1, c1, c2):
            r2 = r1 + c1 - c2
            
            # Out of bounds
            if r1 == N or c1 == N or r2 == N or c2 == N:
                return -float("inf")
            # Thorn in the way
            elif grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -float("inf")
            # Hit the bootom right corner
            # Note that if one person did, and we're not out of bounds,
            # that means the other person successfully got to the bottom right too
            elif r1 == c1 == N-1:
                return grid[r1][c1]
            else:
                # Counter the cherries in current cells
                ans = grid[r1][c1]
                if (r1, c1) != (r2, c2):
                    ans += grid[r2][c2]
                
                ans += max( fillDp(r1+1, c1, c2), fillDp(r1+1, c1, c2+1), \
                            fillDp(r1, c1+1, c2), fillDp(r1, c1+1, c2+1)  )

                return ans
            
        return max(0, fillDp(0, 0, 0))



# Bottom up is interesting but don't have time to implement rn...



"""
Notes:

Very cool problem. Not sure how anyone would ever nail this in 30 mins or less without doing an enormous amount
of practice for related problems ahead of time...but still very cool problem. 


The first key thing to note is that we don't have to actually go there and back. Instead we can just 
think about sending two paths there and picking up as many cherries utilizing these two paths as we 
possibly can. It also simplifies the whole right/left and up/down bit...if you reverse time for the return 
trip, then all those left steps turn into right steps and same for the up/down...so now we're just dealing 
with two paths that are only down and right. 

Next step....brute force would be to enumerate all the paths and then try all pairs of them. We could do 
this with some sort of DFS and store every possible path and path-value. This can become excessively 
complicated, because we can't consider them in a vacuum. Two different paths may pick up the same cherry...

Much better/simpler approach is dp. 


Top Down:
Here's the idea:
Person 1 has taken r1 + c1 steps total at time t
Person 2 has taken r2 + c2 steps total at time t. 
So we have r1 + c1 = r2 + c2  =>   r2 = r1 + c1 - c2
=> given 3/4 of the step values, we know all 4...more pertinently, 3 values can serve as a sort of id. 

so we form a dp memo that has 3 dimensions, and we fill this cube in (for a O(N^3) solution. 

Now for the key part...how to relate the subproblems...
Each spot in the cube corresponds to a specific time step...meaning that when we move to a different 
element, we need to increase the steps of both paths by 1 to maintain that time step consistency. And 
we are only allowed to move down and to the right. So in other words:

Assuming the three dimensions of dp correspond with (implicit r2) r1 c1 c2

From                          dp[i][j][k]
We can go to       dp[i+1][j][k]      dp[i][j+1][k]   dp[i][j+1][k+1]   dp[i+1][j][k+1]
Correspondng to      down,down         right,down        right,right      down,right
(person1 person2)


=> 

dp[i][j][k]   =   (#cherries at the two spots) + max(dp[i+1][j][k],
 													 dp[i][j+1][k],
 													 dp[i][j+1][k+1],
 													 dp[i+1][j][k+1])

The last notes are just boundary conditions:
In the dp function, you need to calculate r2 from the three input variables. 
If any of the 4 = N are on the boundary, or either of the corresponding squares are -1,
then just return -Infinity so that those solutions are effectively axed.

If you hit the bottom left square then you can just return that value (it's the end)

If you've already calculated this path, just return the value (typical dp)

Otherwise, calculate it with the equation above, and store the result. This is also the part that spins 
up the recursive calls. 



Bottom up:
I think this way is harder...
But, it's also a bit better in that its O(N^2) memory...this makes sense considering that to calculate 
values for t, you just need the values from t-1...And since we're building from the bottom we don't have 
to keep everything and then build backwards. 

Building on this...we're explicitly keeping track of t now. That means that if we know one component of 
each of the two people's moves (down or right), we know the other. Explciitly

t - r1 = c1      and       t - r2 = c2
So our dp is 
dp[c1][c2]

So our dp is now just two dimensions. How to relate a dp element to other elements?

dpCurrentTime[c1][c2] = max ( dpLastTime[c1-1][c2],
 							  dpLastTime[c1][c2-1],
 							  dpLastTime[c1-1][c2-1],
 							  dpLastTime[c1][c2]
								)

Which correspond with 

								r1       r2        c1       c2
dpLastTime[c1-1][c2]            r1       r2-1      c1-1     c2
dpLastTime[c1][c2-1]            r1-1     r2        c1       c2-1
dpLastTime[c1-1][c2-1]          r1       r2        c1-1     c2-1
dpLastTime[c1][c2]              r1-1     r2-1      c1       c2

The last one can look a bit weird at first because it looks we're saying there was no
movement...but it's implicit in the design. 


How do we fill in the dp arrays? In top down we didn't need loops because we used recursive calls. Now 
we need loops. We need one for t, and then we need two more for up/down and left/right. We have two N^2 
arrays for t-1 and for t. Basically for each t, we transfer the last t dp array to the t-1 dp array. Then
 with the two inner loops, we consider every possible combination of moves for the new time step. 

In my opinion, the hard part of this approach is figuring out the ranges of the loops... 
Time loop: 1 to 2N-1 ....this intuitively makes sense when you realize that you could take N steps to the
 right and then N steps down...for a maximum of 2N time steps
Two inner loops:
max(0, t-(N-1)) to min(N-1, t)+1

Lower bound: we can't be in a negative spot. As time goes on, we have to get farther away from our starting 
point...we can't go backwards...say we took the first N-1 steps to the right. At the point we're at the edge 
and the only way to go is down. So now we don't have to worry about filling in the 0th row...and our handy 
loop will start at N-(N-1) = 1! 

Upper bound: At t = 2, there's no need to fill in the whole array...we could have only gone 2 steps...however,
 after we get to N-1, we could be in a square at the bottom or the side, so we need to check to N-1.

Done with the loop ranges. How do we fill in the elements? At each element, we just ignore it if either of 
the two component squares are -1 (we just continue in the loop)...note we can do this because we intialize 
the dp arrays with -Infinities, so continuing is the same as leaving that value there...so later max calls 
will just skirt over it. 

Then we can actually value that square. The value of the element is equal to the number of cherries in the 
two component squares (make sure the squares aren't the same) 
+
the max of the 4 values enumerate earlier...note the need to make sure we're not considering negative values
with the negatives...

And boom! That's it! 

"""