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
                # for j in range(i*2, n, i): easier to read but slower
                for j in range(i*i, n, i):
                    primes[j] = False
        
        return sum(primes)


"""
Notes:

Seive of Eratosthenes (SOE)

Initialization is O(N) to make the primes array.

Logic for SOE:
Every number is composed of a product of prime terms. Given a prime
and a limit to check up until, we can identify that every number that 
contains the prime in its product is not prime.

Thinking through an example:
The sieve starts at 2 and eliminates all numbers that have 2 as a term. It
does the same with 3. Now when it hits 4, we can skip. The reason is that 4 is
really just 2*2 and we aleady took care of 2. We continue with 5. It is
prime, so we cross off its terms. We hit 6. Again, this is just a product
of smaller terms we have already seen, so we don't have to do any work.


The underlying logic:
Each number can eliminate greater numbers for which it is a term. To identify
which numbers to eliminate, we keep incrementing the number by itself.
There is no need to process numbers that are not prime, because they are comprised
of smaller pieces that we have already processed.

We actually only need to process sqrt(n) numbers...easy to see...(sqrt(n+1))*(sqrt(n+1))
will be greater than our limit n.

The only tricky part is understanding why we can actually start with i*i in the inner
loop. The intuition: say we are pricing the prime p. Now consider numbers between p
and p*p. Now zero in on the numbers between p and p*p that have p as a factor. p must
be the greatest prime factor for any of these numbers. It's obivous because if you
divide out p, you must get something smaller than p...therefore, if any of these
numbers are not prime, we already axed them when we processed primes smaller than p.

Run time:
The outer loop runs sqrt(n) times. The inner loop runs n/2 times for 2, n/3 for 3, n/5, for
5 and so on. So:
n/2 + n/3 + n/5 + n/7 + n/11 + ...
You can prove that this is log(log(n))...not diving into it here
So total time is O(n(log(log(n))))

Fin

"""