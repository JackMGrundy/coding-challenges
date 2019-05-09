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
import java.util.Set;
import java.util.HashSet;
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> seen = new HashSet<Character>();
        int tail = 0;
        int res = 0;
        char[] cs = s.toCharArray();
        
        for (int head = 0; head < cs.length; head++) {
            char c = s.charAt(head);
            if (seen.contains(c)) {
                res = Math.max(res, head - tail);
                while (cs[tail]!=c) {
                    seen.remove(cs[tail++]);
                }
                tail++;
            }
            seen.add(c);
        }        
        return Math.max(res, cs.length - tail);
    }
}