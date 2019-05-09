/*
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
Accepted
540,233
Submissions
1,989,622
*/
// 50th percentile. 31ms. 
class Solution {
    public String longestPalindrome(String s) {
        if (s.length()==0) return "";
        int maxPalindromeLen = 1;
        int start = 0;
        
        for (int i = 0; i < s.length(); i++) {
            
            // Even length palindrome
            if (i+1 < s.length() && s.charAt(i) == s.charAt(i+1)) {
                int candidateMaxLen = 2;
                int candidateStart = i;
                int j = 1;
                while (i-j >= 0 && i+j+1 < s.length() && s.charAt(i-j) == s.charAt(i+j+1)) {
                    candidateStart = i-j;
                    candidateMaxLen += 2;
                    j++;
                }
                
                if (candidateMaxLen > maxPalindromeLen) {
                    maxPalindromeLen = candidateMaxLen;
                    start = candidateStart;
                }
            }
            
            // Odd length palindrome
            if (i > 0 && i+1 < s.length() && s.charAt(i-1) == s.charAt(i+1)) {
                int candidateMaxLen = 3;
                int candidateStart = i-1;
                int j = 1;
                while (i-j-1 >= 0 && i+j+1 < s.length() && s.charAt(i-j-1) == s.charAt(i+j+1)) {
                    candidateStart = i-j-1;
                    candidateMaxLen += 2;
                    j++;
                }
                
                if (candidateMaxLen > maxPalindromeLen) {
                    maxPalindromeLen = candidateMaxLen;
                    start = candidateStart;
                }
            }
        
        }
        return s.substring(start, start+maxPalindromeLen);
    }
}