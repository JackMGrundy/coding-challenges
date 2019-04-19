"""
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""
# 1st attempt: dumb, quick and simple. 11th percentile in speed.
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        res = 1
        incr = A
        check = False
        while B not in A:
            if check and len(A) >= 2* len(B): return -1
            check = True
            res += 1
            A += incr
        
        return res

# 2nd attempt: 84th percentile in speed
# If A is shorter than B, the only two possible minimum repeat values 
# Are x = min # repeats required for A to be longer than B
# and x+1. 
# To see this just note that just draw a picture of repeating A until it's 
# as long as B. 
import math
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        x = math.ceil( len(B) / len(A) )
        if B in A*x: return x
        if B in A*(x+1): return x+1
        return -1
    