"""
Given  an  array  of  meeting  time  intervals consisting of start and end times
[[s1,e1],[s2,e2],...]  (si  <  ei),  determine  if  a  person  could  attend all
meetings.                                                                       

Example 1:                                                                      

Input: [[0,30],[5,10],[15,20]]                                                  

Output: false                                                                   

Example 2:                                                                      

Input: [[7,10],[2,4]]                                                           

Output: true                                                                    

NOTE:  input  types have been changed on April 15, 2019. Please reset to default
code definition to get new method signature.                                    

"""

# 84ms. 93 percentile.
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        
        intervals.sort(key = lambda x: x[0])
        for i, [start, end] in enumerate(intervals[1:], 1):
            if start < intervals[i-1][1]:
                return False
            
        return True


"""
Notes:


"""