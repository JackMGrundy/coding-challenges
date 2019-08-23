"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""
# 36ms 87th percentile.
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        suffixes = ["", "Thousand", "Million", "Billion"]
        oneToNineteen = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = [None, None, "Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]

        def helper(num):
            if num == 0:
                return [""]
            res = []
            numDigitsTotal = len(str(num))
            numDigitsToProcess = 3 if (numDigitsTotal % 3) == 0 else (numDigitsTotal % 3)
            suffix = suffixes[ abs(numDigitsTotal-1) // 3 ]
            numToProcess = num // (10**(numDigitsTotal - numDigitsToProcess))
            currentNum = numToProcess
            
            if 100 <= currentNum < 1000:
                hundredsDigit = currentNum // 100
                res += list(oneToNineteen[hundredsDigit]) + list(" Hundred ")
            currentNum = currentNum % 100
            if 20 <= currentNum < 100:
                tensDigit = currentNum // 10
                onesDigit = currentNum % 10
                res += list(tens[tensDigit]) + [" "]
                if onesDigit > 0:
                    res += list(oneToNineteen[onesDigit]) + [" "]
            elif 0 < currentNum < 20:
                res += list(oneToNineteen[currentNum]) + [" "]
            
            res += list(suffix) + [" "]
            nextNum = num % (numToProcess * 10**(numDigitsTotal - numDigitsToProcess))
            return res + helper(nextNum)

        res = helper(num)
        return "".join(res).strip()
            



# 36ms 87th percentile
# Very happy with how short this has ended up
class Solution:
    def numberToWords(self, num: int) -> str:
        suffixes = ["", "Thousand ", "Million ", "Billion "]
        oneToNineteen = ["", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine ", "Ten ", "Eleven ", "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen "]
        tens = ["", "Ten ", "Twenty ","Thirty ","Forty ","Fifty ","Sixty ","Seventy ","Eighty ","Ninety "]

        def helper(num):
            if num < 20:
                return oneToNineteen[num]
            if 20 <= num < 100:
                return tens[num // 10] + oneToNineteen[num % 10]
            if 100 <= num <= 999:
                return oneToNineteen[num // 100] + "Hundred " + helper(num % 100) 
            
        res = []
        while num:
            totalDigits = len(str(num))
            digitsToProcess = totalDigits % 3 if (totalDigits % 3 != 0) else 3
            suffix = suffixes[(totalDigits-1) // 3]
            currentDigits = num // (10**(totalDigits-digitsToProcess))
            res += helper(currentDigits) + suffix
            num = num % (currentDigits * 10**(totalDigits-digitsToProcess))
            
        return "".join(res).strip() or "Zero"