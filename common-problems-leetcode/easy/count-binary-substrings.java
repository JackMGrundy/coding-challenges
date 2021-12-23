/*
Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

 

Example 1:

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:

Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
 

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
*/

// First attempt 92nd percentile
class Solution {
    public int countBinarySubstrings(String s) {
        int prevGroup=0, curGroup=1, numberOfMatches=0;
        
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) != s.charAt(i - 1)) {
                numberOfMatches += Math.min(prevGroup, curGroup);
                prevGroup = curGroup;
                curGroup = 1;
            } else {
                curGroup += 1;
            }
        }
        
        return numberOfMatches + Math.min(prevGroup, curGroup);
    }
}


/*
Notes:
The more obvious solution is to calculate all the group sizes and then get
the mins of each adjacent pair...
    to see this just note that for example two adjacent groups of 3
    -> 3 matches

However, this requires two passes to get the group sizes and then calculate
the total number of mathces...

using the solution above we can do one pass by just keeping track of the current
and previous group sizes...


Good place to note a bit about java chars and strings...
You can speed up the above by converting the string to a char array...

https://www.geeksforgeeks.org/difference-between-string-and-character-array-in-java/
https://www.geeksforgeeks.org/string-constant-pool-in-java/
^this stuff
*/