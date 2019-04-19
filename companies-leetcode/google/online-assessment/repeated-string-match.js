/*
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
*/
// 1st attempt: 100th percentile in speed
/**
 * @param {string} A
 * @param {string} B
 * @return {number}
 */
var repeatedStringMatch = function(A, B) {
    let x = Math.ceil(B.length / A.length);
    let temp = A.repeat(x);
    if ( temp.includes(B) ) return x;
    temp += A;
    if ( temp.includes(B) ) return x+1;
    return -1;
};