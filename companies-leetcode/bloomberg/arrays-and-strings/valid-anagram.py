"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
# 71st percentile. 56ms.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letterCounts = {}
        
        for c in list(s):
            letterCounts[c] = 1 if c not in letterCounts else letterCounts[c]+1
        
        for c in list(t):
            if c not in letterCounts:
                return False
            letterCounts[c] -= 1
            if letterCounts[c] < 0:
                return False
        
        return True


# 40ms. 97th percentile.
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)