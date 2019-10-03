"""
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time 
for all employees, also in sorted order.

Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation:
There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
 

Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
 

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not 
lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined.)

Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

Note:

schedule and schedule[i] are lists with lengths in range [1, 50].
0 <= schedule[i].start < schedule[i].end <= 10^8.
NOTE: input types have been changed on June 17, 2019. Please reset to default code definition to get 
new method signature.


Accepted
19.7K
Submissions
31.3K
"""

# 264ms.
# 95 percentile.
# O(N(Log(N)) where N is the number of intervals
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def employeeFreeTime(self, schedule: 'list<list<Interval>>') -> 'list<Interval>':
        intervals = [ interval for employeeSchedule in schedule for interval in employeeSchedule ]
        intervals.sort(key = lambda x: x.start)
        return self._gaps(intervals)
    
    def _gaps(self, intervals):
        if not intervals:
            return []
        
        gaps, previousEnd = [], intervals[0].end
        
        for interval in intervals[1:]:
            if previousEnd < interval.start:
                gaps.append(Interval(previousEnd, interval.start))
                previousEnd = interval.end
            else:
                previousEnd = max(previousEnd, interval.end)

        return gaps

# 284ms. 48 percentile.
# O(N(Log(C)) where N is the number of intervals and C is the number of employees
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import *
class Solution:
    def employeeFreeTime(self, schedule: 'list<list<Interval>>') -> 'list<Interval>':
        pq = []
        # Add each employee's first interval to the priority queue
        for listIndex,employeeSchedule in enumerate(schedule):
            heappush( pq, (employeeSchedule[0].start, employeeSchedule[0].end, listIndex, 0, employeeSchedule[0]) )
        
        # Merge the in
        overlaps = []
        while pq:
            start, end, listIndex, elementIndex, interval = heappop(pq)
            if overlaps and start <= overlaps[-1].end:
                overlaps[-1].end = max(overlaps[-1].end, end)
            else:
                overlaps.append(interval)
            
            if elementIndex + 1 < len(schedule[listIndex]):
                nextEvent = schedule[listIndex][elementIndex + 1]
                heappush(pq,  (nextEvent.start, nextEvent.end, listIndex, elementIndex+1, nextEvent) )
        
        freeTime = []
        for i in range(1, len(overlaps)):
            freeTime.append( Interval(overlaps[i-1].end, overlaps[i].start) )
        
        return freeTime


"""
Notes:

1)
    There are a few approaches to solving this. I like this one^ for the simplicitly. 
    We just flatten the intervals into a single list, merge, and during the merge
    process identify the gaps.
    The downside is the sort operation which makes it Nlog(N). We're giving up the benefit
    that the lists are initially sorted. To make this faster, we could replace the sorting
    with a merge type operation that combines the employee's schedules in sorted order in
    linear time. I like the simplicitly of the single line for sorting though...

2) The asymptotically better solution. Use a priority queue to get the next earliest interval
amongst the sorted lists of employees schedules. 
"""