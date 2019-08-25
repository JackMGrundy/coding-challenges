/*
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
*/

// 5ms. 75th percentile
class Solution {
    public List<String> commonChars(String[] A) {
        List<String> res = new ArrayList<String>();
        if (A.length == 0) {
            return res;
        }
        
        int[] finalCharCounts = new int[26];
        
        for (char c : A[0].toCharArray()) {
            finalCharCounts[c-'a']++;
        }
        
        for (int i = 1; i < A.length; i++) {
            int[] currentCharCounts = new int[26];
            for (char c : A[i].toCharArray()) {
                currentCharCounts[c-'a']++;
            }
            
            for (int j = 0; j < 26; j++) {
                finalCharCounts[j] = Math.min(finalCharCounts[j], currentCharCounts[j]);
            }
        }
        
        for (int i = 0; i < 26; i++) {
            if (finalCharCounts[i] > 0) {
                for (int j = 0; j < finalCharCounts[i]; j++) {
                    res.add( Character.toString((char)(i+'a')) );
                }
            }
        }
        return res;
    }
}