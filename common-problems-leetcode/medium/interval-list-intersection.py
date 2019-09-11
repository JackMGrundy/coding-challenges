"""
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

 

Example 1:



Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
 

Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""

# 168ms. 92nd percentile.
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []
        
        aI, bI = 0, 0
        aLow, aHigh = A[aI]
        bLow, bHigh = B[bI]
        res = []
        while aI < len(A) and bI < len(B):
            minMax = min(aHigh, bHigh)
            maxMin = max(aLow, bLow)
            
            # There is overlap
            if maxMin <= minMax:
                res.append([maxMin, minMax])
            
            if aHigh < bHigh:
                aI += 1
                if aI < len(A):
                    aLow, aHigh = A[aI]
            else:
                bI += 1
                if bI < len(B):
                    bLow, bHigh = B[bI]
        
        return res


"""
Notes:


        Cases
        ----------
          -----
          
        -------
           --------
        
        -----
              -----

  The only case where there is no overlap is where the minEnd < maxStart
  Otherise we append. 
  The overlap is going to be the range from maxStart to minEnd. 

  Note, because the question says that A and B are each pairwise disjont, we don't have to worry about the case of

    --~~~~
  ----------  

where there are two consecutive intervals in A or in B that could actually be combined into a single combined bit of intersection. 

"""