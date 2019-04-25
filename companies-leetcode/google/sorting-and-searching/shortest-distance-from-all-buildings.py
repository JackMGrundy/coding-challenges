"""
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
"""
# Passes half the test cases and then to's
from collections import deque
class Solution:
     
    def shortestDistance(self, grid: List[List[int]]) -> int:
        
        def bfs(j, i, grid, numBuildings) -> int:
            q = deque( [(j, i, 0)] )
            m = len(grid); n = len(grid[0])
            visited = set()
            bestRoutes = {}
            # buildings = set()

            while q:
                j, i, d = q.popleft()
                visited.add( (j, i) )
                 
                # Found a building
                if grid[j][i]==1:
                    # We previously found a path to this building
                    if ( (j,i) in bestRoutes ):
                        bestRoutes[ (j,i) ] = min( bestRoutes[ (j,i) ], d)
                    # First time seeing this building
                    else:
                        bestRoutes[ (j,i) ] = d
                    
                
                # add children if we are on an empty square
                if grid[j][i] == 0:
                    for c in [ (j, i+1), (j, i-1), (j+1, i), (j-1, i) ]:
                        c_j, c_i = c
                        # Its a spot in bounds, that doesn't have an obstacle, that we haven't seen
                        if 0 <= c_j < m and 0 <= c_i < n and grid[c_j][c_i] in [0, 1] and c not in visited:
                            q.append( (c_j, c_i, d+1) )

            # Add up total distances
            
            # if we didn't find a path to every location, this spot is invalid
            if len(bestRoutes.keys()) < numBuildings:
                return -1
            
            res = 0
            for key, val in bestRoutes.items():
                res += val
                    
            return res
    
        res = float("inf")
        m = len(grid); n = len(grid[0])
        
        # Count buildings:
        numBuildings = 0
        for j in range(m):
            for i in range(n):
                if grid[j][i]==1: numBuildings += 1
        
        # Check each square
        for j in range(m):
            for i in range(n):
                if grid[j][i] != 0 : 
                    continue
                dist = bfs( j, i, grid, numBuildings )
                if dist == -1: continue
                res = min(res, dist)
        
        
        return res if res < float("inf") else -1



# 98th percentile
"""
Notes: the key idea behind this isn't too tricky, but it's a lot of work for an interview question

-The idea is that if we run a BFS from each spot, we can identify the shortest paths from that spot to each building.
Sum of those distances, and you have the value of that spot. Repeat this for every 0 spot and you can find the best one.
-You can speed things up drastically with a slight shift in logic. In stead of doing a bfs for every 0 spot, do one for every building.
During the bfs, every time you hit a new cell, tally how far it is from the building currently being examined. After repeating this
process for each building, the tallies will include all distances from all the buildings...just what we need.
^Note, that how useful this is depends on the ratio of 0's to 1's...these test cases seem to imply more 1's than 0's.
-A big speedup (prune technically...): since we're doing BFS's starting from buildings, we can tell quickly if one building
is not reachable from the others (just count up the total number of buildings reached from the current start point). If that's the case,
just return -1 immediately. This trick is the difference between being 33rd percentile and 98th (736ms vs 56ms)

"""
from collections import deque
class Solution:
     
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n, numBuildings = len(grid), len(grid[0]), sum(val for line in grid for val in line if val==1)
        res = float("inf")
        hits, dists = [ [0]*n for _ in range(m) ], [ [0]*n for _ in range(m) ]
        
        
        def bfs(startJ, startI, grid ) -> int:
            visited = [ [False]*n for _ in range(m) ]
            visited[startJ][startI], q, buildingsReached = True, deque( [(startJ, startI, 0)] ), 1

            while q:
                y, x, d = q.popleft()
                visited[y][x] = True
                for j, i in ((y, x+1), (y, x-1), (y+1, x), (y-1, x)):
                    if 0 <= j < m and 0 <= i < n and not visited[j][i] and grid[j][i]!=2:
                        visited[j][i] = True
                        
                        if grid[j][i]==1:
                            buildingsReached += 1
                        else:
                            q.append((j, i, d+1))
                            # Tally how far this spot is from the building we are searching from
                            dists[j][i] += d+1
                            # Tally how many buildings this spot is reachable from
                            hits[j][i] += 1
            
            return buildingsReached == numBuildings
                            

 
        # Complete a bfs search starting from each building
        for j in range(m):
            for i in range(n):
                if grid[j][i] == 1: 
                    if not bfs( j, i , grid ): return -1
        
        res = float("inf")
        for j in range(m):
            for i in range(n):
                if grid[j][i]==0 and hits[j][i]==numBuildings and dists[j][i]<res:
                    res = dists[j][i]
        
        return res if res < float("inf") else -1