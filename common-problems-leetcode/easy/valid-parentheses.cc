/*
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
*/

#include <stack>
#include <string> 

class Solution {
public:
    bool isValid(std::string s) {
        std::stack<char> stack;
        for (const auto& c : s) {
            switch(c) {
                case '{': stack.push('}'); break;
                case '(': stack.push(')'); break;
                case '[': stack.push(']'); break;
                default:
                    if (stack.size() == 0 || c != stack.top()) return false;
                    else stack.pop();
            }
        }
        
        return stack.size() == 0;
    }
};


/*

Notes:

Note the use of const in the for loop to be careful to not change the original chars
Note that in the worst case switches have the same time complexity as if elses. In 
the best case, the compiler can actually provide some optimizations given a switch.

*/