"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
Accepted
96,108
Submissions
480,736
"""
# 32ms. 93 percentile.
# Would build res as a list in production code...just want the cleanliness of strings rn
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0 or denominator == 0:
            return "0"
        quotient, remainder = divmod(abs(numerator), abs(denominator))
        negative = numerator*denominator < 0
        res = str(quotient)
        if negative:
            res = "-" + res
        
        if 0 < remainder:
            res += "."
        
        i = len(res)
        seen = { remainder: i }
        while 0 < remainder:
            quotient, remainder = divmod(remainder*10, abs(denominator) )
            res += str(quotient)
            
            if remainder in seen:
                res = res[0:seen[remainder]] + '(' + res[seen[remainder]:] + ')'
                return res
            
            i += 1
            seen[remainder] = i
            
        return res

"""
Notes:
divmod gives you back quotient, remainder

Explain with an example:
We want 500/70 = 7.1428571428...


500 / 70 
q = 7
remainder = 10
res = 7.

Next question, how many times does 70 go into 10? That gives
us the decimal part. Instead, we'll just get the next digit. If we
multiply 10 by 10, we can divide 70 into 100 and use divmod again. 
That gives us
100 / 70
q = 1
remainder = 30
res = 7.1

Next question, how many times does 70 go into 30? Again, multiply 30 by 10.
300 / 70
q = 4
remainder = 20
res = 7.14

How many times does 70 go into 20?
200 / 70
q = 2
remainder = 60
res = 7.142

...we repeat this until we get back to
How many times does 70 go into 100?
At this point we know we're in a cycle.

Intuitively, we're actually just reducing the remainder with every division...
So 70 into 10
Then 70 into 3
Then 70 into .2
...70 into .06

And we're hiding the annoying decimal stuff by multiplying by 10 at every level
so we can keep using divmod. 

Written another way

dividend / divisor = quotient and remainder

500 / 70 = 7 and 10
        =
        7  + 10 / 70

10 / 70 = .1 and 3
        =
        .1 + 3 / 70

        ...


"""