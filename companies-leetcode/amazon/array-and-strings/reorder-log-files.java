/*abstractYou have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 

Example 1:

Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
 

Note:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.
*/

// 1st attempt: 2ms. 99th percentile.
class Solution {
    public String[] reorderLogFiles(String[] logs) {
        Comparator<String> logComparator = new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                int s1WordsIndex = s1.indexOf(" ");
                int s2WordsIndex = s2.indexOf(" ");
                char s1TestChar = s1.charAt(s1WordsIndex+1);
                char s2TestChar = s2.charAt(s2WordsIndex+1);
                
                if (s1TestChar <= '9' && s2TestChar > '9') {
                    return 1;
                }
                if (s1TestChar > '9' && s2TestChar <= '9') {
                    return -1;
                }
                if (s1TestChar <= '9' && s2TestChar <= '9') {
                    return 0;
                }
                
                // both logs are letterLogs
                int compareWords = s1.substring(s1WordsIndex+1).compareTo(s2.substring(s2WordsIndex+1));
                if (compareWords != 0) {
                    return compareWords;
                }
                
                int compareIds = s1.substring(0, s1WordsIndex).compareTo(s2.substring(0, s2WordsIndex));
                return compareIds;
            }
        };
    
        Arrays.sort(logs, logComparator);
        return logs;
    }
}