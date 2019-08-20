"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
# 32ms. 94th percentile
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalsTriangle = [ [1], [1, 1] ]
        
        for _ in range(numRows-2):
            previousRow = pascalsTriangle[-1]
            nextRow = [1] + [ previousRow[i] + previousRow[i+1] for i in range(len(previousRow)-1) ] + [1]
            pascalsTriangle.append(nextRow[:])
        
        return pascalsTriangle[0:numRows]