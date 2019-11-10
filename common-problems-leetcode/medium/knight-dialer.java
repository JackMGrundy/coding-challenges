/* 

A chess knight can move as indicated in the chess diagram below:                

 .                                                                              

                                                                                

This  time,  we  place  our  chess  knight  on  any  numbered key of a phone pad
(indicated above), and the knight makes N-1 hops.  Each hop must be from one key
to another numbered key.                                                        

Each  time it lands on a key (including the initial placement of the knight), it
presses the number of that key, pressing N digits total.                        

How many distinct numbers can you dial in this manner?                          

Since the answer may be large, output the answer modulo 10^9 + 7.               

                                                                                

Example 1:                                                                      

Input: 1                                                                        

Output: 10                                                                      

Example 2:                                                                      

Input: 2                                                                        

Output: 20                                                                      

Example 3:                                                                      

Input: 3                                                                        

Output: 46                                                                      

                                                                                

Note:                                                                           

1 <= N <= 5000                                                                  


*/


// 9ms. 95 percentile.
class Solution {
    public int knightDialer(int N) {
        if (N == 1) {
            return 10;
        }
        
        int[] a = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
        int[] b = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
        int mod = (int) Math.pow(10, 9) + 7;
        
        for (int i = 0; i < N - 1; i++) {
            b[0] = (a[4]%mod + a[6])%mod;
            b[1] = (a[6]%mod + a[8])%mod;
            b[2] = (a[7]%mod + a[9])%mod;
            b[3] = (a[4]%mod + a[8])%mod;
            b[4] = ((a[0]%mod + a[3])%mod + a[9])%mod;
            b[5] = 0;
            b[6] = ((a[0]%mod + a[1])%mod + a[7])%mod;
            b[7] = (a[2]%mod + a[6])%mod;
            b[8] = (a[1]%mod + a[3])%mod;
            b[9] = (a[2]%mod + a[4])%mod;
            
            for (int j = 0; j < 10; j++) {
                a[j] = b[j];
            }
        }
        
        int result = 0;
        for (int j = 0; j < 10; j++) {
         result = (result + a[j])%mod;   
        }
        
        return result;
    }
}


/*

Notes:

Love this problem. It's simple, but layered and there's an insight
that's a real gem...a useful application of random walk

First key insight that came to mind -> the subproblems are connected...
i.e. a knight with n hops from starting position can generate numbers
equal to the number of results you could generate with 1 less hop 
from all of its neighbors...

This immediately implies that you can do a DP-memoization approach...multiple
problems are going to rely on the same subproblems...and a bottom up approach
seems better as no matter what we are going to get to a point where we're asking
questions like "how many numbers can you generate with a knight starting at position
x with 1 hop". 

Without the memoization, this is an exponential runtime complexity, which is bad.
To see this just note that at every turn, we have at least two additional spots to jump
to. This means we're going to end up with something like 2^n. 

The memoization cuts this to linear time. To see this, note that at each step
we're just doing the constant work of adding up how many ways there are to finish 
from each neighbors. So this will always be a process of just summing 1 or 2 numbers.
We have to do this for every number, but still, we're just doing ~10 sets of addition
for each step -> linear time. 

Now the gem:
We can implement the above with a series of simple equations...doing additions at
each step. However, we can do better. This is a straight up transition matrix
problem. So we can frame those equations in terms of a matrix. Then we can use
some ideas from probability theory to get the solution down to log time. 

Basically, instead of doing N processing steps, we can just square the matrix
log(N) times...this is basically like the "implement pow" problem.


Last Note:
Modular arithmetic reminder...
(A + B) mod C = (A mod C + B mod C) mod C




Boom. Terminado. 

*/