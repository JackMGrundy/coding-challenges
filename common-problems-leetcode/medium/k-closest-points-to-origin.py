"""
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 

Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""


# 724ms 91 percentile
# Built ins
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda x: x[0]**2+x[1]**2)[0:K]


# 744ms 74th percentile
# Quick select
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points:
            return []
        if len(points) <= K:
            return points
        pointsWithDistances = [ (x[0]*x[0] + x[1]*x[1], x[0], x[1]) for x in points ]
        self.quickSelect(pointsWithDistances, K)
        kClosestPoints = [ (x[1],x[2]) for x in pointsWithDistances[0:K] ]
        return kClosestPoints
    

    def quickSelect(self, pointsWithDistances, K):
        return self._quickSelect(pointsWithDistances, 0, len(pointsWithDistances) - 1, K-1)
    

    def _quickSelect(self, pointsWithDistances, start, end, K):
        if start == end:
            return 
        
        partitionIndex = self._partition(pointsWithDistances, start, end)
        
        if partitionIndex == K:
            return
        elif K < partitionIndex:
            self._quickSelect(pointsWithDistances, start, partitionIndex - 1, K)
        else:
            self._quickSelect(pointsWithDistances, partitionIndex + 1, end, K)
    

    def _partition(self, pointsWithDistances, start, end):
        left = right = start
        
        m = left + (right - left)//2
        pointsWithDistances[m], pointsWithDistances[end] = pointsWithDistances[end], pointsWithDistances[m]
        
        while right < end:
            if pointsWithDistances[right][0] < pointsWithDistances[end][0]:
                pointsWithDistances[right], pointsWithDistances[left] = pointsWithDistances[left], pointsWithDistances[right]
                left += 1
            right += 1
        
        pointsWithDistances[left], pointsWithDistances[end] = pointsWithDistances[end], pointsWithDistances[left]
        
        return left
        

"""
Notes:

The first solution wins due to constant factors, but technically it's Nlog(N), while the second solution is O(N).
Note the second solution is constructed to be in place...one of the main benefits of quick sort...makes the code a bit more complicated though. 

See notes on quick select for second solution info. 
"""