"""
Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

 

Example 1:

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:

Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
 

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
"""


# First attempt
# 23rd percentile
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        
        sectionCounts = []
        sectionCount = 0
        curChar = s[0]
        index = 0
        while index < len(s):
            c = s[index]
            if c != curChar:
                sectionCounts.append(sectionCount)
                curChar = c
                sectionCount = 1
            else:
                sectionCount += 1
            index += 1
        
        sectionCounts.append(sectionCount)
        numberOfMatches = 0
        index = 0
        
        while index < len(sectionCounts) - 1:
            numberOfMatches += min(sectionCounts[index], sectionCounts[index + 1])
            index += 1
        
        return numberOfMatches

# Second attempt
# 32 percentile
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groupBoundaries = [0] + [ i for i,c in enumerate(s) if 0 < i and c != s[i - 1] ] + [len(s)]
        groupSizes = [ groups[i] - groups[i - 1] for i in range(len(groupBoundaries)) if 0 < i ]
        numberOfMatches = sum( [ min(groupSizes[i], groupSizes[i - 1]) for i in range(len(groupSizes)) if 0 < i] )
        return numberOfMatches
        


# Third attempt:
# 46th percentile
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                groups.append(1)
            else:
                groups[-1] += 1
        
        return sum( [ min(groups[i], groups[i-1]) for i in range(1, len(groups)) ] )


# Fourth attempt
# 92nd percentile
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        matches, prevGroupSize, curGroupSize = 0, 0, 1
        
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                matches += min(prevGroupSize, curGroupSize)
                prevGroupSize, curGroupSize = curGroupSize, 1
            else:
                curGroupSize += 1
        
        return matches + min(prevGroupSize, curGroupSize)