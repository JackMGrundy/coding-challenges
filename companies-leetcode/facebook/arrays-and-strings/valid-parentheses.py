"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""
# 1st attempt: 83rd percentile in speed
class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return(True)
        if len(s) % 2 == 1: return(False)
        stack = []
        d = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in d.values(): 
                stack.append(c)
            elif c in d.keys():
                if stack and d[c]==stack[-1]:
                    stack.pop()
                else:
                    return(False)
            else:
                return(False)
        
        return(not stack)