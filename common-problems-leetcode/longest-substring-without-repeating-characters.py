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
# 94th percentile
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        seen = set()
        curBest = tail = res = 0
        
        for head, c in enumerate(s):
            # Not repeating char
            if c not in seen:
                curBest += 1
            # Repeating char
            else:
                # Check if we found a new best answer
                res = max(res, curBest)
                while s[tail]!=c:
                    seen.remove(s[tail])
                    tail += 1
                tail += 1
                curBest = head-tail+1
            
            seen.add(c)
        
        return max(res, curBest)