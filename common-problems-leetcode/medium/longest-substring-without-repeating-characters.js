/*
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
Accepted
887,886
Submissions
3,144,652
*/
// 95th percentile
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let seen = new Set();
    let res = 0,
        tail = 0,
        curBest = 0;
    
    for(let head = 0; head < s.length; head++) {
        let c = s.charAt(head);
        if (!seen.has(c)) {
            curBest += 1;;
        } else {
            res = Math.max(res, curBest);
            while (s.charAt(tail)!==c) {
                seen.delete(s[tail]);
                tail += 1;
            }
            tail += 1;
            curBest = head - tail + 1;
        }
        seen.add(c);
    }
    return Math.max(res, curBest);
};