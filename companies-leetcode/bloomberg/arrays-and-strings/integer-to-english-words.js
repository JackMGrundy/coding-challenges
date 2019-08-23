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
// 60ms. 88th percentile.
/**
 * @param {number} num
 * @return {string}
 */
var numberToWords = function(num) {
    let suffixes = ["", "Thousand ", "Million ", "Billion "]
    let oneToNineteen = ["", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine ", "Ten ", "Eleven ", "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen "]
    let tens = ["", "Ten ", "Twenty ","Thirty ","Forty ","Fifty ","Sixty ","Seventy ","Eighty ","Ninety "]
    
    let helper = function(num) {
        
        if (num < 20) {
            return oneToNineteen[num];
        }
        if (20 <= num && num < 100) {
            return tens[Math.floor(num / 10)] + oneToNineteen[num % 10];
        }
        if (100 <= num && num < 1000) {
            return oneToNineteen[Math.floor(num / 100)] + "Hundred " + helper(num % 100);
        }
    }
    
    let res = "";
    while (num > 0) {
        let totalDigits = ("" + num).length;
        let currentDigits = (totalDigits%3 === 0) ? 3 : totalDigits % 3;
        let suffix = suffixes[Math.floor((totalDigits-1) / 3)];
        let currentNum = Math.floor(num / (10 ** (totalDigits-currentDigits)));
        res += helper(currentNum) + suffix;
        num = num % (10 ** (totalDigits-currentDigits));
    }

return res.trim() || "Zero";
};