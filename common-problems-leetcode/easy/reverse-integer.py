"""
Given a 32-bit signed integer, reverse digits of an integer.                    

Example 1:                                                                      

Input: 123                                                                      

Output: 321                                                                     

Example 2:                                                                      

Input: -123                                                                     

Output: -321                                                                    

Example 3:                                                                      

Input: 120                                                                      

Output: 21                                                                      

Note:                                                                           

Assume we are dealing with an environment which could only store integers within
the  32-bit  signed  integer  range:  [−231,   231 − 1]. For the purpose of this
problem,  assume  that  your  function  returns  0  when  the  reversed  integer
overflows.                                                                      

"""
# 40ms. 60 percentile.
class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -(2**31)
        isNegative = x < 0
        x = abs(x)
        total = 0
        
        while x:
            if not isNegative and MAX_INT/10.0 < total:
                return 0
            if isNegative and abs(MIN_INT)/10.0 < total:
                return 0
            
            total = total*10 + x%10
            x //= 10
        
        return total if not isNegative else -total

"""
Notes:

Simple intuition is to reduce the magnitude of the max and min values by 1
and then compare at that order of magnitude.

"""