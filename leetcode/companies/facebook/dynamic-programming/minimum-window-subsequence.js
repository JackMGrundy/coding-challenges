/*
Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:

Input: 
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation: 
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.
 

Note:

All the strings in the input will only contain lowercase letters.
The length of S will be in the range [1, 20000].
The length of T will be in the range [1, 100].
*/

// 1st attempt: 50th percentile...simpler solutions exist
/**
 * @param {string} S
 * @param {string} T
 * @return {string}
 */
var minWindow = function(S, T) {
    let m = T.length,
        n = S.length,
        d = {};
    
    // reference dictionary of locations of chars in subsequence
    for (let i = 0; i < m; i++) {
        let c = T[i];
        if ( !Object.keys(d).includes(c) ) {
            d[c] = [i];
        } else {
            d[c].push(i);
        }
    }
    
    // dp array to keep track of possible windows
    let dp = [];
    for (i = 0; i < m; i++) dp.push(-1);
    
    var k = 0,
        windowLength = Number.MAX_SAFE_INTEGER,
        windowStart = -1,
        l;
    // iterate through search string
    for (let j = 0; j < n; j++) {
        let c = S[j];
        // character is in target subsequence
        if ( Object.keys(d).includes(c) ) {
            // each occurrence of c in target subsequence
            for (k = d[c].length-1; k >= 0; k--) {
                l = d[c][k];
                // start of target subsequence
                if ( l===0 ) {
                    dp[0] = j;
                } 
                /// another character in target subsequence
                else {
                    dp[l] = dp[l-1];
                }
                // character is end of subsequence, we have already matched
                // every target character, and the new window discovered is
                // smaller than the best one found so far
                if ( l === m - 1 && dp[l] !== -1 && ( j - dp[l] + 1 ) < windowLength ) {
                    windowStart = dp[l];
                    windowLength = j - dp[l] + 1;
                }
            }
        }
    }
    
    return windowLength <= n ? S.slice(windowStart, windowStart+windowLength) : ""; 
};