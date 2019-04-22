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
import java.util.Arrays;

// I think this is good...but LeetCode is having internal server errors...can't check
class Solution {
    public String addBoldTag(String s, String[] dict) {
        if (s.length()==0 || dict.length == 0) return "";
        
        boolean[] bolded = new boolean[s.length()];
        
        // Identify characters to be bolded
        for (int i = 0; i < dict.length; i++) {
            String nxtTag = dict[i];
            int start = s.indexOf(nxtTag);
            while (start != -1) {
                Arrays.fill(bolded, start, start+nxtTag.length(), true);
                start = s.indexOf(nxtTag, start+1);
            }
        }
        
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (!bolded[i]) {
                result.append(s.charAt(i));
                continue;
            }
            int j = i;
            while (j < s.length() && bolded[j]) j++;
            result.append("<b>" + s.substring(i, j) + "</b>");
            i = j - 1;
        }
        
        return result.toString();
    }
}