"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at
coordinate  (i,  ai).  n vertical lines are drawn such that the two endpoints of
line  i  is  at  (i,  ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.             

Note: You may not slant the container and n is at least 2.                      

                                                                                

The  above  vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this
case, the max area of water (blue section) the container can contain is 49.     

 

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
Accepted
353.5K
Submissions
805.1K
"""
# 140ms. 82 percentile. 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        leftEnd, rightEnd = 0, len(height)-1
        leftHeight, rightHeight = height[0], height[-1]
        mostWaterContained = 0
        
        while leftEnd < rightEnd:
            mostWaterContained = max(mostWaterContained, (rightEnd - leftEnd)*min(leftHeight, rightHeight))
            
            if leftHeight <= rightHeight:
                leftEnd += 1
                leftHeight = height[leftEnd]
            else:
                rightEnd -= 1
                rightHeight = height[rightEnd]
        
        return mostWaterContained        


"""
Intuition
Same intuition as trapping rain water...

                                -
                                -
-                               -
-                               -
------------------------------  -

^In the cell to the right of the left column, we know we'll get at least 2 units
of water. In fact, this is the best we can do. It doesn't matter if             
we  have a bigger/smaller column between these two. Therefore we can confidently
process that column to the right of the far left column. In this way,           
we can keep advancing the pincer...always moving the minimum height end column 1
ahead and then processing.                                                      

"""