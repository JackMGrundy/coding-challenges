/*
Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.

 

Example 1:

Input: s = "owoztneoer"
Output: "012"
Example 2:

Input: s = "fviefuro"
Output: "45"
 

Constraints:

1 <= s.length <= 105
s[i] is one of the characters ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"].
s is guaranteed to be valid.
*/





// 48th percentile
#include <string>
#include <vector>
#include <unordered_map>


class Solution {
public:
    std::string originalDigits(std::string s) {
        std::unordered_map<char, int> sCharCounts;
        
        for (auto& c : s) {
            sCharCounts[c]++;
        }
    
        std::vector<int> answerDigitCounts(10,0);
        
        // z only in zero
        answerDigitCounts[0] = sCharCounts['z'];
        // w only in two
        answerDigitCounts[2] = sCharCounts['w'];
        // u only in four
        answerDigitCounts[4] = sCharCounts['u'];
        // x only in six
        answerDigitCounts[6] = sCharCounts['x'];
        // g only in eight
        answerDigitCounts[8] = sCharCounts['g'];
        // h only in eight and three
        answerDigitCounts[3] = sCharCounts['h'] - answerDigitCounts[8];
        // f only in four and five
        answerDigitCounts[5] = sCharCounts['f'] - answerDigitCounts[4];
        // s only in six and seven
        answerDigitCounts[7] = sCharCounts['s'] - answerDigitCounts[6];
        // i only in five, size, eight, and nine
        answerDigitCounts[9] = sCharCounts['i'] - answerDigitCounts[5] - answerDigitCounts[6] - answerDigitCounts[8];
        // o only in zero, two, four, and one
        answerDigitCounts[1] = sCharCounts['o'] - answerDigitCounts[0] - answerDigitCounts[2] - answerDigitCounts[4];
        
        
        std::string answer = "";
        for (int i = 0; i < answerDigitCounts.size(); i++) 
            for (int j = 0; j < answerDigitCounts[i]; j++) 
                answer += std::to_string(i);
        
        return answer;
    }
};