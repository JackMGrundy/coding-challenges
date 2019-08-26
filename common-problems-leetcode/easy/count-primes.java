/*
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
*/

// 11ms. 72nd percentile.
import java.util.*;
class Solution {
    public int countPrimes(int n) {
        if (n < 3) {
            return 0;
        }
        
        boolean[] primes = new boolean[n+1];
        Arrays.fill(primes, true);
        primes[0] = false;
        primes[1] = false;
        
        for (int i = 2; i < (int) Math.floor(Math.sqrt(n))+1; i++) {
            if (primes[i]) {
                for (int j = i*i; j < n; j+=i) {
                    primes[j] = false;
                }
            }
        }
        
        int res = 0;
        for (int i = 0; i < n; i++) {
            if (primes[i]) {
                res++;
            }
        }
        
        return res;
    }
}