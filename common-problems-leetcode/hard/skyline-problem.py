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
# 128ms. 89 percentile.
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        startEvents = [ (L, -H, R) for L,R,H in buildings ]
        endEvents   = list({ (R, 0, None) for _,R,_ in buildings })
        events = sorted(startEvents + endEvents)
        pq = [(0, float("inf"))]
        res = [ [0,0] ]
        
        for eventTime, negEventHeight, eventEnd in events:
            while pq[0][1] <= eventTime:
                heapq.heappop(pq)
            if negEventHeight != 0:
                heapq.heappush(pq, (negEventHeight, eventEnd))
            if abs(pq[0][0]) != res[-1][1]:
                res.append([eventTime, -pq[0][0]])
        
        return res[1:]

"""
Notes:
Seems like a computational geometry problem. Goal is to 
find the overlapped image basically...specifically, we are 
to describe this by identifying the far left coordinates of 
each line segment. 

The classic solution to this problem involves divide and 
conquer and a cool merge sort algo. I find a priority queue
solution more natural though. 


Intuition:

Instead of thinking of buildings, we think in terms of "events". An event is the start or the end of a building. 
We make a list of our events. Each event is represented by a tuple where the first element indicates the location of
the event, the second is the height, and the third is the end of the events duration. The end of a building is
indicated by a height 0 and a 0 length duration.

We sort the events chronologically..that is left to right

Queue invariant:
-gives the tallest building left of the current event that hasn't ended yet. This could be current building.

The while loop maintains this invariant. It's like saying "please show me the best you have" to the pq. 
The pq says "here's the best we have". You say "that doesn't fit my requirements. Whats the next best?".
So the pq tosses the old item and serves up another item. This continues until you have the best item that fits your 
requirements. Note the discarded items couldn't fit your later "requests" either because we move strictly to the right. 
Therefore there's no concern about discarding them permanently.

This pq and its invariant is all we need to construct our list.

The only locations where we could get a change in the overlapping heights are the starts and ends of buildings. Therefore
our list of events provides every location we could be interested in. 

The final step is to identify if there is a change at a given spot and to record what that change is. We already know the 
location where the change would take place (its the location of the event). We need to know what height to record if
any. Given two pieces of information we can figure this out:

1) What is the tallest building that hasn't ended yet
2) Is it a different height than the height of the last building on our list 

The pq provides 1. As for 2, we can simply look at the height of the last segment we recorded in our answer.

If 1 yields a height that satisfies 2, then we know at the current location, the superimposed heights have changed
and we record an answer.
"""