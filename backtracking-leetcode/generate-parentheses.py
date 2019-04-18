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
# 1st attempt: 82nd percentile in speed
"""
Key intuition:
At each step (adding a character), there are two options: add ( or add ).
We can do the former if there are open parentheses left to add. We cad do the later
if there is a ( to pair it with. 
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(s='', l=0, r=0 ):
            if l + r == 2 * n: ans.append(s)
            if l < n:
                backtrack(s+'(', l+1, r)
            if r < l:
                backtrack(s+')', l, r+1)
            
        backtrack()
        return ans