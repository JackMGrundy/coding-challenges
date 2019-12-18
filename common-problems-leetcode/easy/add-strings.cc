/*
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
*/

// 8ms. 64th percentile.
#include <string>
#include <bits/stdc++.h> 

class Solution {
public:
std::string addStrings(std::string num1, std::string num2) {
    int i = num1.size() - 1;
    int j = num2.size() - 1;
    int carry = 0;
    std::string result = "";

    while (0 <= i || 0 <= j || carry != 0) {
        long sum = 0;
        if (0 <= i) {
            sum += (num1[i] - '0');
            i--;
        }

        if (0 <= j) {
            sum += (num2[j] - '0');
            j--;
        }

        sum += carry;
        carry = sum / 10;
        sum = sum % 10;
        result = result + std::to_string(sum);
    }

    reverse(result.begin(), result.end());
    return result;
}
};