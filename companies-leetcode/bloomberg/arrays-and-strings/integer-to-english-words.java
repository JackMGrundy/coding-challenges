/*
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
*/

// 78th percentile. 2ms. 
class Solution {
    public String numberToWords(int num) {
        String[] suffixes = {"", "Thousand ", "Million ", "Billion "};
        
        String res = "";
        while (num > 0) {
            int numDigits = ("" + num).length();
            int currentDigits = (numDigits % 3 == 0) ? 3 : numDigits % 3;
            String suffix = suffixes[(numDigits-1)/3];
            int currentNumber = num / (int) (Math.pow(10, numDigits-currentDigits));
            res += helper(currentNumber) + suffix;
            num = num % (int) (Math.pow(10, numDigits-currentDigits));
        }
        
        return res == "" ? "Zero" : res.trim();
    }
    
    public String helper(int num) {
        String[] oneToNineteen = {"", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine ", "Ten ", "Eleven ", "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen "};
        String[] tens = {"", "Ten ", "Twenty ","Thirty ","Forty ","Fifty ","Sixty ","Seventy ","Eighty ","Ninety "};
        
        if (num < 20) {
            return oneToNineteen[num];
        }
        if (20 <= num && num < 100) {
            return tens[num / 10] + oneToNineteen[num % 10];
        }
        if (100 <= num && num < 1000) {
            return oneToNineteen[num / 100] + "Hundred " + helper(num % 100);
        }
        return "";
    }
}