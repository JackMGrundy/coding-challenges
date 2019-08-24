/*
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
*/
// 60ms. 58th percentile.
/**
 * @param {string[]} strs
 * @return {string}
 */
/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if (strs.length === 0) {
        return "";
    }
    if (strs.length === 1) {
        return strs[0];
    }
    let longestCommon = 0;
        
    for (let i = 0; i < strs[0].length; i++) {
        let curChar = strs[0][i];
        for (let j = 1; j < strs.length; j++) {
            if (strs[j][i] !== curChar) {
                return strs[0].slice(0, longestCommon);
            }
        }
        longestCommon++;
    }
    return strs[0].slice(0, longestCommon);
};