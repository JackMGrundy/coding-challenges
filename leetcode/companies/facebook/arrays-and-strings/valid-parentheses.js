/*
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
*/
// 1st attempt: 72nd percentile in speed
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    if (!s) return(true);
    if (s.length % 2 === 1) return(false);
    var stack = [];
    var d = {")":"(", "}":"{", "]":"["}
    for (let i = 0; i < s.length; i++) {
        let c = s[i];
        if ( Object.values(d).includes(c) ) {
            stack.push(c);
            continue;
        } else {
            if ( stack.length>0 && d[c]===stack.pop() ) {
                continue;
            } else {
                return(false);
            }
        }
    }
    
    return(true ? stack.length===0 : false);
};