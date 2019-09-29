"""
Given  n non-negative integers representing the histogram's bar height where the
width of each bar is 1, find the area of largest rectangle in the histogram.    

                                                                                

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

                                                                                

The largest rectangle is shown in the shaded area, which has area = 10 unit.    

                                                                                

Example:                                                                        

Input: [2,1,5,6,2,3]                                                            

Output: 10                                                                      
"""
# 124ms. 69 percentile.
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largestRectangle = 0
        heights.append(0)
        stack = [-1]
        
        for i, height in enumerate(heights):
            while height < heights[stack[-1]]:
                candidateRectangeHeight = heights[stack.pop()]
                candidateRectangleWidth = i - 1 - stack[-1]
                largestRectangle = max(largestRectangle, candidateRectangeHeight*candidateRectangleWidth)
            stack.append(i)
                
        return largestRectangle
"""
Notes:
See notes on largest rectangle. These problems are equivalent.
"""