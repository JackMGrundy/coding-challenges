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
# 268ms.
# 90 percentile.
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
        intervals = self._mergeIntervals(intervals)
        gaps = []
        for i in range(len(intervals)-1):
            if intervals[i].end < intervals[i+1].start:
                gaps.append(Interval(intervals[i].end, intervals[i+1].start))
        return gaps
    
        
    def _mergeIntervals(self, intervals):
        if not intervals:
            return []
        
        merged = [intervals[0]]
        
        for interval in intervals[1:]:
            start, end = interval.start, interval.end
            if start <= merged[-1].end:
                merged[-1].end = max(merged[-1].end, end)
            else:
                merged.append(interval)

        return merged

"""
Notes:

    There are a few approaches to solving this. I like this one^ for the simplicitly. 
    You just flatten the intervals into a single list, merge, and then identify the gaps.
    The downside is the sort operation which makes it Nlog(N). We're giving up the benefit
    that the lists are initially sorted. To make this faster, we could replace the sorting
    with a merge type operation that combines the employee's schedules in sorted order in
    linear time. I like the simplicitly of the single line for sorting though...
"""