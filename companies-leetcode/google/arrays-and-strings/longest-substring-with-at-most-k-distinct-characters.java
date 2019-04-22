/*
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
*/
import java.util.HashMap;
import java.util.Collections;
import java.util.Map;

// 41st percentile
class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        int res = 0;
        int start = 0;
        int max = 0;
        Map<Character, Integer> data = new HashMap<Character, Integer>();
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            data.put(c, i);
            
            if (data.size() > k) {
                int min = Collections.min(data.values());
                char removeChar = s.charAt(min);
                data.remove(removeChar);
                start = min+1;
            }
            
            max = Math.max(max, i-start+1);
        }
        
        return max;
    }
}

// 64th percentile
class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        int res = 0;
        int start = 0;
        int max = 0;
        Map<Character, Integer> data = new HashMap<Character, Integer>();
        
        for (int i = 0; i < s.length(); i++) {
            data.put(s.charAt(i), i);
            
            if (data.size() > k) {
                
                int rm_idx = s.length();
                char rm_c = ' ';
                for(Character c: data.keySet()){
                    if(rm_idx > data.get(c)){
                        rm_idx = data.get(c);
                        rm_c = c;
                    }
                }
                
                data.remove(rm_c);
                start = rm_idx+1;
            }
            
            max = Math.max(max, i-start+1);
        }
        
        return max;
    }
}


// 99th percentile
class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        char[] cs = s.toCharArray();
        int[] counts = new int[256];
        int numSeen = 0;
        int res = 0;
        
        for (int l = 0, r = 0; r < s.length(); r++) {
            counts[cs[r]]++;
            if (counts[cs[r]]==1) {
                numSeen++;
            }
            while (numSeen > k) {
                counts[cs[l]]--;
                if (counts[cs[l]]==0) {
                    numSeen--;
                }
                l++;
            }
            res = Math.max(res, r-l+1);
        }
        
        return res;
}
}