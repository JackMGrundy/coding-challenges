"""
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.

Example:

Input: n = 3, k = 2
Output: 6
Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:

            post1  post2  post3      
 -----      -----  -----  -----       
   1         c1     c1     c2 
   2         c1     c2     c1 
   3         c1     c2     c2 
   4         c2     c1     c1  
   5         c2     c1     c2
   6         c2     c2     c1
Accepted
41,106
Submissions
113,416
"""
# 1st attempt: 64th percentile in speed
"""
Intuition:

Imagine n = 4, k = 4


1  -  4  -  15  -  57 
1  /  4  /  15  /  57
1  /  4  /  15  /  57
1  /  4  /  15  /  57

^this illustrates the number of different legal ways to get to each spot. The lines are focusing on "flow"
from the lower levels to the top row. 

They key example: focus on the first 15 in the third column. Each of the bottom 3, "4"'s in the previous column
contribute 4 ways to the 15 for 12 total. They are all valid, because if we pass through any of them before 
going to the top option, then we won't have more than 2 of the same color in a row. The
only catch is the top 4...one of the ways to get to that 4 involves going from the top 1 to the top 4...
if we then were to go to the top 15, that would be the same color 3 times in a row, which isn't legal,
So we have to subtract that, which ultimately yields 15. So you just need to make sure you can accurately count
how many of the routes to subtract from the spot in the previous column that corresponds with the same color.

You can work out that for the second column, the number of valid paths to a spot, arr, is k.
From there on out, its arr[i] = arr[i-1](k-1) + a 

where a = # of valid paths from same color in previous layer

We can keep a little recurrence going for a:
At column 2, a = 1
then a[i] = arr[i-1] - a[i-1]

Then there's just some pesky edge cases to deal with
"""
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if k==0 or n==0: return 0
        if n < 3: return k**n
        
        a = 1; arr = k
        for i in range(2, n):
            a = arr - a
            arr = arr*(k-1) + a
        
        return k*arr
