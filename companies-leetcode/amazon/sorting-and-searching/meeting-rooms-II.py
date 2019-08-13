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
# First attempt - 5th percentile in speed and memory inefficient
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if intervals==[]: return(0)
        
        maxVal = max([ x.end for x in intervals ])
        counts = [ 0 for x in range(maxVal+1)]
        for interval in intervals:
            counts[interval.start]+=1
            counts[interval.end]-=1
        
        res = 0
        runningTotal = 0
        for c in counts:
            runningTotal += c
            if runningTotal > res: 
                res = runningTotal
            
        return(res)


# Second attemp: 80th percentile in speed, 5th percentile in memory
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if intervals==[]: return(0)
        
        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        starts.sort(reverse=True)
        ends.sort(reverse=True)
        res = 0
        runningTotal = 0
        while starts and ends:
            if starts[-1] < ends[-1]:
                runningTotal+=1
                starts.pop()
            elif starts[-1]==ends[-1]:
                starts.pop()
                ends.pop()
                continue
            else:
                runningTotal-=1
                ends.pop()
            if runningTotal>res: 
                res = runningTotal
        return(res)


# Third attempt: 99th percentile in speed. 5th percentile in memory
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if intervals==[]: return(0)
        
        starts = map(lambda x: x.start, intervals)
        ends = map(lambda x: x.end, intervals)
        
        starts.sort()
        ends.sort()
        
        res = 0
        index = 0
        for i in range(len(intervals)):
            if starts[i] < ends[index]:
                res += 1
            else:
                index += 1
        return(res)




# Another possibility...iterate through a sorted list of starts. Put the ends in a priority queue as you go
# This lets you compare the starts to the nearest end. Given this logic you can solve the problem similar to the above logic.
# I think it's easier to just think about extracting the ends and sorting them though. 