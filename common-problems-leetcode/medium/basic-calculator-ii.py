"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""
# 84ms. 95 percentile.
class Solution:
    def calculate(self, s: str) -> int:
        operator = "+"
        num = 0
        stack = []
        s = s + "$"
        
        for i,c in enumerate(s):
            if c == " ":
                continue
            elif c.isdigit():
                num = num*10 + int(c)
            else:
                if operator == "+":
                    stack.append(num)
                elif operator == "-":
                    stack.append(-num)
                elif operator == "*":
                    stack.append(stack.pop() * num)
                elif operator == "/":
                    stack.append( int(stack.pop() / num) )
                
                operator = c
                num = 0

        return sum(stack)