"""
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.
"""
# 100th percentile...bad practice...not good to use exceptions
# as logical operators...
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
            return True
        except:
            return False



# 100th percentile. All logic in one loop:
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        decimalPassed, ePassed, numPassed = False, False, False
        
        for i,c in enumerate(s):
            if c.isdigit():
                numPassed = True
            elif c == ".":
                if decimalPassed or ePassed:
                    return False
                decimalPassed = True
            elif c == "e":
                if ePassed or not numPassed:
                    return False
                ePassed = True
                numPassed = False
            elif c in "+-":
                if i != 0 and s[i - 1] != "e":
                    return False
            else:
                return False
        
        return numPassed


"""
Notes:

I see the value in questions like this that demonstrate an ability to organize nitty gritty details concisely...
can't say I enjoy them though. 

This question is all about gathering requirements. What are all the types of valid numbers?

The buckets include:
Integer 
    Positive
    Negative

Decimal
    Positive
    Negative

Exponent - 2e10 for example
    Positive
    Negative

Turns out we can make a concise function that catches all these cases. The key observations:
-) The only allowed chars under any circumstance are [0-9], e, ., +, -. If we see anything else, we can return False
-) . and then e is allowed. Vice versa is not 
-) At most 1 . and 1 e are allowed
-) e is only allowed after we've seen a number
-) if we see an e, there must be another number after it
-) + and - are allowed either at the beginnining or after an e

Given these we're good to go. 
"""