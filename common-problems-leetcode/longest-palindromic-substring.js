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

// 45th percentile. 212 ms.
// Note, the use of substring instead of slice doesn't speed up the result.
/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    if (s.length==0) return "";
    let maxPalindromeLength = 1,
        start = 0;
    
    for (let i = 0; i < s.length; i++) {
        if ( i-maxPalindromeLength >= 1 && s.slice(i-maxPalindromeLength-1, i+1) === s.slice(i-maxPalindromeLength-1, i+1).split("").reverse().join('') ) {
            start = i-maxPalindromeLength-1;
            maxPalindromeLength += 2;
            continue;
        }
        
        if ( i-maxPalindromeLength >= 0 && s.slice(i-maxPalindromeLength, i+1) === s.slice(i-maxPalindromeLength, i+1).split("").reverse().join('') ) {
            start = i-maxPalindromeLength;
            maxPalindromeLength += 1;
            }
    }
    
    return s.slice(start, start+maxPalindromeLength);
    
};

// 99th percentile. 68 ms. 
/*
Interesting to note that in Python, it's much faster to compare substrings as in the above answer. In
Javascript, it's much faster to compare character by character rather than using the slice methods. 
*/

/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    if (s.length==0) return "";
    let maxPalindromeLen = 1,
        start = 0;
    
    for (let i = 0; i < s.length; i++) {
        // even palindrome
        if (s[i]===s[i+1]) {
            let candidatePalindromeLen = 2;
            let candidateStart = i;
            let j = 1;
            while (i-j >= 0 && i+j+1 < s.length && s[i-j]===s[i+j+1]) {
                candidatePalindromeLen += 2;
                candidateStart--;
                j++;
            }
            
            if (candidatePalindromeLen > maxPalindromeLen) {
                start = candidateStart;
                maxPalindromeLen = candidatePalindromeLen;
            }
        }
        
        // odd palindrome
        if (i > 0 && s[i-1]==s[i+1]) {
            let candidatePalindromeLen = 3;
            let candidateStart = i-1;
            let j = 1;
            while (i-j-1 >= 0 && i+j+1 < s.length && s[i-j-1]===s[i+j+1]) {
                candidatePalindromeLen += 2;
                candidateStart--;
                j++;
            }
            
            if (candidatePalindromeLen > maxPalindromeLen) {
                start = candidateStart;
                maxPalindromeLen = candidatePalindromeLen;
            }
        }   
    }
    return s.slice(start, start+maxPalindromeLen);
};