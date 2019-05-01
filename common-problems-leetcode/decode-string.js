/*
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
Accepted
97.9K
Submissions
219.9K
*/
// 100th percentile. 56ms. List building
/*
Big lesson here...in javascript, most modern engines (like v8) are optimized to 
convert string building to list building under the hood. Unlike Python, Java, etc.
so do whatever is most readable. 
...see below for equal speed string building
*/
/**
 * @param {string} s
 * @return {string}
 */
/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function(s) {
    let res = [],
        stack = [],
        opens = 0;
    s = s.split('');
    
    for (let i = 0; i < s.length; i++) {
        c = s[i];
        
        if (c === "[") {
            opens++;
        } else if (c === "]") {
            opens--;
             
            // Get string portion of group
            let cur = stack.pop();
            let temp = [];
            while (cur !== "[") {
                temp.unshift(cur);
                cur = stack.pop();
            }
            
            let d = stack.pop();
            let k = [];

            // Get multiplier
            while (stack.length > 0 && !isNaN(parseInt(d))) {
                k.unshift(d);
                d = stack.pop();
            }

            if (!isNaN(parseInt(d))) {
                k.unshift(d);
            } else {
                stack.push(d);
            }
            
            k = parseInt(k.join(''));
            stack.push(temp.join('').repeat(k));
            if (opens === 0) {
                res.push(stack.join(''));
                stack = [];
            }
            
            continue;
        }
        
        stack.push(c);
    }
    return res.join('') + stack.join('');
};




// 100th percentile. 56 ms. String building approach. 
/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function(s) {
    let res = "",
        stack = [],
        opens = 0;
    s = s.split('');
    
    for (let i = 0; i < s.length; i++) {
        c = s[i];
        
        if (c === "[") {
            opens++;
        } else if (c === "]") {
            opens--;
             
            // Get string portion of group
            let cur = stack.pop();
            let temp = "";
            while (cur !== "[") {
                temp = cur + temp;
                cur = stack.pop();
            }
            
            let d = stack.pop();
            let k = "";

            // Get multiplier
            while (stack.length > 0 && !isNaN(parseInt(d))) {
                k = d + k;
                d = stack.pop();
            }

            if (!isNaN(parseInt(d))) {
                k = d + k;
            } else {
                stack.push(d);
            }
            
            k = parseInt(k);
            stack.push(temp.repeat(k));
            if (opens === 0) {
                res += stack.join('');
                stack = [];
            }
            
            continue;
        }
        
        stack.push(c);
    }
    return res + stack.join('');
};