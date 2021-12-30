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



// 14th percentile
class Solution {
    public String originalDigits(String s) {
        HashMap<Character, Integer> sCharCounts = new HashMap<Character, Integer>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            sCharCounts.put(c, sCharCounts.getOrDefault(c, 0) + 1);
        }

        int[] answerDigitCounts = new int[10];
        
        // z only in zero
        answerDigitCounts[0] = sCharCounts.getOrDefault('z', 0);
        // w only in two
        answerDigitCounts[2] = sCharCounts.getOrDefault('w', 0);
        // u only in four
        answerDigitCounts[4] = sCharCounts.getOrDefault('u', 0);
        // x only in six
        answerDigitCounts[6] = sCharCounts.getOrDefault('x', 0);
        // g only in eight
        answerDigitCounts[8] = sCharCounts.getOrDefault('g', 0);
        // h only in eight and three
        answerDigitCounts[3] = sCharCounts.getOrDefault('h', 0) - answerDigitCounts[8];
        // f only in four and five
        answerDigitCounts[5] = sCharCounts.getOrDefault('f', 0) - answerDigitCounts[4];
        // s only in six and seven
        answerDigitCounts[7] = sCharCounts.getOrDefault('s', 0) - answerDigitCounts[6];
        // i only in five, size, eight, and nine
        answerDigitCounts[9] = sCharCounts.getOrDefault('i', 0) - answerDigitCounts[5] - answerDigitCounts[6] - answerDigitCounts[8];
        // o only in zero, two, four, and one
        answerDigitCounts[1] = sCharCounts.getOrDefault('o', 0) - answerDigitCounts[0] - answerDigitCounts[2] - answerDigitCounts[4];
        
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < answerDigitCounts[i]; j++) {
                sb.append(i);
            }
        }
        
        return sb.toString();
        
    }
}





// 75th percentile
class Solution {
    public String originalDigits(String s) {
        
        char[] sCharCounts = new char[26 + (int)'a'];
        for (char ch : s.toCharArray()) {
            sCharCounts[ch]++;
        }
        
        int[] answerDigitCounts = new int[10];
        
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
        
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < answerDigitCounts[i]; j++) {
                sb.append(i);
            }
        }
        
        return sb.toString();
        
    }
}




// 99th percentile
class Solution {
    public String originalDigits(String s) {
        int numLettersLeft = s.length();
        if (numLettersLeft == 0) return "";
        
        char[] sCharCounts = new char[26 + (int)'a'];
        for (char ch : s.toCharArray()) {
            sCharCounts[ch]++;
        }
        
        int[] answerDigitCounts = new int[10];
        
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
        
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < answerDigitCounts[i]; j++) {
                sb.append(i);
            }
        }
        
        return sb.toString();
        
    }
}