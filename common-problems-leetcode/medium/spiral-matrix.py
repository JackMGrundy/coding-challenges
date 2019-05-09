"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
# 1st attempt: 71st percentile in speed
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        rStop = len(matrix[0])
        bStop = len(matrix)
        lStop = 0
        tStop = 0
        res = []
        eles = len(matrix)*len(matrix[0])
        count = 0
        
        while lStop < rStop and bStop > tStop:
            for i in range(lStop, rStop):
                res.append(matrix[tStop][i])
                count += 1
                if count == eles: return res
            rStop -= 1
            
            for j in range(tStop+1, bStop):
                res.append(matrix[j][rStop])
                count += 1
                if count == eles: return res
            bStop -= 1
            
            for i in range(rStop-1, lStop-1, -1):
                res.append(matrix[bStop][i])
                count += 1
                if count == eles: return res
            lStop += 1
            
            for j in range(bStop-1, tStop, -1):
                res.append(matrix[j][lStop-1])
                count += 1
                if count == eles: return res
            tStop += 1
        
            
        