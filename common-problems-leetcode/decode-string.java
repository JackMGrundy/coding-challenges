/*
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
Accepted
97.9K
Submissions
219.9K
*/
// 52nd percentile. 2ms.
// Not super clean...but out of time to improve this...
import java.util.List; 
import java.util.ArrayList; 
import java.util.ArrayDeque; 
import java.util.Collections;
import java.util.Deque;
class Solution {
    public String decodeString(String s) {
        Deque<Character> stack = new ArrayDeque<Character>();
        List<Character> res = new ArrayList<Character>();
        int opens = 0;
        
        for (int j = 0; j < s.length(); j++) {
            char c = s.charAt(j);
            
            if (c == '[') {
                opens++;
            } else if (c == ']') {
                opens--;
                
                // Get string portion of group
                char cur = stack.pollLast();
                ArrayList<Character> temp = new ArrayList<Character>();
                
                while (cur != '[') {
                    temp.add(cur);
                    cur = stack.pollLast();
                }
                
                Collections.reverse(temp);
                
                // Get multiplier for group
                char d = stack.pollLast();
                StringBuilder k = new StringBuilder();
                while (stack.size() > 0 && Character.isDigit(d)) {
                    k.append(d);
                    d = stack.pollLast();
                }
                
                if (Character.isDigit(d)) {
                    k.append(d);
                } else {
                    stack.offer(d);
                }
                
                k.reverse();
                int multiplier = Integer.parseInt(k.toString());
                for (int i = 0; i < multiplier; i++) {
                    stack.addAll(temp);
                }

                // Add group to res if not inside a group
                if (opens == 0) {
                    res.addAll(stack);
                    stack.clear();
                } 
                continue;
            }
            stack.offer(c);
        }
        
        res.addAll(stack);
        StringBuilder answer = new StringBuilder();
        for (char c : res) {
            answer.append(c);
        }
        return answer.toString();
    }
}