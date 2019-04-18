"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""

# 1st attempt: 36th percentile in speed.
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def check(s: str) -> bool:
            count = 0
            for c in s:
                if c == '(': 
                    count+=1
                elif c == ')':
                    count-=1
                    if count < 0:
                        return(False)
            return(count==0)
                    
        
        level = {s}
        while True:
            correct = [x for x in level if check(x)]
            if correct:
                return(correct)
            level = { s[:i]+s[i+1:] for s in level for i in range(len(s)) }


# 2nd attempt: I looked through some faster solutions, and as far as I can tell,
# they achieve speedup by cutting down on the number of items that have to
# be checked. I found them long and confusing though...would rather have the readability.
            
a = ")(f"  
sol = Solution()
res = sol.removeInvalidParentheses(a)
print(res)