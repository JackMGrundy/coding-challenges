/*
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
*/

// 104ms. 24th percentile.
// lazy...
/**
 * @param {string[]} A
 * @return {string[]}
 */
var commonChars = function(A) {
    let charCounts = A[0].split("").reduce( (a,b) => {
        a[b] = b in a ? a[b]+1 : 1;
        return a;
    }, {});
    
    
    let temp = {};
    for (let word of A.slice(1, A.length)) {
        let temp = word.split("").reduce( (a,b) => {
            a[b] = b in a? a[b]+1: 1;
            return a
        }, {});

        for (let key in charCounts) {
            let oldCount = charCounts[key];
            let tempCount = key in temp ? temp[key] : 0;
            charCounts[key] = Math.min(tempCount, oldCount);
        }
    }
    
    let res = [];
    for (let key in charCounts) {
        for (let i = 0; i < charCounts[key]; i++) {
            res.push(key);
        }
    }
    
    return res;
};