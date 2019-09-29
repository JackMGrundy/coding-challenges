"""
Implement a basic calculator to evaluate a simple expression string.            

The  expression  string may contain open ( and closing parentheses ), the plus +
or minus sign -, non-negative integers and empty spaces .                       

The  expression string contains only non-negative integers, +, -, *, / operators
,  open  (  and  closing  parentheses  ) and empty spaces . The integer division
should truncate toward zero.                                                    

You  may  assume  that  the  given  expression is always valid. All intermediate
results will be in the range of [-2147483648, 2147483647].                      

Some examples:                                                                  

"1 + 1" = 2                                                                     

" 6-4 / 2 " = 4                                                                 

"2*(5+5*2)/3+(6/2+8)" = 21                                                      

"(2+6* 3+5- (3*14/7+2)*5)+3"=-12                                                
"""
# 48ms. 93 percentile.
class Solution:
    def calculate(self, s: str) -> int:
        s += "$"
        
        def helper(s, stack, i):
            num, operation = 0, '+'
            
            while i < len(s):
                character = s[i]
                if character.isdigit():
                    num = num*10 + int(character)
                    i += 1
                elif character == ' ':
                    i += 1
                elif character == "(":
                    num, i = helper(s, [], i+1)
                else:
                    if operation == '+':
                        stack.append(num)
                    elif operation == '-':
                        stack.append(-num)
                    elif operation == '/':
                        stack.append(int(stack.pop() / num) )
                    elif operation == '*':
                        stack.append(stack.pop() * num)
                    
                    i += 1
                    num = 0
                    if character == ')':
                        return (sum(stack), i)
                    operation = character
            
            return sum(stack)
        
        return helper(s, [], 0)
        
"""
Notes:

Careful handling of if cases + use of recursion to deal with parentheses.    

"""