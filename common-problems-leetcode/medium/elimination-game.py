"""
There  is  a  list  of sorted integers from 1 to n. Starting from left to right,
remove the first number and every other number afterward until you reach the end
of the list.                                                                    

Repeat  the  previous  step  again, but this time from right to left, remove the
right most number and every other number from the remaining numbers.            

We  keep repeating the steps again, alternating left to right and right to left,
until a single number remains.                                                  

Find the last number that remains starting with a list of length n.             

Example:                                                                        

Input:                                                                          

n = 9,                                                                          

1 2 3 4 5 6 7 8 9                                                               

2 4 6 8                                                                         

2 6                                                                             

6                                                                               

Output:                                                                         

6                                                                               
"""
# 48ms. 84 percentile.
class Solution:
    def lastRemaining(self, n: int) -> int:
        ans, step, isForward = 1, 1, True
        
        while 1 < n:
            if isForward or n%2 == 1:
                ans += step
            
            step *= 2
            n //= 2
            isForward = not isForward
        
        return ans

"""
Notes:

We don't have to actually make a list. We can just work with n.

Intuition:
Instead of thinking about finding the answer in the middle of the interval 1 to n,
think of it as starting with the answer 1, the smallest value in the interval
and then updating our answer as the halving's cull off values. 

We start with "1" as our value. 

A forward pass eliminates our value by design. 

If the list is odd length, a backwards
pass also eliminates it. 

A backwards pass with an even length is the only traversal that doesn't eliminate our number. 

In all three cases, n is halved. 

In the first two cases, we need a new number. We make a step variable. At first this step is
just 1, signifying that a step from 1 to 2 gets us to the next smallest available number.

Every time we travers the list, we eliminate half the values and need to double the step
size in order to reach a remaining, valid number. 

This gives us everything for an answer. While n is greater than 1, we check if we're doing 
a forward pass or a backwards pass at odd parity. If we are, we advance our number before
it gets clobbered.

We then "complete" the traversal symbolically by halving the value of n and doubling the 
step size.

Finally, we prep for the next traversal by reversing the boolean forward.

"""