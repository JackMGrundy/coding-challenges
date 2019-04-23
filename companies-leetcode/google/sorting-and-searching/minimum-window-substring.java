/*
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
*/
// 49th percentile
class Solution {
    public String minWindow(String s, String t) {
        if (s.length()==0 || t.length()==0) {
            return "";
        }
        
        // Count up chars in t
        HashMap<String, Integer> counts = new HashMap();
        HashSet<String> chars = new HashSet();
        for (int i = 0; i < t.length(); i++) {
            String c = Character.toString(t.charAt(i));
            chars.add(c);
            if (!counts.containsKey(c) ) {
                counts.put(c, 1);
            }
            else {
                counts.put(c, counts.get(c)+1);
            }
        }
        
        int tail = 0;
        String res = "";
        int maxLength = Integer.MAX_VALUE;
        int missing = t.length();
        
        for (int head = 0; head < s.length(); head++) {
            String c = Character.toString(s.charAt(head));
            
            // Hit a char in t
            if (chars.contains(c)) {
                if (counts.get(c) > 0) {
                    missing--;
                }
                counts.put(c, counts.get(c)-1);
            }
            // Have hit all chars in t
            while (missing == 0) {
                //Check for new best answer
                
                if (head - tail + 1 < maxLength) {
                    maxLength = head - tail + 1;
                    res = s.substring(tail, head+1);
                }
                
                //Advance tail
                String tc = Character.toString(s.charAt(tail));
                if (chars.contains(tc)) {
                    if (counts.get(tc)==0) {
                        missing++;
                    }
                    counts.put(tc, counts.get(tc)+1);
                }
                
                tail += 1;
            }
        }
        
        return res;
    }
}


// 70th percentile
// Use int array of chars instead of HashMap
class Solution {
    public String minWindow(String s, String t) {
        if (s.length()==0 || t.length()==0) {
            return "";
        }
        
        int[] counts = new int[256];
        HashSet<Character> chars = new HashSet();
        for (int i = 0; i < t.length(); i++) {
            Character c = t.charAt(i);
            chars.add(c);
            counts[c]++;
        }
        
        int tail = 0;
        String res = "";
        int maxLength = Integer.MAX_VALUE;
        int missing = t.length();
        
        for (int head = 0; head < s.length(); head++) {
            Character c = s.charAt(head);
            
            // Hit a char in t
            if (chars.contains(c)) {
                if (counts[c] > 0) {
                    missing--;
                }
                counts[c]--;
            }
            // Have hit all chars in t
            while (missing == 0) {
                //Check for new best answer
                
                if (head - tail + 1 < maxLength) {
                    maxLength = head - tail + 1;
                    res = s.substring(tail, head+1);
                }
                
                //Advance tail
                Character tc = s.charAt(tail);
                if (chars.contains(tc)) {
                    if (counts[tc]==0) {
                        missing++;
                    }
                    counts[tc]++;
                }
                
                tail += 1;
            }
        }
        
        return res;
    }
}


// 75th percentile
// Extend trick to get rid of HashSet
class Solution {
    public String minWindow(String s, String t) {
        if (s.length()==0 || t.length()==0) {
            return "";
        }
        
        int[] counts = new int[256];
        int[] chars = new int[256];
        for (int i = 0; i < t.length(); i++) {
            Character c = t.charAt(i);
            chars[c]++;
            counts[c]++;
        }
        
        int tail = 0;
        String res = "";
        int maxLength = Integer.MAX_VALUE;
        int missing = t.length();
        
        for (int head = 0; head < s.length(); head++) {
            Character c = s.charAt(head);
            
            // Hit a char in t
            if (chars[c]>0) {
                if (counts[c] > 0) {
                    missing--;
                }
                counts[c]--;
            }
            // Have hit all chars in t
            while (missing == 0) {
                //Check for new best answer
                
                if (head - tail + 1 < maxLength) {
                    maxLength = head - tail + 1;
                    res = s.substring(tail, head+1);
                }
                
                //Advance tail
                Character tc = s.charAt(tail);
                if (chars[tc]>0) {
                    if (counts[tc]==0) {
                        missing++;
                    }
                    counts[tc]++;
                }
                
                tail += 1;
            }
        }
        
        return res;
    }
}



// 84th percentile
// Use of ++ in ifs - note that ++ is evaluated after the comparisons
class Solution {
    public String minWindow(String s, String t) {
        if (t.length() > s.length()) {
            return "";
        }
        
        int[] counts = new int[128];
        int[] chars = new int[128];
        for (int i = 0; i < t.length(); i++) {
            Character c = t.charAt(i);
            chars[c]++;
            counts[c]++;
        }
        
        int tail = 0;
        String res = "";
        int maxLength = Integer.MAX_VALUE;
        int missing = t.length();
        
        for (int head = 0; head < s.length(); head++) {
            Character c = s.charAt(head);
            
            // Hit a char in t
            if (chars[c]>0) {
                if (counts[c]-- > 0) {
                    missing--;
                }
            }
            // Have hit all chars in t
            while (missing == 0) {
                //Check for new best answer
                
                if (head - tail + 1 < maxLength) {
                    maxLength = head - tail + 1;
                    res = s.substring(tail, head+1);
                }
                
                //Advance tail
                Character tc = s.charAt(tail);
                if (chars[tc]>0) {
                    if (counts[tc]++ ==0) {
                        missing++;
                    }
                }
                
                tail += 1;
            }
        }
        
        return res;
    }
}