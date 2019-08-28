/*
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
*/

// 6ms. 63rd percentile.
class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1) {
            return s;
        }
        List<StringBuilder> rows = new ArrayList<StringBuilder>();
        for (int i = 0; i < numRows; i++) {
            rows.add( new StringBuilder());
        }
        int rowNumber = 0;
        boolean increasing = true;
        
        for (int i = 0; i < s.length(); i++) {
            rows.get(rowNumber).append(s.charAt(i));
            
            if (increasing) {
                rowNumber++;
            } else {
                rowNumber--;
            }
            
            if (rowNumber == 0 || rowNumber == numRows-1) {
                increasing = !increasing;
            }
        }
        
        StringBuilder res = new StringBuilder();
        for (StringBuilder sb : rows) {
            res.append(sb);
        }
        
        return res.toString();
    }
}