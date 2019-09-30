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
        if not s or not k: 
            return 0
        
        res = start = end = 0        
        # seen = defaultdict(lambda:0)
        seen = defaultdict(int)
        for i, c in enumerate(s):
            seen[c] += 1
            if len(seen) <= k:
                res = max(res, end-start+1)
            else:
                while len(seen) > k:
                    seen[s[start]] -= 1
                    if seen[s[start]]==0: 
                        del seen[s[start]]
                    start += 1
            end += 1
        return res

# 94th percentile
# We don't need the full counts. Just the rightmost values. 
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or not k: 
            return 0
        
        res = start = end = 0        
        seen = {}
        for i, c in enumerate(s):
            seen[c] = i
            if k < len(seen):
                start = min(seen.values())
                del seen[s[start]]
                start += 1
            res = max(res, i - start + 1)
        return res
                 
"""
Notes:

1)
The straightforward answer is to a leader/lagger approach. We advanced the leader
until we have seen too many unique characters. Then we advance the lagger until
we don't have too many characters. 

2)
We can do better. No matter what, we are going to advance the leader through every single
character in the line. The goal is to decrease the time it takes to update the lagger. 

consider a case where we have

cb...c..c..a
Assume that is the only b in the string.
where the periods could be anything. Assume we hit too many unique chars when we hit a.
At that point we want to advance the lagger. We can't just increase it to get rid of c, because
we actually want to increase it to just past b, the first char we can eliminate by advancing.
To do this, we keep a dictionary mapping chars to the last time they were seen. Then, we
advance the lagger (start in the code above) to be just past that element. 

"""