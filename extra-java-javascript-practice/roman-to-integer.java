/* 
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
*/
// 74th percentile in speed
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int romanToInt(String s) {
        int res = 0;
        Map<Character, Integer> transl = new HashMap<Character, Integer>();
        transl.put('I', 1);
        transl.put('V', 5);
        transl.put('X', 10);
        transl.put('L', 50);
        transl.put('C', 100);
        transl.put('D', 500);
        transl.put('M', 1000);
        
        Map<String, Integer> pairs = new HashMap<String, Integer>();
        pairs.put("IV", 4);
        pairs.put("IX", 9);
        pairs.put("XL", 40);
        pairs.put("XC", 90);
        pairs.put("CD", 400);
        pairs.put("CM", 900);
        
        
        char[] cs = s.toCharArray();
        for (int i = 0; i < cs.length; i++) {
            if (i < cs.length-1 && pairs.containsKey("" + cs[i] + cs[i+1])) {
                res += pairs.get("" + cs[i] + cs[i+1]);
                i++;
            } else {
                res += transl.get(cs[i]);
            }
        }
        return res;
    }
}