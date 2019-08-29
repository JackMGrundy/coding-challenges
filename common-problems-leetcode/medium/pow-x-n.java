/*
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
*/

// Iterative. 0ms. 100th percentile.
class Solution {
    public double myPow(double x, int n) {
        double total = 1.0;
        if (n < 0) {
            x = 1.0/x;
            if (n == Integer.MIN_VALUE) {
                total *= x;
                n += 1;
            }
            n = -n;
        }
        
        while (n > 0) {
            if (n%2 == 1) {
                total *= x;
            }
            x *= x;
            n /= 2;
        }
        return total;
    }
}


// Recursive
// 0ms. 100th percentile.
class Solution {
    public double myPow(double x, int n) {
        if (n==0) {
            return 1;
        }
        if (n == 1) {
            return x;
        }
        if (n < 0) {
            if (n == Integer.MIN_VALUE) {
                n += 1;
                return (1/x)*myPow(1/x, -n);
            } else {
                return myPow(1/x, -n);
            }
        }
        if (n%2 == 1) {
            return x*myPow(x, n-1);
        }
        return myPow(x*x, n/2);
    }
}
