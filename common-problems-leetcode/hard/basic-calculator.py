"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
Accepted
123K
Submissions
361.1K
"""
# 84ms. 91 percentile.
class Solution:
    def calculate(self, s: str) -> int:
        total, num, sign, stack = 0, 0, 1, []
        
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c in ["+", "-"]:
                total += sign*num
                sign = [-1, 1][c=="+"]
                num = 0
            elif c == "(":
                stack.append(total)
                stack.append(sign)
                total, sign = 0, 1
            elif c == ")":
                total += sign*num
                total *= stack.pop()
                total += stack.pop()
                sign, num = 1, 0
        
        return total + sign*num



"""
Notes:
Reverse the string. Make a stack. If you see a parenthesis, push it on...start adding elements 
until you see a matching closed parenthesis...then start popping and calculating...

Notes...
If you see a multidigit number I think it's easier to keep building it up until you see a non digit...
then push that onto the stack. The alternative is to deal with multiplying values by 10 as you pop them off...


A way I like better:
Iterate straight through. Keep track of the sign of the current number being processed. Whenever you hit
a new term, apply the sign to get the num. 

When you hit an open parenthesis, store the current total on the stack along with the sign of the parenthesis'
enclosed value and start a new total with default sign positive. 

When you hit a close parenthesis, update the total with the last value in the parentheses. You know the sign will
be on top of the stack...and we've already summed up the total, so we can flip it to the right sign. Then
we know the total before we started the parenthsis is the next value on the stack...so we can add those together.

"""