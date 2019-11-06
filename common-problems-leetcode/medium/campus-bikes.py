"""

On a campus represented as a 2D grid, there are N workers and M bikes, with N <=
M. Each worker and bike is a 2D coordinate on this grid.                        

Our  goal  is  to  assign  a  bike to each worker. Among the available bikes and
workers,  we choose the (worker, bike) pair with the shortest Manhattan distance
between  each  other, and assign the bike to that worker. (If there are multiple
(worker,  bike)  pairs  with the same shortest Manhattan distance, we choose the
pair  with  the smallest worker index; if there are multiple ways to do that, we
choose  the  pair  with  the  smallest bike index). We repeat this process until
there are no available workers.                                                 

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x
- p2.x| + |p1.y - p2.y|.                                                        

Return  a  vector  ans of length N, where ans[i] is the index (0-indexed) of the
bike that the i-th worker is assigned to.                                       

                                                                                

Example 1:                                                                      

Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]                           

Output: [1,0]                                                                   

Explanation:                                                                    

Worker  1  grabs  Bike  0  as  they  are closest (without ties), and Worker 0 is
assigned Bike 1. So the output is [1, 0].                                       

Example 2:                                                                      

Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]               

Output: [0,2,1]                                                                 

Explanation:                                                                    

Worker 0 grabs Bike 0 at first. Worker 1 and Worker 2 share the same distance to
Bike  2,  thus Worker 1 is assigned to Bike 2, and Worker 2 will take Bike 1. So
the output is [0,2,1].                                                          

                                                                                

Note:                                                                           

0 <= workers[i][j], bikes[i][j] < 1000                                          

All worker and bike locations are distinct.                                     

1 <= workers.length <= bikes.length <= 1000                                                                                                              

"""

# 712ms. 94th percentile.
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = [ [] for _ in range(2001) ]
        
        for workerIndex, (workerX, workerY) in enumerate(workers):
            for bikeIndex, (bikeX, bikeY) in enumerate(bikes):
                manhattanDistance = abs(workerX - bikeX) + abs(workerY - bikeY)
                distances[manhattanDistance].append( (workerIndex, bikeIndex) )
        
        usedBikes = set()
        assignments = [-1]*len(workers)
        for distance in distances:
            for workerIndex, bikeIndex in distance:
                if assignments[workerIndex] == -1 and bikeIndex not in usedBikes:
                    usedBikes.add(bikeIndex)
                    assignments[workerIndex] = bikeIndex
        
        return assignments

"""

Notes:

Brute force would be to calculate the manhattan distances between all
biker-worker combinations. Then we put those into a priority queue.
Then we keep popping off distances until there are none left. If 
we pop off a distance for a worker or bike that has already been accounted
for, we just continue to the next distance. 
^This is O(N^2)

What else could we do?


O(M*N) space and time solution...
This is a great time to use bucket sort. See notes on bucket sort for specifics.

The key info here is the limit on the size of the grid. It be at most 1000 by 1000.
In this case the max distance is between (0,0) and (1000,1000), which is a
manhattan distance of 2000. 

We assume that the bikes and workers are uniformly distributed across the range
of possible values. 

Given this, we can define buckets based on distance, generate distances for each
pair of bikes and workers, and drop them into the corresponding buckets.

Normally with bucket sort we would have to sort the individual buckets. Here we 
aren't doing that as every value in a given bucket has the same distance, they
only differ in terms of the worker and bike indices. 

So we just dump all the distances into their appropriate indices, then we loop
through them and generate the final assignments. We skip any worker-bike pair
pair that has a worker and/or bike that was already used in a different assignment. 

"""