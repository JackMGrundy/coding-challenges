/*
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
Accepted
231,974
Submissions
279,564
*/
// 83rd percentile
import java.util.Set;
import java.util.HashSet;
class Solution {
    public int numJewelsInStones(String J, String S) {
        Set jewels = new HashSet();
        for (int i = 0; i < J.length(); i++) {
            jewels.add(J.charAt(i));
        }
        int res = 0;
        for (int i = 0; i < S.length(); i++) {
            if (jewels.contains(S.charAt(i))) res++;
        }
        return res;
    }
}



// 99th percentile
class Solution {
    public int numJewelsInStones(String J, String S) {
        Set jewels = new HashSet();
        int res = 0;
        for (char c : J.toCharArray() ) jewels.add(c);
        for (char c : S.toCharArray()) if (jewels.contains(c)) res++;
        return res;
    }
}