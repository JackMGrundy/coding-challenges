/*
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
*/
// 100th percentile
class Solution {
    public int[] plusOne(int[] digits) {
        int carry = 0;
        digits[digits.length-1]++;
        for (int i = digits.length-1; i >= 0; i--) {
            digits[i] += carry;
            if (digits[i] < 10) {
                return digits;
            }
            carry = digits[i] - 9;
            digits[i] = 0;
        }

        int[] res = new int[1+digits.length];
        System.arraycopy(digits, 0, res, 1, res.length-1);
        res[0] = 1;
        return res;
    }
}