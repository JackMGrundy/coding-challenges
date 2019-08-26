/*
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
*/

// 2ms. 95th percentile.
import java.util.*;
class Solution {
    public String addStrings(String num1, String num2) {
        StringBuilder s = new StringBuilder();
        
        int ni1 = num1.length()-1;
        int ni2 = num2.length()-1;
        int carry = 0;
        while (ni1 >= 0 || ni2 >= 0) {
            int d1 = 0;
            int d2 = 0;
            if (ni1 >= 0) {
                d1 = num1.charAt(ni1--) - '0';
            }
            if (ni2 >= 0) {
                d2 = num2.charAt(ni2--) - '0';
            }
            
            int temp = d1 + d2 + carry;
            carry = temp / 10;
            s.append( temp%10 );    
        }
        if (carry == 1) {
            s.append("1");
        }
        
        return s.reverse().toString();
    }
}