/*
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
*/

// 3ms. 94th percentile.
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        char[] c = new char[128];
        
        for (char i : s.toCharArray()) {
            c[i]++;
        }
        
        for (char i : t.toCharArray()) {
            if (c[i] != 0) {
                c[i]--;
            } else {
                return false;
            }
        }
        
        return true;
    }
}