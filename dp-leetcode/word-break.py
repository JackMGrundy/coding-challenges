"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
# 1st attempt: Brute force BFS. Time out. Passed ~70 percent of tests.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # s = list(s)
        wordDict = set(wordDict)
        
        stack = [s]
        while stack:
            cur = stack.pop()
            for i in range(len(cur)+1):
                curSub = cur[:i]
                # We have matched another part of the remaining string
                if curSub in wordDict:
                    # The match accounts for the rest of the string
                    if i==( len(cur) ): 
                        return(True)
                    else:
                        stack.append(cur[i:])
        
        return False


# 2nd attempt: 70th percentile in speed
# A problem with the 1st attempt: we repeat a lot of work. For example, if we have a dictionary with "a" and "aa"
# in it and a target string of "aaaa...", then we are going to confirm "aaaa" with 4 "a's" and 2 "aa's".
# 
# The intuition for this problem, is that no matter what, you have to match a word to the first part of the string
# Given that you find a match, you can reduce the problem to matching the remaining, smaller string. So
# whenever we match up to a certain point, we can mark that...it doesn't matter if there are different
# ways of getting there. 
# 
# This solution simply maintains a boolean set of markers indicating how far we have succesfully matched. 
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [ False ]*len(s)
        
        for i in range(len(s)):
            for word in wordDict:
                # The chars up to i match the current word...and we are either matching the first
                # word in the string or we succesfully matched everything before the start of the
                # current word
                if ( word == s[i-len(word)+1:i+1] ) and ( i-len(word)==-1 or dp[i-len(word)] ):
                    dp[i] = True
        
        return dp[-1]