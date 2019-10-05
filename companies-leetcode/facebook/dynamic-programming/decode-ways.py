"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""


# Simple backtracking dfs with memoization
# Without memoization it times out:
# 32ms. 97th percentile. 
class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        
        def dfs(curCharIndex):
            if curCharIndex in memo:
                return memo[curCharIndex]
            elif curCharIndex == len(s):
                return 1 
            elif curCharIndex > len(s):
                return 0
            
            c = s[curCharIndex]
            if c == '0':
                return 0
            elif c == '1':
                memo[curCharIndex] = dfs(curCharIndex+1) + dfs(curCharIndex+2)
            elif c == '2' and curCharIndex+1 < len(s) and s[curCharIndex+1] in ['0', '1', '2', '3', '4', '5', '6']:
                memo[curCharIndex] = dfs(curCharIndex+1) + dfs(curCharIndex+2)
            else:
                memo[curCharIndex] = dfs(curCharIndex+1)
            return memo[curCharIndex]
                
        return dfs(0)


# Built ins for caching
# Without memoization it times out:
# 32ms. 97th percentile. 
from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        
        @lru_cache(maxsize=None)
        def dfs(sI):
            if sI == len(s):
                return 1
            elif len(s) < sI:
                return 0
            
            c = s[sI]
            
            if c == '0':
                return 0
            elif c == '1':
                return dfs(sI + 1) + dfs(sI + 2)
            elif c == '2' and sI + 1 < len(s) and s[sI + 1] in '0123456':
                return dfs(sI + 1) + dfs(sI + 2)
            else:
                return dfs(sI + 1)
                
        return dfs(0)



# Instead of thinking of decoding, think of "taking steps" towards the end.
# You can take 1 step at a time, except when you hit a pair of #'s between 10 and 26. 
# Given this perspective, key intuition is: #of ways of getting to point 
# n = sumOverI(num of ways of getting to n from previous spot i) where i are spots that are
# 1 action away. 
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == "0": return(0)    
        last = 1
        cur = 1

        for i in range(1, len(s)):
            # 0's are only valid if they are paired with a preceding 1 or 2. Otherwise, the encoding
            # is invalid. 
            if s[i] == "0" and s[i - 1] not in ["1", "2"]: 
                return(0)
            # 3 cases:
            # - We hit a 0. Given previous if, the 0 must be paired with a 1 or 2. Now that
            #   1 or 2 cannot be used to generate new combinations. Reset the cur number of
            #   combinations to what it was before considering the 1 or 2.
            if s[i] == "0":
                last, cur = [cur, last]
            # - We hit a # and the last 2 nums are between 10 and 26 inclusive. Then
            #   f(n) = f(n-1)+f(n-2)
            elif "10" <= s[(i - 1):(i + 1)] <= "26":
                last, cur = [cur, cur + last]
            # - We hit a # and the 2 nums are not between 10 and 26. Then simply set f(n) to f(n-1)
            else:
                last, cur = [cur, cur]
        return cur
