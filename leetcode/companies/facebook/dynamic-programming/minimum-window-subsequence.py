"""
Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:

Input: 
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation: 
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.
 

Note:

All the strings in the input will only contain lowercase letters.
The length of S will be in the range [1, 20000].
The length of T will be in the range [1, 100].

"""

# 1st attempt: 90th percentile in speed. Found this challenging...need to work on dp. 
from collections import defaultdict
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        m = len(T)
        
        # Reference dictionary of locations of chars in target subsequence S
        d = defaultdict(list)
        for i, c in enumerate(T):
            d[c].append(i)
        
        # DP array for keeping track of possible windows
        dp = [ -1 for x in range(len(T)) ]
        windowLen = float("inf")
        windowStart = 0
        
        for index, c in enumerate(S):
            # If char is in target subsequence
            if c in d:
                # For each of c's locations in the subsequence
                for i in d[c][::-1]:
                    # The character is the start of the subsequence
                    if i==0:
                        dp[0] = index
                    # The character is in the subsequence, but not the start
                    else:
                        dp[i] = dp[i-1]
                    # If the char is the last in the subsequence, we have matched all preceding chars
                    # and the resulting window is smaller than the best one found so far
                    if i == m-1 and dp[i] != -1 and (index - dp[i] + 1) < windowLen:
                        windowStart = dp[i]
                        windowLen = index - dp[i] + 1
        
        if windowLen < float("inf"):
            return S[windowStart:(windowStart+windowLen)]
        else:
            return ""
            