"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Accepted
324,573
Submissions
921,724
"""
# 1st attempt: 76th percentile in speed
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution:
    def isOverlapping(self, in1, in2):
        l1, r1 = in1.start, in1.end
        l2, r2 = in2.start, in2.end
        res = False
        if l2 <= l1 and l1 <= r2: res = True
        if l2 <= r1 and r1 <= r2: res = True
        if l1 <= l2 and l2 <= r1: res = True
        if l1 <= r2 and r2 <= r1: res = True
        return res
    
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        if not intervals: return []
        intervals = sorted(intervals, key=lambda x: x.start)
        res = [ intervals[0] ]
        for interval in intervals[1:]:
            if self.isOverlapping(res[-1], interval):
                res[-1].end = max(interval.end, res[-1].end)
            else:
                res.append(interval)
        return res
            
        
            
# 2nd attempt: 98th percentile in speed
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution:
    
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        if not intervals: return []
        intervals = sorted(intervals, key=lambda x: x.start)
        res = [ intervals[0] ]
        for interval in intervals[1:]:
            if interval.start <= res[-1].end:
                res[-1].end = max(interval.end, res[-1].end)
            else:
                res.append(interval)
        return res

"""
Notes:

The great second solution is possible because of the initial sorting
During the iteration, we know that each successive interval has a start 
after that of the interval on top of the stack. Therefore, we can simply check if
the current interval's start is less than the end of the intervals on top 
of the stack.
"""