"""
Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.

 

Example 1:

Input: s = "owoztneoer"
Output: "012"
Example 2:

Input: s = "fviefuro"
Output: "45"
 

Constraints:

1 <= s.length <= 105
s[i] is one of the characters ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"].
s is guaranteed to be valid.
"""

# First attempt: 15th percentile
from collections import defaultdict
class Solution:
    def originalDigits(self, s: str) -> str:
        def getCharDict(s):
            charCounts = defaultdict(int)
            for c in s:
                charCounts[c] += 1
            return charCounts

        digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        digitCounts = {}
        for i,digit in enumerate(digits):
            digitCounts[str(i)] = getCharDict(digit)

        """       
              first pass    second pass
         zero  -> z
         one   ->               o
         two   -> w
         three ->               r
         four  -> u
         five  ->               f
         six   -> x
         seven ->               s
         eight -> g
         nine  ->
        """
        digitsInAnswer = { str(i):0 for i in range(10) }
        
        sDigitCounts = getCharDict(s)
        
        def accountForDigit(digit, indicatorChar, sDigitCounts, digitCounts, digitsInAnswer):
            while 0 < sDigitCounts[indicatorChar]:
                for char, count in digitCounts[digit].items():
                    sDigitCounts[char] -= count
                digitsInAnswer[digit] += 1

        accountForDigit('0', 'z', sDigitCounts, digitCounts, digitsInAnswer)
        accountForDigit('2', 'w', sDigitCounts, digitCounts, digitsInAnswer)
        accountForDigit('4', 'u', sDigitCounts, digitCounts, digitsInAnswer)
        accountForDigit('6', 'x', sDigitCounts, digitCounts, digitsInAnswer)
        accountForDigit('8', 'g', sDigitCounts, digitCounts, digitsInAnswer)
        
        accountForDigit('1', 'o', sDigitCounts, digitCounts, digitsInAnswer)
        accountForDigit('3', 'r', sDigitCounts, digitCounts, digitsInAnswer)
        accountForDigit('5', 'f', sDigitCounts, digitCounts, digitsInAnswer)
        accountForDigit('7', 's', sDigitCounts, digitCounts, digitsInAnswer)
        
        accountForDigit('9', 'n', sDigitCounts, digitCounts, digitsInAnswer)
        
        answer = []
        for char, count in digitsInAnswer.items():
            answer += [char]*count
        
        return ''.join(answer)



# 2nd attempt. 99.66%  : )
from collections import Counter
class Solution:
    def originalDigits(self, s: str) -> str:
        sCharCounts = Counter(s)
        answer = [ 0 for _ in range(10) ]
        
        # z only in zero
        answer[0] = sCharCounts['z']
        # w only in two
        answer[2] = sCharCounts['w']
        # u only in four
        answer[4] = sCharCounts['u']
        # x only in six
        answer[6] = sCharCounts['x']
        # g only in eight
        answer[8] = sCharCounts['g']
        # h only in eight and three
        answer[3] = sCharCounts['h'] - answer[8]
        # f only in four and five
        answer[5] = sCharCounts['f'] - answer[4]
        # s only in six and seven
        answer[7] = sCharCounts['s'] - answer[6]
        # i only in five, size, eight, and nine
        answer[9] = sCharCounts['i'] - answer[5] - answer[6] - answer[8]
        # o only in zero, two, four, and one
        answer[1] = sCharCounts['o'] - answer[0] - answer[2] - answer[4]
        
        return ''.join( [ str(digit)*count for digit,count in enumerate(answer) ] )
