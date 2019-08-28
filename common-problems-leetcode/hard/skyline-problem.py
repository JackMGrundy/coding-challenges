"""
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

Buildings  Skyline Contour
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
"""
# 132ms. 77the percentile.
from heapq import *
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        prevBestHeight = 0
        curBestHeight = 0
        lastX = -1
        res = []
        removed = collections.defaultdict(int)
        pq = []
        
        startsAndEnds = []
        for building in buildings:
            x, y, h = building
            startsAndEnds.append( (x, h, True) )
            startsAndEnds.append( (y, h, False) )
        
        startsAndEnds.sort()
        
        for marker in startsAndEnds:
            curX, h, isStart = marker
            
            if isStart:
                heappush(pq, -h)
            else:
                removed[h] += 1
            
            updatedHeight = False
            
            while not updatedHeight:
                curBestHeight = 0 if not pq else -pq[0]
                if removed[curBestHeight] > 0:
                    removed[curBestHeight] -= 1
                    heappop(pq)
                else:
                    updatedHeight = True

            if lastX == curX and res and res[-1][1] < curBestHeight:
                res.pop()
                prevBestHeight = 0 if not res else res[-1][1]
                lastX = 0 if not res else res[-1][0]
                
            if curBestHeight != prevBestHeight:
                res.append( [curX, curBestHeight] )
                prevBestHeight = curBestHeight
                lastX = curX
            
        
        return res













"""
Notes:
Seems like a computational geometry problem. Goal is to 
find the overlapped image basically...specifically, we are 
to describe this by identifying the far left coordinates of 
each line segment. 

The classic solution to this problem involves divide and 
conquer and a cool merge sort algo. The solution that 
immediately comes to my mind is a priority queue based 
solution:



Make tuples out of each x and y that are like:

(x/y value, height, flag of start or end)
Sort those. 

Make a pq for heights. Add 0 to the pq. 

Take the first tuple and start with that height. 

Make a hashtable to record counts of removed height

for each tuple
    If it is a start
        Add its height to the pq
    If it is an end:
        Increment the count of removed heights

    Peak the current best height in the pq
    Check if the best heigh has been removed as recorded by the 
    hash table. If so, decrement the hash table entry, pop the best
    height from the queue, and then get the next biggest height. 

    Deal with overlaps:
    if the current x/y matches that previous x/y and the height 
    of the current interval is greater than that of the last one 
    put on the result, pop the last one and roll back the lastX 
    and previous best height. 

    if the best height changed:
        Close off the previous interval and start a new one.



"""