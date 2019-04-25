/*
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Accepted
664,472
Submissions
2,631,788
*/

// 100th percentile. 1ms. 
class Solution {
    public int reverse(int x) {
        int res = 0;
        
        while (x != 0) {
            
            int tail = x % 10;
            int newResult = res * 10 + tail;
            if ( (newResult-tail) / 10 != res) {
                return 0;
            }
            res = newResult;
            x = x / 10;
        }
        
        return res;
 }
}


// 100th percentile.
// kind of cheap...using long
class Solution {
    public int reverse(int x) {
        long res = 0;
        boolean positive = x >= 0;
        if (!positive) x = x*-1;
        
        while (x > 0) {
            res = res*10 + x%10;
            x = x / 10;
        }
        
        if (positive && res < Integer.MAX_VALUE) {
            return (int) res;
        } else if (!positive && res < Integer.MAX_VALUE) {
            return (int) res*-1;
        } else {
            return 0;
        }
    }
}