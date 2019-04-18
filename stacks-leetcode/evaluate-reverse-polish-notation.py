"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""
# 1st attempt: 80th percentile in speed
"""
I simultaneously really like and dislike this problem
Pro: It's an interesting bit of knowledge (reverse polish notation). Brings up the python operator library.
Brings up an interesting design division by Guido with respect to remainder behavior for negative division.

Neg: The one challenging bit is just an obnixous result of a very language specific detail (negative divison)
"""
import operator
import math
ops = { "+":operator.add, "-":operator.sub, "/t":operator.truediv, "/":operator.floordiv, "*":operator.mul }

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens: return 0
        s = []
        res = 0
        operators = ["+", "-", "*", "/"]
        tokens = [ int(t) if t not in operators else t for t in tokens ]
        
        for token in tokens:
            if token in operators:
                a, b = s.pop(), s.pop()
                if token=="/" and ( ( a < 0 and b > 0 ) or ( b < 0 and a > 0 ) ):
                    c = ops[token + "t"](b, a)
                    c = -1*math.floor(abs(c))
                else:
                    c = ops[token](b, a)
                s.append(c)
            else:
                s.append(token)
        
        return s[0]
    
    
# 2nd attempt: 80th percentile but cleaner
import operator
import math
ops = { "+":operator.add, "-":operator.sub, "/t":operator.truediv, "/":operator.floordiv, "*":operator.mul }

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens: return 0
        s = []

        for token in tokens:
            if token in "+-*/":
                n2 = s.pop()
                n1 = s.pop()
                if token=="+":
                    s.append(n1 + n2)
                elif token=="-":
                    s.append(n1 - n2)
                elif token=="*":
                    s.append(n1 * n2)
                elif token=="/":
                    s.append(int(n1 / n2))
            else:
                s.append(int(token))
            
        return s[0]
