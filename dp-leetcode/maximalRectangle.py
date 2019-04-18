"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""

# Attempt 1: 57th percentile in speed
"""
# Intuition:
The confusing part is picking "which rectangle" to examine when you get to a given index.
you could examine the rectange tacken by stretching as far back to the left (assuming you're going left
to right) as you can or stretching up as far as you can (assuming your going from top to bottom)
The key intuition is that at each index, you want to know maximum left endpoint for the maximum
height rectangle obtainable, and you want to know the minimum right endpoint for the maximum height
rectangle obtainable. Given these, you can get the max height rectangle at that point. 

Now this can still be confusing as shown in this example:

When you're processing matrix[2][3], the best you could do would the 2x2 but the process described in the last
paragraph instead examines the 3x1. 

0 0 0 1 0 0 0 
0 0 1 1 0 0 0 
0 1 1 1 0 0 0

The key thing to note is that we are going to account for the 2x2 at matrix[2][2]. 

Don't feel like trying to elaborate on this...future self...here's an example that is helpful in lieu of a better explanation

0 0 0 1 0 0 0 
0 0 1 1 1 0 0 
0 1 1 1 1 1 0
The vector "left" and "right" from row 0 to row 2 are as follows

row 0:

l: 0 0 0 3 0 0 0
r: 7 7 7 4 7 7 7
row 1:

l: 0 0 2 3 2 0 0
r: 7 7 5 4 5 7 7 
row 2:

l: 0 1 2 3 2 1 0
r: 7 6 5 4 5 6 7
"""
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        numCols = len(matrix[0])
        numRows = len(matrix)
        dpLeft = [ 0 for _ in range(numCols) ]
        dpRight = [ numCols for _ in range(numCols) ]
        dpHeight = [ 0 for _ in range(numCols) ]
        res = 0
        # Loop through rows
        for i in range(numRows):
            # Loop through columns
            curLeft = 0
            curRight = numCols
            
            # Height
            for j in range(numCols):
                dpHeight[j] = dpHeight[j]+1 if matrix[i][j]=="1" else 0 
            # Left to right
            for j in range(numCols):
                if matrix[i][j]=="1": 
                    dpLeft[j] = max(curLeft, dpLeft[j])
                else: 
                    dpLeft[j] = 0
                    curLeft = j+1
            # Right to left
            for j in range(numCols-1, -1, -1):
                if matrix[i][j]=="1": 
                    dpRight[j] = min(curRight, dpRight[j])
                else:
                    dpRight[j] = numCols
                    curRight = j
            # Check for new best max
            for j in range(numCols):
                res = max(res, ( dpRight[j]-dpLeft[j] )*dpHeight[j] )

        return res
        
        

# Attempt 2: 90th percentile in speed.
# The best answers to this problem almost all take a stack based approach
# This is a fast/cool answer that adapts the solution for "largest rectangular area
# in a histrogram" to this problem (see https://www.geeksforgeeks.org/largest-rectangle-under-histogram/)

"""
Notes for later intuition:
The first two for loops just construct a "histogram" with "row" as the base. You can easily 
construct this given just info from the previous row and so on.

The innermost loop is the key. Its key info is maintained in a stack. The stack holds column indexes.
The while loop maintains the invariant that the heights of the indices on the stack are monotonically
increasing. I.e, the top index on the stack must have a height that is equal to or greater than all
before it. 

Say the next index would break the invariant, then the while loop kicks in. It will pop off the previous
index (which corresponds with the highest bar seen so far), and get the height of that index. Then, it will
get the distance to the next topmost index on the stack. This gives the width of a valid rectangle.
Take the product of these and ojala there is a possible answer. We may repeat this a few times. For example, 
in the example to ponder, when we are processing the third row and hit the 5th column, we'll pop twice, once for 
each of the h=3 columns preceding. The second pop is what will capture the 3x2 rectangle that is a possible answer.


Example to ponder:
0 0 1 1 0 0 0 
0 0 1 1 1 0 0 
0 1 1 1 1 1 0
"""
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        res = 0
        numCols = len(matrix[0])
        heights = [0]*(numCols+1)
        # Loop through rows
        for row in matrix:
            # Create height histogram
            for j in range(numCols):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0
            stack = [-1]
            for j in range(numCols + 1):
                while heights[j] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = j - 1 - stack[-1]
                    res = max(res, h * w)
                stack.append(j)
        
        return(res)
