"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

Accepted
196,724
Submissions
617,949
"""

# 72ms. 100th percentile in speed. O(N)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        newStart, newEnd = newInterval
        if newEnd < intervals[0][0]:
            return [newInterval] + intervals
        
        for i, [iStart, iEnd] in enumerate(intervals):
            if iStart <= newStart <= iEnd:
                return intervals[0:i] + self._mergeSortedIntervals( [[iStart, iEnd]] + [newInterval] + intervals[i+1:] )
            elif newStart <= iStart <= newEnd:
                return intervals[0:i] + self._mergeSortedIntervals( [newInterval] + intervals[i:] )
            elif 0 < i and intervals[i-1][0] <= newStart <= iStart: 
                return intervals[0:i] + [newInterval] + intervals[i:]
        
        return intervals + [newInterval]


    def _mergeSortedIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = [intervals[0]]
        
        for [start,end] in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start,end])
        
        return merged



# 96ms. 55 percentile
# I like this better because its cleaner. Although its O(Nlog(N))
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals += [newInterval]
        return self._mergeIntervals(intervals)

    def _mergeIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key = lambda x: x[0])
        merged = [intervals[0]]
        
        for interval in intervals[1:]:
            start, end = interval
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append(interval)
        
        return merged
        

"""
Notes:

1) The easiest solution is to just append the new interval and run merge intervals.
    Only issue is that this O(Nlon(N)) and we could get a O(N) solution since
    the list is already sorted.

2) Getting a O(N) solution.
    First check is the newInterval belongs at the front of the list.
    Then iterate through the intervals. There are three cases:
    1) The new intervals start is contained in the current interval
        --------------  New interval
    ------------        Current interval

    2) The new interval's end is contained in the current interval. Equivalenty, the current interval's
    start is contained in the new interaval

    ----------            new interval
        -------------     current interval

    3 The new interval is completely between old intervals

    ---------                           Interval before current
            ---------                New interval
                        -----------   Current interval

    We just check for each along the way. In case of the first two, we need to merge the new interval in.
    The private _mergeSortedIntervals function can be used in both cases.

    If we get to the end, it can only mean the new interval goes at the very end. 
"""