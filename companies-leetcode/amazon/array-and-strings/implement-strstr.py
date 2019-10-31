"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""
# 36ms. 81st percentile.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


# 36ms. 81st percentile
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        for hIndex in range(len(haystack)):
            nIndex = 0
            
            if len(haystack) - hIndex < len(needle):
                return -1
            
            while nIndex == len(needle) or needle[nIndex] == haystack[hIndex + nIndex]:
                nIndex += 1
                
                if nIndex >= len(needle):
                    return hIndex
        
        return -1