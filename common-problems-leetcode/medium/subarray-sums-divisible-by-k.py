"""
Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

 

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 

Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
"""

# 348ms. 70th percentile.
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        cumSum = [0]
        for num in A:
            cumSum.append( (cumSum[-1]+num)%K )
        
        remainderCounts = collections.Counter(cumSum).values()
        res = 0
        for count in remainderCounts:
            res += count*(count-1)//2
        
        return res




"""
Notes:
This question is basically a math problem imo...

Note:
Given an array and indices i and j
Given a target value of k, you can write the sum of any subarray as 

sum(i, j) = q*k + r

where q is the quotient and the remainder is r

Next up, we can write:
sum(i, j) = sum(0,j) - sum(0, i-1)

Combining these two ideas:
sum(i, j) = q1*k + r1 - q2*k - r2
=>
          = (q1 - q2)k + (r1-r2)

So to evaluate whether a subarray(i,j) is divisible by k, we care about the remainders of
dividing sum(subarray(0,j)) and sum(subarray(0, i-1)) by k. 

If you have those two sums, you can just add them and see if the result is divisible by k. 

Before diving into more intuition, here's the procedure:

Take a cumulative sum of nums
At each step, get the mod of the sum with k
At the end, count up how many different mod values you get
Then loop over those counts and add this to the total result:
    (count(count-1))/2

return 

Why does this work?
Intuitively, each of the counts represents the remainder of dividing some subarray from 0 to j by k
This means that we can combine any pair of them we want...If we take two counts, one will be for
0 to j and the other will be for 0 to i...so they will overlap...

So say k = 5 and we have two sub arrays 0 to i and 0 to j. They have remainder 4
with k. To make this really conrete, lets say their sums are 14 and 9. Take the difference 
and ojala, its divisible by 5...which means that subarray i to j is divisile by k! Very cool.

So in other words, for each remainder count...we can take any two distinct ones and get
a valid sub array. 

(n
 2)  =  n!
       -----  =      =  n(n-1) / 2
        2!(n-2)!


Boom
"""



