"""
A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if: 

For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;  

OR,  for  i  <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is
odd.                                                                            

That  is,  the  subarray  is turbulent if the comparison sign flips between each
adjacent pair of elements in the subarray.                                      

Return the length of a maximum size turbulent subarray of A.                    

                                                                                

Example 1:                                                                      

Input: [9,4,2,10,7,8,8,1,9]                                                     

Output: 5                                                                       

Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])                                 

Example 2:                                                                      

Input: [4,8,12,16]                                                              

Output: 2                                                                       

Example 3:                                                                      

Input: [100]                                                                    

Output: 1                                                                       

                                                                                

Note:                                                                           

1 <= A.length <= 40000                                                          

0 <= A[i] <= 10^9                                                               

"""
# 520ms. 97 percentile.
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        up, down = [1]*len(A), [1]*len(A)
        
        for i in range(1, len(A)):
            if A[i-1] < A[i]:
                up[i] = down[i-1] + 1
            elif A[i-1] > A[i]:
                down[i] = up[i-1] + 1
        
        return max(max(up), max(down))


# 620ms. 
# 20 percentile.
# cmp
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        ans, anchor = 1, 0
        
        for i in range(1, len(A)):
            leftVsMid = (A[i-1] > A[i])-( A[i-1] < A[i])
            midVsRight = 0 if i == len(A)-1 else (A[i] > A[i+1])-( A[i] < A[i+1])
            if leftVsMid == 0:
                anchor = i
            elif leftVsMid*midVsRight != -1:
                ans = max(ans, i - anchor + 1)
                anchor = i
        
        return ans

"""
Notes:

We can think of convertin A to a series of cmp operations comparing i and i-1
so that:
[9,4,2,10,7,8,8,1,9]

looks like:
[-1, -1, 1, -1, 1, 0, -1, 1]

Then our goal is to find the longest sequence of alternating +1 -1.

The cmp approach does this explicitly. Python3 got rid of the cmp operation so instead we can
use (a > b)-(a < b).

A more efficient approach is to maintain two arrays "up" and "down that records the 
longest streaks such that the last comparison was an increase or decrease respectively.

We can note that for an "up" streak to be valid, there must have been a down on the previous
comparison. As a result, at an index i, if there is an up, then up[i] will be equal to 
1 + down[i-1]
"""