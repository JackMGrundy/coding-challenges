/*
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
*/

// 60ms. 90th percentile.
/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var addStrings = function(num1, num2) {
    num1 = num1.split("");
    num2 = num2.split("");
    let carry = 0;
    let res = [];
    
    while (num1.length > 0 || num2.length > 0) {
        let d1 = 0;
        let d2 = 0;
        if (num1.length > 0) {
            d1 = num1.pop().charCodeAt(0) - '0'.charCodeAt(0);
        }
        if (num2.length > 0) {
            d2 = num2.pop().charCodeAt(0) - '0'.charCodeAt(0);
        }
        
        let temp = d1 + d2 + carry;
        carry = temp > 9 ? 1 : 0;
        res.push( (temp % 10) );
    }
    
    if (carry === 1){
        res.push(1);
    }
    
    res.reverse();
    return res.reduce( (a,b) => {
        return a + b;
    }, "");
};


// ...reminder, as much as I love reduce...simpler is better
/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var addStrings = function(num1, num2) {
    num1 = num1.split("");
    num2 = num2.split("");
    let carry = 0;
    let res = [];
    
    while (num1.length > 0 || num2.length > 0) {
        let d1 = 0;
        let d2 = 0;
        if (num1.length > 0) {
            d1 = num1.pop().charCodeAt(0) - '0'.charCodeAt(0);
        }
        if (num2.length > 0) {
            d2 = num2.pop().charCodeAt(0) - '0'.charCodeAt(0);
        }
        
        let temp = d1 + d2 + carry;
        carry = temp > 9 ? 1 : 0;
        res.push( (temp % 10) );
    }
    
    if (carry === 1){
        res.push(1);
    }
    
    res.reverse();
    return res.join("");
};