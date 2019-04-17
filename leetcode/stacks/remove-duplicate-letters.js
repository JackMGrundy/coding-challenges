/*
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"
*/
// 1st attempt: 97th percentile in speed O(N)
/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicateLetters = function(s) {
    let lasts = {};
    let visited = {};
    let stack = [];
    s = s.split('')
    // Get last appearance of each character
    for (let i = 0; i < s.length; i++) {
        let c = s[i];
        lasts[c] = i;
        visited[c] = false;
    }
    
    for (i = 0; i < s.length; i++) {
        let c = s[i];
        if (visited[c]) continue;
        
        while (stack.length > 0 && stack[stack.length-1].charCodeAt(0) > c.charCodeAt(0) && i < lasts[stack[stack.length-1]] ) {
            visited[stack.pop()] = false;       
        }
        
        stack.push(c);
        visited[c] = true;
    }
    
    return stack.join('');
};