"""
Given a non negative integer number num. For every numbers i in the range 0 <= i <= num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""


"""
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
0 1 1 2 1 2 2 3 1 2  2  3  2  3  3  4  1


00000       0
10000       1

01000       2
11000       3

00100       4
10100       5
01100       6
11100       7

00010       8
10010       9
01010       10
11010       11
00110       12
10110       13
01110       14
11110       15


00001       16

"""
# Attempt 1: 51st percentile in speed. Implement log base 2 function
# Intuition: binary repeats in chunks with an extra 1...so #s 4 to 7 are the same
# as 0 to 3 with an extra 1 added...8 to 15 are the same as 0 to 7 with an extra 1 added
# and so on
class Solution:
    def countBits(self, num: int) -> List[int]:
        def lg(x):
            res = 0
            while x>1:
                x = x >> 1
                res +=1
            return(res)
        
        res = [0, 1]
        for _ in range( lg(num) ):
            res += [ x+1 for x in res ]
        return res[0:num+1]



# 2nd attempt: 81st percentile in speed. Extra speed with built ins. 
from math import log, floor
class Solution:
    def countBits(self, num: int) -> List[int]:
        if num==0: return[0]
        res = [0, 1]
        for _ in range( int(floor(log(num, 2))) ):
            res += [ x+1 for x in res ]
        return res[0:num+1]


# 3rd attempt: 99th percentile in speed. Simplify the loop
class Solution:
    def countBits(self, num: int) -> List[int]:
        # if num==0: return[0]
        res = [0, 1]
        while len(res) < num+2:
            res += [ x+1 for x in res ]
        return res[0:num+1]


# 4th attempt: 76th percentile in speed
# Different tact. Two facts. 1) Every binary value has the same number of 1's as the result of
# multiplying it by 2. 2) Every odd number has a binary representation with 1 more 1 than the
# even number that is one less.
class Solution:    
    def countBits(self, num: 'int') -> List[int]:
        res = [0]*(num+2)
        res[1] = 1
        for i in range(1,num//2+1):
            res[i*2] = res[i]
            res[i*2+1] = res[i]+1
        return res[:num+1]
