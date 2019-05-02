/*
Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Follow up:

For C programmers, try to solve it in-place in O(1) extra space.

Accepted
274,305
Submissions
1,662,513
*/
// Laughbly bad, hacked together as fast as possible solution...slower than javascript.
// 5th percentile. 60ms.
class Solution {
    public String reverseWords(String s) {

        StringBuilder sb = new StringBuilder();
        for (String c : s.trim().split("")) {
            sb.append(c);
        }
        sb.reverse();
        
        StringBuilder res = new StringBuilder();
        String[] temp = sb.toString().split("");
        sb.setLength(0);
        for (int i = 0; i < temp.length; i++) {
            String c = temp[i];
            if (c.equals(" ")) {
                sb.reverse();
                res.append(sb.toString().trim());
                if (sb.length() > 0) {
                    res.append(" ");
                }
                sb.setLength(0);
            } else if (i == temp.length-1) {
                sb.append(c);
                sb.reverse();
                res.append(sb.toString());                
            } else {
                sb.append(c);
            }
        }
        
        return res.toString();
    }
}


// 100th percentile. 1ms.
class Solution {
    public String reverseWords(String s) {

        String[] words = s.split(" ");
        StringBuilder sb = new StringBuilder();
        
        for (int w = words.length-1; w >= 0; w--) {
            if (!words[w].isEmpty()) {
                sb.append(words[w]);
                
                if (w > 0) {
                    sb.append(" ");
                }
            }
        }
        
        return sb.toString().trim();
    }
}