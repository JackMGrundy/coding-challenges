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

// 80ms. 92nd percentile.
/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    if (numRows === 1) {
        return s;
    }
    let rows = [];
    for (let i = 0; i < numRows; i++) {
        rows.push([]);
    }
    let rowNumber = 0;
    let increasing = true;
    
    for (let c of s) {
        rows[rowNumber].push(c);
        if (increasing) {
            rowNumber++;
        } else {
            rowNumber--;
        }
        if (rowNumber === 0 || rowNumber === numRows-1) {
            increasing = !increasing;
        }
    }
    
    let res = rows.reduce( (a,b) => {
        for (let c of b) {
            a.push(c);
        }
        return a;
    }, []);
    return res.join("");
    
};