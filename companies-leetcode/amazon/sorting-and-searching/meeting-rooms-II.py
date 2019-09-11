"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
# 76ms. 99.99 percentile.
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        starts = [ meeting[0] for meeting in intervals ]
        ends   = [ meeting[1] for meeting in intervals ]
        
        starts.sort()
        ends.sort()
        
        startsPointer, endsPointer = 0, 0
        roomsInUse = 0
        
        for startsPointer in range(len(intervals)):
            if starts[startsPointer] >= ends[endsPointer]:
                roomsInUse -= 1
                endsPointer += 1
            
            roomsInUse += 1
            
        return roomsInUse



# Simple prioirty queue approach:
# 96ms. 42nd percentile.
from heapq import *
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x: x[0])
        pq = []
        maxOverlap = 0
        
        for interval in intervals:
            start, end = interval
            while pq and pq[0] <= start:
                heappop(pq)
            heappush(pq, end)
            maxOverlap = max(maxOverlap, len(pq))
        

        return maxOverlap


"""
Notes:

Approach 1:
We sort the intervals by starts and then iterate through them. We keep a heap of end times. 

To maintain the heap:
Pop all the meetings from the heap that have end times before the start time of the current meeting (they have ended by the time the 
current meeting starts). Check the size of the heap at each iteration for the max number of rooms simultaneously used. 

Complexity: Nlog(N)...log(n) for each heap operation and n meetings.


Aproach 2:
Separate starts / ends and sort them ascending. We keep incrementing the number of rooms in use as long as we haven't seen a stop time. 
When we do see a start after an ending, keep the number of rooms in use the same...we're effectively popping the one that ended, but
we're also adding a new meeting. 

This can seem unintuitive because now our number of rooms is monotonically increasing...
In approach 1, we keep popping ends until all expired meetings are gone. 
In approach 2 we're effectively removing 1 end for every start after an end. So they are constantly either balancing out, or we have a new start
that precedes the last end. 

Note that in this approach we are iterating through starts and only iterating through ends when we need to...so we don't have to process all of the
ends. 

Example


------------
  --------
   ------
    ---
             ------
                     -----
                            ------
                                    -------
                                     -----
                                      ----
                                       ----
                                       ---

In this case we're going to quickly get up to 4 concurrent rooms. Then we have 4 in a row where each time the new meeting has a start
after an ending from the first 4 we counted. So they balance and we just stay at 4. Then we have a chunk of 5 overlapping meetings. We already used
the start of the first one to pop an end from the first chunk of 4. The second, third, and fourth in the chunk of 5 are still stuck popping off
old ends. Finally, the last one's start is before the current ending, the first in meeting in the chunk, so we incremenet the number of required rooms
to 5. 

->CORE INTUITION. 
This shows that while each cluster can quickly increase the count, it also creates a back log of ends to get through. The only way we get through that 
back log, is to come across a chunk that's even big to process all of it and then continue increasing the count. 
                  
"""