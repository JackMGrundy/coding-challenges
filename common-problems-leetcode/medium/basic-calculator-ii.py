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
# 92ms. 88 percentile.
class Solution:
    def calculate(self, s: str) -> int:
        s = list(s)
        num = 0
        stack = []
        lastOp = None
        
        for i,c in enumerate(s):
            if c.isdigit():
                num = num*10 + int(c)
            if (c in "+-*/") or (i == len(s)-1):
                if not lastOp:
                    stack.append(num)
                elif lastOp == "+":
                    stack.append(num)
                elif lastOp == "-":
                    stack.append(-num)
                elif lastOp == "*":
                    stack[-1] *= num
                elif lastOp == "/":
                    stack[-1] = int(stack[-1]/num)
                num = 0
                lastOp = c
        return sum(stack)