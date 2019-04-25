/*
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
*/
// 76th percentile
import java.util.Stack;
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) return false;
        String temp = "" + x;
        boolean res = true;
        Stack<Character> s = new Stack<Character>();
        char[] firstHalf = temp.substring(0, temp.length()/2).toCharArray();
        char[] secondHalf = (temp.length() % 2)==1 ? temp.substring(1+ temp.length()/2).toCharArray() : temp.substring(temp.length()/2).toCharArray();
        
        for (char c : firstHalf ) s.push(c);
        for (char c : secondHalf ) {
            
            if (c != s.pop()) {
                res = false;
                break;
            }
        }
        return res;
    }
}

// 84th percentile
// Faster implementations are 5 times as many lines and 1 to 2ms faster
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) return false;
        String xs = "" + x;
        for (int i = 0; i < xs.length()/2; i++) if (xs.charAt(i) != xs.charAt(xs.length()-1-i)) return false;
        return true;
    }
}