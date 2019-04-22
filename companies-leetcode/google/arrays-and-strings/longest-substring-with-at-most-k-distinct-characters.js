/*
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
*/
// 26th percentile
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var lengthOfLongestSubstringKDistinct = function(s, k) {
    let rightMost = {};
    let res = 0;
    let start = 0;
    for (let i = 0; i < s.length; i++) {
        let c = s[i];
        rightMost[c] = i;
        if (Object.keys(rightMost).length > k) {
            start = Math.min(...Object.values(rightMost))
            delete rightMost[s[start]];
            start += 1;
        }
        res = Math.max(res, i-start+1);
    }
    return res;
};


// 15th percentile
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var lengthOfLongestSubstringKDistinct = function(s, k) {
    let counts = {};
    let seen = new Set();
    let res = 0;
    let start = 0;
    for (let i = 0; i < s.length; i++) {
        let c = s[i];
        seen.add(c);
        if (Object.keys(counts).indexOf(c) !== -1) {
            counts[c] += 1
        } else {
            counts[c] = 1;
        }
        while (seen.size > k) {
            let r = s[start];
            counts[r] -= 1;
            if (counts[r] <= 0) {
                seen.delete(r);
            }
            start += 1;
        }
        res = Math.max(res, i-start+1);
    }
    
    return res;
};



// 99th percentile
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var lengthOfLongestSubstringKDistinct = function(s, k) {
    if(!s || !k) return 0
    
    let rightMost = new Map();
    let res = 0;
    let start = 0;
    for (let i = 0; i < s.length; i++) {
        let c = s[i];
        rightMost.set(c, i);
        
        if (rightMost.size > k) {
            let min = s.length,
                keyToRemove;
            
            for (let [key, value] of rightMost.entries()) {
                if (value < min) {
                    min = value;
                    keyToRemove = key;
                }
            }
            start = min + 1;
            rightMost.delete(keyToRemove);
        }
        res = Math.max(res, i-start+1);
    }
    return res;
};



// 23rd percentile
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var lengthOfLongestSubstringKDistinct = function(s, k) {
    if(!s || !k) return 0
    
    // let rightMost = new Map();
    let rightMost = {};
    let res = 0;
    let start = 0;
    for (let i = 0; i < s.length; i++) {
        let c = s[i];
        // rightMost.set(c, i);
        rightMost[c] = i;
        
        if (Object.keys(rightMost).length > k) {
            var min = s.length,
                keyToRemove;
            
            Object.keys(rightMost).forEach(key => {
                if (rightMost[[key]] < min) {
                    min = rightMost[[key]];
                    keyToRemove = key;
                }  
            })
            
            start = min + 1;
            delete rightMost[[keyToRemove]];
        }
        res = Math.max(res, i-start+1);
    }
    return res;
};