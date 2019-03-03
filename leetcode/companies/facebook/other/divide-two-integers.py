"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
"""
# 1st attempt: brute force. Times out.
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        temp = abs(dividend)
        res = 0
        while temp >= abs(divisor):
            temp -= abs(divisor)
            res += 1
        if (dividend>=0 and divisor>=0) or (dividend<=0 and divisor<=0):
            return(res)
        else:
            return(-res)


# 2nd attempt: bit shifting. 60th percentile in speed.
# Key intuition -> when you bit shift in base n, you are multiplying / dividing (depending on the direction)
# the number by n. To see that, note that moving a value up a decimal place is equivalent to multiplying by n.
# Therefore, if you shift each bit that comprises a number up, you multiply the whole number by n.
# ...just like shifting 3, 1 spot to 30 is 3 * 10. 
# 
# Applying this idea to the problem: take the divisior, and shift it as much as you can (see the 32-bit signed part in the question).
# Then check if it is smaller than the dividend. Keep shifting it 1 space less until you get a value that is less than the dividend.
# For example, say dividend = 303, we're in base 10, and the divisor is 3. We check ...3 * 10^32, 3*1-^31...until we get to 300.
# This tells us that 100, "3's" fit in the dividend. Add 100 to res, subtract 300 from 303 to get 3. And continue the process.
# You'll end up finding that 1 "3" "fits" into the reminaing and 3, add that to res, and get a final answer of 101. 
# 
# Last tid bit, answer is in base 2, because that's what Python (being a programming language...) comes with. 
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend>=0 and divisor>=0) or (dividend<=0 and divisor<=0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        
        for i in range(31, -1, -1):
            if dividend < divisor: break
            if (divisor << i) <= dividend:
                res += (1 << i)
                dividend -= (divisor << i) 
                
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)



# 3rd attempt: Attempt to optimize submission 2 a bit. Instead of descending in orders of magnitude, ascend.
# Runtime unclear. Ossicaltes between top submission and ~20th percentile. 
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend>=0 and divisor>=0) or (dividend<=0 and divisor<=0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i = i << 1
                temp = temp << 1
                
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)