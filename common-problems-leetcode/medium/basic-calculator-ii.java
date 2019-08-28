/*
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
*/

// 13ms. 81 percentile.
import java.util.*;
class Solution {
    public int calculate(String s) {
        Stack<Integer> stack = new Stack<Integer>();
        int num = 0;
        char lastOp = '!';
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if ('0' <= c && c <= '9') {
                num = num*10 + (c-'0');
            }
            
            if ("+-*/".indexOf(c) != -1 || i == s.length()-1) {
                if (lastOp == '!') {
                    stack.push(num);
                }
                else if (lastOp == '+') {
                    stack.push(num);
                }
                else if (lastOp == '-') {
                    stack.push(-num);
                }
                else if (lastOp == '*') {
                    stack.push(stack.pop() * num);
                }
                else if (lastOp == '/') {
                    if (stack.peek() < 0) {
                        stack.push( (int) Math.ceil(stack.pop() / ( (float) num)) );
                    } else {
                        stack.push( (int) Math.floor(stack.pop() / ( (float) num)) );
                    }
                }
                lastOp = c;
                num = 0;
            }
        }
        
        int sum = 0;
        for (Integer n : stack) {
            sum += n;
        }
        return sum;
    }
}
