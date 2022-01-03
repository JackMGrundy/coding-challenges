/*
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter.
*/

#include <string>
#include <unordered_set>
#include <stack>

// 15th percentile
class Solution {
public:
    std::string minRemoveToMakeValid(std::string s) {
        std::stack<int> st;
        std::unordered_set<int> charsToRemove;
        
        for (int i = 0; i < s.length(); i++) {
            char c = s[i];
            if (c == '(') {
                st.push(i);
            } else if (c == ')') {
                if (st.size() == 0) {
                    charsToRemove.insert(i);
                } else {
                    st.pop();
                }
            }
        }
        
        while (0 < st.size()) {
            int charToRemove = st.top();
            st.pop();
            charsToRemove.insert(charToRemove);
        }
        
        std::string answer = "";
        for (int i = 0; i < s.length(); i++) {
            if (charsToRemove.find(i) == charsToRemove.end()) {
                answer += s[i];
            }
        }
        
        return answer;
    }
};


// 98th percentile
class Solution {
public:
    std::string minRemoveToMakeValid(std::string s) {
        std::stack<int> st;
        
        for (int i = 0; i < s.length(); i++) {
            char c = s[i];
            if (c == '(') {
                st.push(i);
            } else if (c == ')') {
                if (st.size() == 0) {
                    s[i] = '*';
                } else {
                    st.pop();
                }
            }
        }
        
        while (0 < st.size()) {
            int charToRemove = st.top();
            st.pop();
            s[charToRemove] = '*';
        }
        
        s.erase(std::remove(s.begin(), s.end(), '*'), s.end());
        return s;
    }
};




// with remove_if....98th percentile
class Solution {
public:
    std::string minRemoveToMakeValid(std::string s) {
        std::stack<int> st;
        
        for (int i = 0; i < s.length(); i++) {
            char c = s[i];
            if (c == '(') {
                st.push(i);
            } else if (c == ')') {
                if (st.size() == 0) {
                    s[i] = '*';
                } else {
                    st.pop();
                }
            }
        }
        
        while (0 < st.size()) {
            int charToRemove = st.top();
            st.pop();
            s[charToRemove] = '*';
        }
        
        s.erase(std::remove_if(s.begin(), s.end(), [](char c) { return c == '*'; }), s.end());
        return s;
    }
};



/*
Second bit is an example of c++ erase-remove idiom
https://en.wikipedia.org/wiki/Erase%E2%80%93remove_idiom

the remove bit basically compacts the elements that do not match * to the start...the std::remove returns an iterator that 
points to the first element that is *...and then erase deletes from that to the old end




https://www.quora.com/What-are-the-differences-between-remove-and-remove_if-in-STL
Can use remove_if for a more general criteria:

For std::remove, we supply a value, and all the elements that compare equal to the value are removed (returns an iterator to new end of the range).

For std::remove_if, we supply a predicate, and all the elements for which predicate returns true are removed (returns an iterator to new end of the range).

NOTE : Neither of std::remove or std::remove_if alters the size of the object i.e. they do not actually erase the elements from the object because it is a non member function. The removal is done by replacing the elements (to be removed) by the next element (not to be removed), and signaling the new size of the shortened range by returning an iterator to the element that should be considered its new past-the-end element.

Example :
[1] Erase 5

std::vector<int> v {1, 2, 3, 4, 6, 5, 5, 10, 5}; 
v.erase(std::remove(v.begin(), v.end(), 5), v.end()); 
for (auto i : v) 
    std::cout << i << '  ';  // 1  2  3  4  6  10  

[2] Erase even elements

bool is_even(int i) { return !(i & 1); } 
 
std::vector<int> v {1, 2, 3, 4, 6, 5, 5, 10, 5}; 
v.erase(std::remove_if(v.begin(), v.end(), is_even), v.end()); 
for (auto i : v) 
    std::cout << i << '  ';  // 1  3  5  5  5 

[3] Erase odd elements

std::vector<int> v {1, 2, 3, 4, 6, 5, 5, 10, 5}; 
v.erase(std::remove_if(v.begin(), v.end(), [](int i){ return i & 1; }), v.end()); 
for (auto i : v) 
    std::cout << i << '  ';  // 2  4  6  10  


*/