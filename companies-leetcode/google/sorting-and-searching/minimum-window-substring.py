"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""
# 17th percentile
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""
        s = list(s)
        counts = Counter(t)
        chars = set(t)
        tail = 0
        res = ""
        minLength = float("inf")
        
        for head, c in enumerate(s):
            # Hit a char in t
            if c in chars:
                counts[c] -= 1
                # We've matched all the characters
                while max(counts.values()) <= 0:
                    # Check if we have a new best res
                    if head - tail < minLength:
                        minLength = head - tail + 1
                        res = s[tail:head+1]
                    # Advance tail
                    if s[tail] in chars:
                        counts[s[tail]] += 1
                    tail += 1
        
        return ''.join(res)


# 38th percentile
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""
        s = list(s)
        counts = Counter(t)
        chars = set(t)
        missing = len(t)
        tail = 0
        res = ""
        minLength = float("inf")
        
        for head, c in enumerate(s):

            # Hit a char in t
            if c in chars:
                if counts[c] > 0: missing -= 1
                counts[c] -= 1
                # We've matched all the characters
                while not missing:
                    # Check if we have a new best res
                    if head - tail < minLength:
                        minLength = head - tail + 1
                        res = s[tail:head+1]
                    # Advance tail
                    if s[tail] in chars:
                        if counts[s[tail]] == 0: missing += 1
                        counts[s[tail]] += 1
                        
                    tail += 1
        
        return ''.join(res)


# 68th percentile 
# Got rid of list conversion
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""
        counts = Counter(t)
        chars = set(t)
        missing = len(t)
        tail = 0
        res = ""
        minLength = float("inf")
        
        for head, c in enumerate(s):

            # Hit a char in t
            if c in chars:
                if counts[c] > 0: missing -= 1
                counts[c] -= 1
                # We've matched all the characters
                while not missing:
                    # Check if we have a new best res
                    if head - tail < minLength:
                        minLength = head - tail + 1
                        res = s[tail:head+1]
                    # Advance tail
                    if s[tail] in chars:
                        if counts[s[tail]] == 0: missing += 1
                        counts[s[tail]] += 1
                        
                    tail += 1
        
        return ''.join(res)

# 97th percentile
# Used simple dictionaries instead of Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""
        # counts = Counter(t)
        counts = {}
        for c in t:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1
        
        chars = set(t)
        missing = len(t)
        tail = 0
        res = ""
        minLength = float("inf")
        
        for head, c in enumerate(s):

            # Hit a char in t
            if c in chars:
                if counts[c] > 0: missing -= 1
                counts[c] -= 1
                # We've matched all the characters
                while not missing:
                    # Check if we have a new best res
                    if head - tail < minLength:
                        minLength = head - tail + 1
                        res = s[tail:head+1]
                    # Advance tail
                    if s[tail] in chars:
                        if counts[s[tail]] == 0: missing += 1
                        counts[s[tail]] += 1
                        
                    tail += 1
        
        return ''.join(res)