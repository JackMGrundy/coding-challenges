"""
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
"""
# 57th percentile. 1076 ms.
# N^2 solution. Try expanding a palindrome outwards from each possble start point in the string.
# Constant space. 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s
        if len(s) == 2: return s if s[0]==s[1] else s[1]
        
        def expandPalindrome(s, l, r):
            res = (0, 0)
            
            while (l >= 0 and r < len(s) and s[l]==s[r]):
                res = (l, r)
                l -= 1
                r += 1
            
            return res
        
        res = (0, 0)
        maxPalindromeSize = 1
        
        for i in range(1, len(s)):
            evenPalindrome = expandPalindrome(s, l=i-1, r=i)
            oddPalindrome = expandPalindrome(s, l=i-1, r=i+1)
            
            for palindrome in [evenPalindrome, oddPalindrome]:
                l, r = palindrome
                if r-l+1 > maxPalindromeSize:
                    maxPalindromeSize = r-l+1
                    res = palindrome
        
        resL, resR = res
        return s[resL:resR+1]


# 99th percentile. 60ms
# Better implementation of above. We still iterate through the string and try expanding out from each starting
# point. However, instead of comparing character by character, check entire substrings at once. 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        maxPalindromeLength = 1
        start = 0
        
        for i in range(len(s)):
            
            if i-maxPalindromeLength >= 1 and s[i-maxPalindromeLength-1:i+1] == s[i-maxPalindromeLength-1:i+1][::-1]:
                start = i - maxPalindromeLength - 1
                maxPalindromeLength += 2
            
            elif i-maxPalindromeLength >= 0 and s[i-maxPalindromeLength:i+1] == s[i-maxPalindromeLength:i+1][::-1]:
                start = i - maxPalindromeLength
                maxPalindromeLength += 1
        
        return s[start: start+maxPalindromeLength]

"""
Notes:
Core idea, when we increase a string by 1 in length, you could at most create a new paldinrome that is 1 or 2 characters longer. 

We don't care about finding new palindromes that are the same length as one we've already found. 
We steadily increase the length of string we are considering.
Each time we look back as far as the longest palindrome we've seen so far.
Note, each time we need to back for two distances...one that considers a string that reaches back 1 greater than we've found so
far, and one that considers 2 greater than we've found so far. We increase the max string matched so far by those amounts
respectively if there is a match in either case. 

Good intuition exercise, think about:

abcdefghgfedcba

you have no palindrome until you get to the second g. You look back two and how you have max length 3. You go to f and look back 3 + 1, and use the 
current char...so effectively trying to make it 2 longer. Once again, new longest plaindrome. This repeats. 
"""