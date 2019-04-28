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

# 36th percentile
"""
Inefficient and unreadable...but fun two-liner
O(Nlog(n))
"""
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points = sorted([ [(point[0]**2 + point[1]**2)**.5, point[0], point[1] ] for point in points ])[0:K]
        return [ [point[1], point[2]] for point in points ]


# 41st percentile. 404 ms
"""
This should be much better than the first solution. This is O(N) on average.
Uses quicksort algo...idea is that after each partition, we know how many items left of
the partition are less than all the elements on the right. So keep partitioning until
we have K elements on the left. Basically we're taking advantage of the fact that
the items don't have to be returned in any order. 
"""
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not K: return []
        if len(points) <= K: return points
        points = [ ( (point[0]**2 + point[1]**2)**.5, point[0], point[1] ) for point in points ]
        
        def partition(arr, low, high):
            i = low-1
            
            for j in range(low, high+1):
                if arr[j] <= arr[high]:
                    i += 1
                    arr[j], arr[i] = arr[i], arr[j]

            return i
        
        
        def quicksort(arr, low, high):
            if low < high:
                p = partition(arr, low, high)
                
                # Done
                if p == K:
                    return
                
                # continue with the right side
                elif p < K:
                    quicksort(arr, p, high)
                
                # forget the right side, continue with the left
                elif p > K:
                    quicksort(arr, low, p-1)
                
        
        quicksort(points, 0, len(points)-1)
        return [ [ point[1], point[2], ]  for point in points[0:K] ]
        

# 90th percentile: 344 ms
"""
The second solution has better asymptotic complexity, but it looks like for 
test cases of these sizes, the constant time trump the benefits and a solution utilizing built
in features like this solution wins. 
"""
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda x: x[0]**2+x[1]**2)[0:K]

# 87th percenilte: 348 ms
# not a big diff..
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0]**2+x[1]**2)
        return points[0:K]