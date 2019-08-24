"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
# 36ms. 91st percentile.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        longestCommon = 0
        minLength = min([ len(x) for x in strs] )
        
        for charIndex in range(minLength):
            curChar = strs[0][charIndex]
            if not all([ x[charIndex]==curChar for x in strs]):
                return strs[0][0:longestCommon]
            else:
                longestCommon += 1
        
        return strs[0][0:longestCommon]