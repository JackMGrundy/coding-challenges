"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter.
"""


# 59th percentile
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        charsToRemove = set()
        
        for i,c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if not stack:
                    charsToRemove.add(i)
                else:
                    stack.pop()
        
        charsToRemove.update(stack)
        
        answer = []
        for i,c in enumerate(s):
            if i not in charsToRemove:
                answer.append(c)
        
        return ''.join(answer)



# 93rd percentile
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        S = list(s)
        
        for i,c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if not stack:
                    S[i] = ""
                else:
                    stack.pop()
        
        for index in stack:
            S[index] = ""

        return ''.join(S)
