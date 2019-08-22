/*
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
*/

// 98th percentile. 56ms.
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length !== t.length) {
        return false;
    }
    let counts = s.split("").reduce( (a,b) => {
        a[b] = b in a ? a[b]+1 : 1;
        return a;
    }, {});
    
    t.split("").map( c => {
       counts[c] -= 1; 
    });
    
    for (let key in counts) {
        if (counts[key] != 0) {
            return false;
        }
    }
    
    return true;
};