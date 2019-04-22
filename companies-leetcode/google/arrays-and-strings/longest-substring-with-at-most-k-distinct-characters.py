"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
"""
# 68th percentile
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or not k: return 0
        
        res = start = end = 0        
        seen = defaultdict(lambda:0)
        for i, c in enumerate(s):
            seen[c] += 1
            if len(seen) <= k:
                res = max(res, end-start+1)
            else:
                while len(seen) > k:
                    seen[s[start]] -= 1
                    if seen[s[start]]==0: del seen[s[start]]
                    start += 1
            end += 1
        return res

# 94th percentile
# We don't need the full counts. Just the rightmost values. 
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or not k: return 0
        
        res = start = end = 0        
        seen = {}
        for i, c in enumerate(s):
            seen[c] = i
            if len(seen) > k:
                start = min(seen.values())
                del seen[s[start]]
                start += 1
            res = max(res, i-start+1)
        return res
                 
