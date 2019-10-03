"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
Accepted
887,886
Submissions
3,144,652
"""
# 93 percentile
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        longestLength = 1
        characterToIndex = {}
        left = 0
        
        for right, c in enumerate(s):
            if c in characterToIndex and left <= characterToIndex[c]:
                longestLength = max(longestLength, right - left)
                left = characterToIndex[c] + 1
            characterToIndex[c] = right
        
        return max(longestLength, len(s) - left)

"""
Notes:
You  could use a set to check for repeats and then advance the left marker until
you  don't have repeats. To speed things up, we can use a hash table instead and
instantly advance the left marker to the first valid point.                     

Important note one:                                                             

"and left <= characterToIndex[c]:"                                              

This says "the last occurence of this repeat character has to be before or equal
to left". This precludes cases like "tmmzuxt" where the repeat offender is t but
left  does not equal the last occurence of t because we already advanced to deal
with  the  repeat  m's.  In  this  case,  resetting  left  would reintroduce the
duplicate m's to the string, because it would set left to "the last occurrenc of
t+1".                                                                           

In  this  case  we want to leave left where it is, because it is already farther
than the last occurence.                                                        

Important note two:                                                             

"max(longestLength, len(s) - left)"                                             

It's  possible  the  last  char we see won't be a duplicate. The code as is only
triggers an update to longestLength when a repeat is seen.                      

"""