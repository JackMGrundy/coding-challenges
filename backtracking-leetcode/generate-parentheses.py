"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
# 49 percentile.
# Simple brute force
class Solution(object):
    def generateParenthesis(self, n):
        validStrings = []
        
        def helper(n, string, opens, closeds):
            if opens < closeds:
                return
            if n == 0: 
                if opens == closeds:
                    validStrings.append(string)
                return

            helper(n-1, string + "(", opens+1, closeds)
            helper(n-1, string + ")", opens, closeds+1)
        
        
        helper(n*2, "", 0, 0)
        return validStrings


# 40ms. 78 percentile. 
"""
Key intuition:
At each step (adding a character), there are two options: add ( or add ).
We can do the former if there are open parentheses left to add. We cad do the later
if there is a ( to pair it with. 
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        validStrings = []

        def helper(opensLeft, closesLeft, s):
            nonlocal validStrings
            if opensLeft == closesLeft == 0:
                validStrings.append(s)
                return
            elif opensLeft == closesLeft:
                helper(opensLeft-1, closesLeft, s+"(")
            else:
                if 0 < opensLeft:
                    helper(opensLeft-1, closesLeft, s+"(")
                helper(opensLeft, closesLeft-1, s+")")
        
        helper(n, n, "")
        return validStrings

"""
Notes:
DFS:  At  each  level, we have a number opens and a number of closes left we can
use.  If  we're  out  of  both,  we've finished a string and we append it to the
result. If we have the same number of each (not 0), then we must use only branch
to  using  an  open.  Otherwise,  if we have an open left, we can branch with an
additional open. And either way we can branch with an additional close.         

"""