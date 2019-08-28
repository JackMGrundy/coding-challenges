"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""
# 68ms. 63 percentile
# Traversing the string in zigzag order
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        firstJump = 2*(numRows - 1)
        secondJump = 0
        res = []
        s = list(s)
        start = 0
        
        while True:
            if len(res) == len(s):
                return ''.join(res)
            
            i = start
            res.append(s[i])
            
            while i < len(s):
                i += firstJump
                if i < len(s) and firstJump != 0:
                    res.append(s[i])
                
                i += secondJump
                if i < len(s) and secondJump != 0:
                    res.append(s[i])
            
            firstJump -= 2
            secondJump += 2
            start += 1


# 60ms. 85th percentil.
# Figure out what row each character goes into, then combine.
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = [ [] for x in range(numRows) ]
        isIncreasing = True
        rowNumber = 0
        
        for c in s:
            rows[rowNumber].append(c)
            if isIncreasing:
                rowNumber += 1
            else:
                rowNumber -= 1
            
            if rowNumber == 0 or rowNumber == numRows - 1:
                isIncreasing = not isIncreasing
        
        res = []
        for row in rows:
            res += row
        
        return ''.join(res)