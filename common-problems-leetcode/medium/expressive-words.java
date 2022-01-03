/*
Sometimes people repeat letters to represent extra feeling. For example:

"hello" -> "heeellooo"
"hi" -> "hiiii"
In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
Return the number of query strings that are stretchy.

 

Example 1:

Input: s = "heeellooo", words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
Example 2:

Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
Output: 3
 

Constraints:

1 <= s.length, words.length <= 100
1 <= words[i].length <= 100
s and words[i] consist of lowercase letters.
*/

// 30th percentile
class Solution {
    public int expressiveWords(String s, String[] words) {
        int numberOfStretchyWords = 0;
        for (String word : words) {
            boolean wordIsStretchy = true;
            int sIndex = 0, wordIndex = 0;
            while (wordIsStretchy && sIndex < s.length() && wordIndex < word.length()) {
                if (s.charAt(sIndex) != word.charAt(wordIndex)) wordIsStretchy = false;
                
                int sCurrentCharCount = 1; 
                while (sIndex + 1 < s.length() && s.charAt(sIndex) == s.charAt(sIndex + 1)) {
                    sCurrentCharCount++;
                    sIndex++;
                }
                
                int wordCurrentCharCount = 1;
                while (wordIndex + 1 < word.length() && word.charAt(wordIndex) == word.charAt(wordIndex + 1)) {
                    wordCurrentCharCount++;
                    wordIndex++;
                }
                
                if (sCurrentCharCount < 3 && sCurrentCharCount != wordCurrentCharCount) wordIsStretchy = false;
                if (3 <= sCurrentCharCount && sCurrentCharCount < wordCurrentCharCount) wordIsStretchy = false;
                
                sIndex++;
                wordIndex++;
            }
            
            if (wordIsStretchy && sIndex == s.length() && wordIndex == word.length()) numberOfStretchyWords++;
        }
        
        return numberOfStretchyWords;
    }
}


// 30th percentile
// Interesting way of replacing while loops with for loop
class Solution {
    public int expressiveWords(String s, String[] words) {
        int numberOfStretchyWords = 0;
        for (String word : words) if ( this.check(s, word) ) numberOfStretchyWords++;
        return numberOfStretchyWords;
    }
    
    public boolean check(String s, String w) {
        int sSlow = 0, wSlow = 0;
        for (int sFast = 0, wFast = 0; sSlow < s.length() && wSlow < w.length(); sSlow = sFast, wSlow = wFast) {
            if (s.charAt(sSlow) != w.charAt(wSlow)) return false;
            while (sFast < s.length() && s.charAt(sFast) == s.charAt(sSlow)) sFast++;
            while (wFast < w.length() && w.charAt(wFast) == w.charAt(wSlow)) wFast++;
            
            int sCurrentCharCount = sFast - sSlow;
            int wCurrentCharCount = wFast - wSlow;
            if (sCurrentCharCount < 3 && sCurrentCharCount != wCurrentCharCount) return false;
            if (3 <= sCurrentCharCount && sCurrentCharCount < wCurrentCharCount) return false;
        }
        
        return sSlow == s.length() && wSlow == w.length();
    }
}


// 30th percentile
// while loop equivalent of above
class Solution {
    public int expressiveWords(String s, String[] words) {
        int numberOfStretchyWords = 0;
        for (String word : words) if ( this.check(s, word) ) numberOfStretchyWords++;
        return numberOfStretchyWords;
    }
    
    public boolean check(String s, String w) {
        int sSlow = 0, sFast = 0, wSlow = 0, wFast = 0;
        while (sSlow < s.length() && wSlow < w.length())
        {
            if (s.charAt(sSlow) != w.charAt(wSlow)) return false;
            while (sFast < s.length() && s.charAt(sFast) == s.charAt(sSlow)) sFast++;
            while (wFast < w.length() && w.charAt(wFast) == w.charAt(wSlow)) wFast++;
            
            int sCurrentCharCount = sFast - sSlow;
            int wCurrentCharCount = wFast - wSlow;
            if (sCurrentCharCount < 3 && sCurrentCharCount != wCurrentCharCount) return false;
            if (3 <= sCurrentCharCount && sCurrentCharCount < wCurrentCharCount) return false;
            
            sSlow = sFast;
            wSlow = wFast;
        }
        
        return sSlow == s.length() && wSlow == w.length();
    }
}




/*
A simple but interesting illustration of for loop / while loop connections...
the for loop has the start, stop, and update conditions in the same line
with while loops you do the start part before the loop, the stop condition in the loop, and then
the update part within the loop...
*/