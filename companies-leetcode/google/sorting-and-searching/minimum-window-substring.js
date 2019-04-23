/*
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
*/
// 18th percentile
/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    if (s.length===0 || t.length===0) return "";
    if (s === t) return s;
    
    let counts = {};
    for (let i = 0; i < t.length; i++) {
        let c = t[i];
        if (Object.keys(counts).indexOf(c) === -1) counts[c] = 1;
        else counts[c] += 1;
    }
    let missing = t.length,
        chars = new Set(t),
        res = "",
        tail = 0,
        maxLength = Number.MAX_SAFE_INTEGER;
    
    for (let head = 0; head < s.length; head++) {
        let c = s[head];
        // hit a char in t
        if ( chars.has(c) ) {
            if (counts[c] > 0) missing -= 1;
            counts[c] -= 1;
            
            // hit all the chars in t
            while (missing===0) {
                // check for a new best res
                if ( head - tail + 1 < maxLength) {
                    maxLength = head - tail + 1;
                    res = s.slice(tail, head+1);
                }
                
                // squeeze the interval
                // tail char is in t
                let ct = s[tail];
                if ( Object.keys(counts).indexOf(ct) !== -1) {
                    // will we no longer have all the chars in t after eliminating the tail?
                    if ( counts[ct] === 0) missing += 1;
                    counts[ct] += 1;
                }
                tail += 1;
            }
        }
    }
    
    return res;
};



// 19th percentile (basically no difference)
/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    if (s.length===0 || t.length===0) return "";
    if (s === t) return s;
    
    let counts = {};
    for (let i = 0; i < t.length; i++) {
        let c = t[i];
        if (Object.keys(counts).indexOf(c) === -1) counts[c] = 1;
        else counts[c] += 1;
    }
    let missing = t.length,
        chars = new Set(t),
        resMin = 0,
        resMax = 0,
        tail = 0,
        maxLength = Number.MAX_SAFE_INTEGER;
    
    for (let head = 0; head < s.length; head++) {
        let c = s[head];
        // hit a char in t
        if ( chars.has(c) ) {
            if (counts[c] > 0) missing -= 1;
            counts[c] -= 1;
            
            // hit all the chars in t
            while (missing===0) {
                // check for a new best res
                if ( head - tail + 1 < maxLength) {
                    maxLength = head - tail + 1;
                    resMin = tail;
                    resMax = head+1;
                }
                
                // squeeze the interval
                // tail char is in t
                let ct = s[tail];
                if ( Object.keys(counts).indexOf(ct) !== -1) {
                    // will we no longer have all the chars in t after eliminating the tail?
                    if ( counts[ct] === 0) missing += 1;
                    counts[ct] += 1;
                }
                tail += 1;
            }
        }
    }
    
    return s.slice(resMin, resMax);
};


// 63rd percentile...forgot to use set
/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    if (s.length===0 || t.length===0) return "";
    if (s === t) return s;
    
    let counts = {};
    for (let i = 0; i < t.length; i++) {
        let c = t[i];
        if (Object.keys(counts).indexOf(c) === -1) counts[c] = 1;
        else counts[c] += 1;
    }
    let missing = t.length,
        chars = new Set(t),
        res = "",
        tail = 0,
        maxLength = Number.MAX_SAFE_INTEGER;
    
    for (let head = 0; head < s.length; head++) {
        let c = s[head];
        // hit a char in t
        if ( chars.has(c) ) {
            if (counts[c] > 0) missing -= 1;
            counts[c] -= 1;
            
            // hit all the chars in t
            while (missing===0) {
                // check for a new best res
                if ( head - tail + 1 < maxLength) {
                    maxLength = head - tail + 1;
                    res = s.slice(tail, head+1);
                }
                
                // squeeze the interval
                // tail char is in t
                let ct = s[tail];
                if ( chars.has(ct) ) {
                    // will we no longer have all the chars in t after eliminating the tail?
                    if ( counts[ct] === 0) missing += 1;
                    counts[ct] += 1;
                }
                tail += 1;
            }
        }
    }
    
    return res;
};



// 71st percentile
// Interesting that adding curly braces around all if's and else's speeds things up a bit
/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    if (s.length===0 || t.length===0) return "";
    if (s === t) return s;
    
    let counts = {};
    for (let i = 0; i < t.length; i++) {
        let c = t[i];
        if (Object.keys(counts).indexOf(c) === -1) {
            counts[c] = 1;
        }
        else {
            counts[c] += 1;
        }
    }
    let missing = t.length,
        chars = new Set(t),
        res = "",
        tail = 0,
        maxLength = Number.MAX_SAFE_INTEGER;
    
    for (let head = 0; head < s.length; head++) {
        let c = s[head];
        // hit a char in t
        if ( chars.has(c) ) {
            if (counts[c] > 0) {
                missing -= 1;
            }
            counts[c] -= 1;
            
            // hit all the chars in t
            while (missing===0) {
                // check for a new best res
                if ( head - tail + 1 < maxLength) {
                    maxLength = head - tail + 1;
                    res = s.slice(tail, head+1);
                }
                
                // squeeze the interval
                // tail char is in t
                let ct = s[tail];
                if ( chars.has(ct) ) {
                    // will we no longer have all the chars in t after eliminating the tail?
                    if ( counts[ct] === 0) {
                        missing += 1;
                    }
                    counts[ct] += 1;
                }
                tail += 1;
            }
        }
    }
    
    return res;
};


// 87th percentile
// Avoided using Object.keys(counts).indexOf(c)
// Note...this is a ~15 percentile jump, but only 88ms to 84ms in absolute time
/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    if (s.length===0 || t.length===0) return "";
    if (s === t) return s;
    
    let counts = {};
    for (let i = 0; i < t.length; i++) {
        counts[t[i]] = counts[t[i]] ? counts[t[i]] + 1 : 1;
    }
    
    let missing = t.length,
        chars = new Set(t),
        res = "",
        tail = 0,
        maxLength = Number.MAX_SAFE_INTEGER;
    
    for (let head = 0; head < s.length; head++) {
        let c = s[head];
        // hit a char in t
        if ( chars.has(c) ) {
            if (counts[c] > 0) {
                missing -= 1;
            }
            counts[c] -= 1;
            
            // hit all the chars in t
            while (missing===0) {
                // check for a new best res
                if ( head - tail + 1 < maxLength) {
                    maxLength = head - tail + 1;
                    res = s.slice(tail, head+1);
                }
                
                // squeeze the interval
                // tail char is in t
                let ct = s[tail];
                if ( chars.has(ct) ) {
                    // will we no longer have all the chars in t after eliminating the tail?
                    if ( counts[ct] === 0) {
                        missing += 1;
                    }
                    counts[ct] += 1;
                }
                tail += 1;
            }
        }
    }
    
    return res;
};