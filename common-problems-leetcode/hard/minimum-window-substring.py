"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""
# 140ms. 55th percentile.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        counts = collections.Counter(t)
        length = float("inf")
        start = 0
        missing = len(t)
        left = 0
        
        for right,c in enumerate(s):
            if c in counts:
                if 0 < counts[c]:
                    missing -= 1
                counts[c] -= 1
                
            while missing == 0:
                if right - left + 1 < length:
                    start, length = left, right - left + 1
                
                if s[left] in counts:
                    if counts[s[left]] == 0:
                        missing += 1
                    counts[s[left]] += 1
                
                left += 1
        
        return "" if length == float("inf") else s[start:start + length]


"""
Notes:

1) The most straightforward solution is...well..straightforwards. You have right
and left pointers. You advance the right pointer until you have a suitable window.
Then as long as the window remains desirable (contains all the chars), you keep
advancing the left pointer. 

In the worst case, the left and right pointers both visit every element of S. Time
complexity is O(|S| + |T|). Space complexity is also O(|S| + |T|). |S| when the
window size equals the entire string. |T| when T has all unique characters. 


^This is actually about as good as it gets. There is another solution for a special case.
The idea is to preprocess S to filter out characters that are not in t. As in:
S = "ABCDDDDDDEEAFFBC" T = "ABC"
  filtered_S = [(0, 'A'), (1, 'B'), (2, 'C'), (11, 'A'), (14, 'B'), (15, 'C')]

^We need the indices so that we can return a window size. 

It only makes sense to do this if S has a lot of characters that are not in S. 

"""