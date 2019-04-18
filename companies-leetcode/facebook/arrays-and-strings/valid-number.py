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
# 1st attempt: 100th percentile...bad practice though...not good to use exceptions
# as logical operators...maybe ok since it's so concise
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
            return(True)
        except:
            return(False)

# 2nd attempt: tried writing helper methods like "isPositiveInt" and "isFloat"...
# Quickly became impossible to work with


# 3rd attempt: 100th percentile. All logic in one loop:
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        decimalPassed = False
        ePassed = False
        numberPassed = False
        
        for index, c in enumerate(s):
            if c.isdigit():
                numberPassed = True
            elif c==".":
                if decimalPassed or ePassed: 
                    return(False)
                decimalPassed = True
            elif c=="e":
                if ePassed or not numberPassed:
                    return(False)
                ePassed = True
                numberPassed = False
            elif c in "+-":
                if index!=0 and s[index-1]!="e":
                    return(False)
            else:
                return(False)
        return(numberPassed)