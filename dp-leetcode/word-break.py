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
# 36ms. 98th percentile.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True
        
        for i in range(len(s)):
            for word in wordDict:
                if dp[i] and (s[i:i+len(word)] == word):
                    if i + len(word) == len(s):
                        return True
                    dp[i + len(word)] = True
        
        return False

"""
Notes:
Starting at the beginning of the string, check every word that can match some starting portion of the string
and mark the point "matched to" in the dp array.

Iterate through the cars of the string. At each char, if we have matched this far, try to match farther into the string.
If we match to the last character, retun true. 
"""