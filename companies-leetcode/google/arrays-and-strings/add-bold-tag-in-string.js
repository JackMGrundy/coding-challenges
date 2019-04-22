/*
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
Example 1:
Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
Example 2:
Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
Note:
The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].
*/
// 100th percentile 
/**
 * @param {string} s
 * @param {string[]} dict
 * @return {string}
 */
var addBoldTag = function(s, dict) {
    if (!s || !dict) return "";
    
    let bolded = new Array(s.length).fill(false);
    
    // Identify bolded characters
    for (let i = 0; i < dict.length; i++) {
        let nxtTag = dict[i];
        let start = s.indexOf(nxtTag);
        while (start !== -1) {
            bolded.fill(true, start, start+nxtTag.length)
            start = s.indexOf(nxtTag, start+1);
        }
    }
    
    // Construct final string
    let res = "";
    let bold = bolded[0];
    let nxtString = bold ? "<b>" + s[0] : s[0];
    
    for (let k = 1; k < s.length; k++) {
        // Completed a bolded / unbolded section
        if (bolded[k] !== bolded[k-1]) {
            if (bold) {
                res += nxtString + "</b>";
                bold = false;
                nxtString = s[k];
            } else {
                res += nxtString;
                bold = true;
                nxtString = "<b>" + s[k];
            }
        } 
        // Continue constructing the string
        else {
            nxtString += s[k];
        }
        // Last character
        if (k === s.length-1) {
            res = bold ? res + nxtString + "</b>" : res + nxtString;
        }
    }
    
    return res;
};