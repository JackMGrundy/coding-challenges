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
// 0ms 100th percentile
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        }
        int longestCommon = 0;
        int minLength = Integer.MAX_VALUE;
        for (String word : strs) {
            if (word.length() < minLength) {
                minLength = word.length();
            }
        }
        
        for (int i = 0; i < minLength; i++) {
            char curChar = strs[0].charAt(i);
            for (int j = 1; j < strs.length; j++) {
                if (curChar != strs[j].charAt(i)) {
                    return strs[0].substring(0, longestCommon);
                }
            }
            longestCommon++;
        }
        
        return strs[0].substring(0, longestCommon);
    }
}