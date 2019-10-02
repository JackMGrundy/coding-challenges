"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""

# Built in...not point of question but good benchmark.
# 32ms. 92nd percentile.
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n


# 28ms. 99th percentile.
# Iterative
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        total = 1
        while n:
            # if n & 1:
            if n % 2 == 1:
                total *= x
            x *= x
            # n >>= 1
            n //= 2
        return total


# Recursive
# 32ms. 92nd percentile.
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return self.myPow(1/x, -n)
        if n & 1:
            return x*self.myPow(x, n-1)
        return self.myPow(x*x, n >> 1)


"""
Notes:
For the most part Fast Power is obvious. One thing to note though...the logic in the iteative version for multiplying
total by x...note that this isn't the original value of x...its x after we've liked already doubled it one or more times.
This might seem strange because "shouldn't we only increase total by a factor of the original x when we encounter an
odd power?". The answer is due to the halving process. Say you start with n = 19. Yes, in the first iteration because 19
is odd, you just multiply total by the original x. However, then you divide 19 down to 9 with integer division. On this next
iteration, you actually need to multiply total by the original x twice. The reason? You halved 18 down to 9. Meaning
that when you halve 9 down to 4, you're losing 2 not 1 factors of x. This compounds as we keep halving. Thankfully, x is
compounding in perfect lockstep with the halving, so multiplying by x makes it all work out. 

Also note that the "odd if" in the iterative method is always going to be triggered at the end of the process. Any
natural number is going to boil down to 1 after the repeated halving.
"""