"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
# 420ms. 69th percentile.
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [False, False] + [True]*(n-2)
        
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = False
        
        return sum(primes)
            