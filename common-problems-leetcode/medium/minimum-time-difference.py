"""
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
"""

# 72ms. 95th percentile.
# 1440 operations...
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        memo = [ 0 for _ in range(24*60) ]
        
        for timePoint in timePoints:
            hours = int(''.join(timePoint[0:2]))
            minutes = int(''.join(timePoint[3:5]))
            totalMinutes = 60*hours + minutes
            memo[totalMinutes] += 1
            if memo[totalMinutes] > 1:
                return 0
        
        first = 24*60+1
        last = -24*60-1
        best = float("inf")
        for i in range(24*60):
            if memo[i]==1:
                best = min(best, i-last)
                first = min(first, i)
                last = max(last, i)
        
        best = min(best, 24*60+first-last)
        return best


# 80ms. 88 percentile.
# O(Nlog(N))
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = [ 60*int(x[0:2]) + int(x[3:]) for x in timePoints ]
        timePoints.sort()
        
        timePoints.append(1440 + timePoints[0])
        minDiff = float("inf")
        for i in range(1, len(timePoints)):
            minDiff = min(minDiff, timePoints[i] - timePoints[i - 1])
        
        return minDiff