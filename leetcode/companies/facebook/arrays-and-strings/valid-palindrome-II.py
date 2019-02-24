"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""
# 1st attempt: 33rd percentile in speed. Slow...but short and understandable
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return(s==s[::-1])

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(s)
        
        l = 0; r = len(s)-1
        while l<r:
            if s[l] != s[r]:
                return( self.isPalindrome(s[(l+1):r+1]) or self.isPalindrome(s[l:r]) )
            l+=1; r-= 1
        return(True)


# 2nd attempt: 75th percentile...just a bit of optimization...no speedup from converting to list
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return(s==s[::-1])

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0; r = len(s)-1
        while l<r:
            if s[l] != s[r]:
                return( self.isPalindrome(s[(l+1):r+1]) or self.isPalindrome(s[l:r]) )
            l+=1; r-= 1
        return(True)



# 3rd attempt: 99th percentile. Optimize a bit by checking if the string is a palindrome at the outset
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return(s==s[::-1])

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if self.isPalindrome(s): return(True)
        l = 0; r = len(s)-1
        while l<r:
            if s[l] != s[r]:
                return( self.isPalindrome(s[(l+1):r+1]) or self.isPalindrome(s[l:r]) )
            l+=1; r-= 1
        return(True)