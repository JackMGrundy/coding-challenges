/*
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
*/
// 64ms. 92nd percentile.
/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {
    s = s.split("");
    let stack = [];
    let num = 0;
    let lastOp = "!";
    for (let i = 0; i < s.length; i++) {
        let c = s[i];

        if ('0' <= c && c <= '9') {
            num = num*10 + parseInt(c);
        }
        if ("+-*/".includes(c) || i === s.length-1) {
            if (lastOp === "!") {
                stack.push(num);
            }
            else if (lastOp === "+") {
                stack.push(num);
            }
            else if (lastOp === "-") {
                stack.push(-num);
            }
            else if (lastOp === "*") {
                stack.push(stack.pop()*num);
            }
            else if (lastOp === "/") {
                let term = stack[stack.length-1];
                if (term < 0) {
                    stack.push(Math.ceil(stack.pop()/num));
                } else {
                    stack.push(Math.floor(stack.pop()/num));
                }
            }
            num = 0;
            lastOp = c;
        }
    }
    
    return stack.reduce( (a,b) => {
        return a+b;
    }, 0);
};