/*
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
*/
// 8ms. 15th percentile.
import java.util.*;
class Solution {
    public List<Integer> partitionLabels(String S) {
        Map<Character, Integer> starts = new HashMap<Character, Integer>();
        Map<Character, Integer> ends = new HashMap<Character, Integer>();
        
        for (int i = 0; i < S.length(); i++) {
            Character c = S.charAt(i);
            if (!starts.containsKey(c)) {
                starts.put(c, i);
            }
        }
        
        for (int i = S.length()-1; i >= 0; i--) {
            Character c = S.charAt(i);
            if (!ends.containsKey(c)) {
                ends.put(c, i);
            }
        }
        
        List<List<Integer>> characterRanges = new ArrayList<List<Integer>>();
        
        for (Map.Entry<Character, Integer> entry : starts.entrySet()) {
            Character c = entry.getKey();
            List nextEntry = new ArrayList<Integer>();
            nextEntry.add(starts.get(c));
            nextEntry.add(ends.get(c));
            characterRanges.add(nextEntry);            
        }
        
        Comparator<List<Integer>> rangeComparator = new Comparator<List<Integer>>() {
            
            public int compare(List<Integer> a, List<Integer> b) {
                return a.get(0)-b.get(0);
            }
        };
        
        Collections.sort(characterRanges, rangeComparator);
        
        List<Integer> partitionCuttoffs = new ArrayList<Integer>();
        partitionCuttoffs.add(-1);
        int currentPartitionEnd = 0;
        
        for (List<Integer> characterRange : characterRanges) {
            Integer currentCharacterStart = characterRange.get(0);
            Integer currentCharacterEnd = characterRange.get(1);
            if (currentCharacterStart > currentPartitionEnd) {
                partitionCuttoffs.add(currentPartitionEnd);
                currentPartitionEnd = currentCharacterEnd;
            } else {
                currentPartitionEnd = Math.max(currentPartitionEnd, currentCharacterEnd);
            }
        }
        partitionCuttoffs.add(currentPartitionEnd);
        
        List<Integer> partitionSizes = new ArrayList<Integer>();
        for (int i = 0; i < partitionCuttoffs.size()-1; i++) {
            partitionSizes.add(partitionCuttoffs.get(i+1)-partitionCuttoffs.get(i));
        }
        

        return partitionSizes;        
    }
}



// 3ms. 88th percentile
class Solution {
    public List<Integer> partitionLabels(String S) {
        int[] ends = new int[26];
        for (int i = 0; i < S.length(); i++) {
            ends[S.charAt(i)-'a'] = i;
        }
        
        List<Integer> partitionSizes = new ArrayList<Integer>();
        int currentPartitionEnd = 0;
        int currentPartitionStart = 0;
        for (int i = 0; i < S.length(); i++) {
            currentPartitionEnd = Math.max(currentPartitionEnd, ends[S.charAt(i)-'a']);
            
            if (i == currentPartitionEnd) {
                partitionSizes.add(i - currentPartitionStart + 1);
                currentPartitionStart = i + 1;
            }
        }
        return partitionSizes;        
    }
}