"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
"""

# 44ms. 59th percentile.
# A lot of the faster solutions just used built in sqrt method...
# binary search
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l, r = 0, 1 + x//2
        
        while l <= r:
            m = l + (r-l)//2
            if m*m <= x < (m+1)*(m+1):
                return m
            if m*m < x:
                l = m+1
            else:
                r = m-1

