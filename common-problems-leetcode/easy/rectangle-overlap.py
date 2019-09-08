"""
A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.

Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two (axis-aligned) rectangles, return whether they overlap.

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
Notes:

Both rectangles rec1 and rec2 are lists of 4 integers.
All coordinates in rectangles will be between -10^9 and 10^9.
"""

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        aTopCornerX, aTopCornerY, aBottomCornerX, aBottomCornerY = rec1
        bTopCornerX, bTopCornerY, bBottomCornerX, bBottomCornerY = rec2
        
        aLeftOfB  = (aBottomCornerX <= bTopCornerX)
        aBelowB   = (aTopCornerY >= bBottomCornerY)
        aRightOfB = (aTopCornerX >= bBottomCornerX)
        aAboveB   = (aBottomCornerY <= bTopCornerY)
        
        return not (aAboveB or aBelowB or aLeftOfB or aRightOfB)


"""
Notes:
Instead of thinking through all the ways there could be overlap, think of just the four ways they
could fail to overlap. Rec1 could be above, below, left, or right of Rec2. Checking left and
right is 100% straightforward. For above and below, just remember that it's computer indexing...
so being below actually means having a greater y and vice versa. 

"""