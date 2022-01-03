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


#include <vector>
#include <string>

// 100th percentile
class Solution {
public:
    int expressiveWords(std::string s, std::vector<std::string>& words) {
        int stretchyWordCount = 0;
        for (std::string word : words) {
            int sIndex = 0, wordIndex = 0;
            bool wordIsStretchy = true;
            while (sIndex < s.size() || wordIndex < word.size()) {
                int sCurrentCharCount = sIndex < s.size() ? 1 : 0;
                int wordCurrentCharCount = wordIndex < word.size() ? 1 : 0;
                
                if (wordCurrentCharCount == 0 || sCurrentCharCount == 0) {
                    wordIsStretchy = false;
                    break;
                }
                
                if (s[sIndex] != word[wordIndex]) {
                    wordIsStretchy = false;
                    break;
                }
                
                while (sIndex + 1 < s.size() && s[sIndex] == s[sIndex + 1]) {
                    sCurrentCharCount++;
                    sIndex++;
                }
                while (wordIndex + 1 < word.size() && word[wordIndex] == word[wordIndex + 1]) {
                    wordCurrentCharCount++;
                    wordIndex++;
                }
                
                if (sCurrentCharCount < 3 && sCurrentCharCount != wordCurrentCharCount) {
                    wordIsStretchy = false;
                    break;
                } else if (3 <= sCurrentCharCount && sCurrentCharCount < wordCurrentCharCount) {
                    wordIsStretchy = false;
                    break;
                }
                                
                sIndex++;
                wordIndex++;
                
            }
            
            if (wordIsStretchy)
                stretchyWordCount++;
        }
        
        return stretchyWordCount;
    }
};



// 100th percentile, cleaner
class Solution {
public:
    int expressiveWords(std::string s, std::vector<std::string>& words) {
        int stretchyWordCount = 0;
        for (std::string word : words) {
            int sIndex = 0, wordIndex = 0;
            bool wordIsStretchy = true;
            while (wordIsStretchy && sIndex < s.size() && wordIndex < word.size()) {
                if (s[sIndex] != word[wordIndex]) wordIsStretchy = false;

                int sCurrentCharCount = 1;
                while (sIndex + 1 < s.size() && s[sIndex] == s[sIndex + 1]) {
                    sCurrentCharCount++;
                    sIndex++;
                }

                int wordCurrentCharCount = 1;
                while (wordIndex + 1 < word.size() && word[wordIndex] == word[wordIndex + 1]) {
                    wordCurrentCharCount++;
                    wordIndex++;
                }
                
                if (sCurrentCharCount < 3 && sCurrentCharCount != wordCurrentCharCount) wordIsStretchy = false;
                if (3 <= sCurrentCharCount && sCurrentCharCount < wordCurrentCharCount) wordIsStretchy = false;
                                
                sIndex++;
                wordIndex++;
            }
            
            if (wordIsStretchy && sIndex == s.size() && wordIndex == word.size()) stretchyWordCount++;
        }
        
        return stretchyWordCount;
    }
};



// 100th percentile
// Interesting way of replacing while loop with for loop
class Solution {
public:
    int expressiveWords(std::string s, std::vector<std::string>& words) {
        int numberOfStretchyWords = 0;
        for (auto& word : words) if (check(s, word)) numberOfStretchyWords++;
        return numberOfStretchyWords;
    }
    
    bool check(std::string S, std::string W) {
        int sSlow = 0, wSlow = 0;
        for (int sFast = 0, wFast = 0; sSlow < S.size() && wSlow < W.size(); sSlow = sFast, wSlow = wFast) {
            if (S[sSlow] != W[wSlow]) return false;
            while (sFast < S.size() && S[sFast] == S[sSlow]) sFast++;
            while (wFast < W.size() && W[wFast] == W[wSlow]) wFast++;
            
            int sCurrentCharCount = sFast - sSlow;
            int wCurrentCharCount = wFast - wSlow;
            if (sCurrentCharCount < 3 && sCurrentCharCount != wCurrentCharCount) return false;
            if (3 <= sCurrentCharCount && sCurrentCharCount < wCurrentCharCount) return false;
        }
        return sSlow == S.size() && wSlow == W.size();
    }
};


// Showing the while loop equivalent of above
class Solution {
public:
    int expressiveWords(std::string s, std::vector<std::string>& words) {
        int numberOfStretchyWords = 0;
        for (auto& word : words) if (check(s, word)) numberOfStretchyWords++;
        return numberOfStretchyWords;
    }
    
    bool check(std::string S, std::string W) {
        int sSlow = 0, sFast = 0, wSlow = 0, wFast = 0;
        while (wSlow < W.size() && sSlow < S.size()) {
            if (S[sSlow] != W[wSlow]) return false;
            while (sFast < S.size() && S[sFast] == S[sSlow]) sFast++;
            while (wFast < W.size() && W[wFast] == W[wSlow]) wFast++;
            
            int sCurrentCharCount = sFast - sSlow;
            int wCurrentCharCount = wFast - wSlow;
            if (sCurrentCharCount < 3 && sCurrentCharCount != wCurrentCharCount) return false;
            if (3 <= sCurrentCharCount && sCurrentCharCount < wCurrentCharCount) return false;
            
            wSlow = wFast;
            sSlow = sFast;
        }
        return sSlow == S.size() && wSlow == W.size();
    }
    
    
};


/*
A simple but interesting illustration of for loop / while loop connections...
the for loop has the start, stop, and update conditions in the same line
with while loops you do the start part before the loop, the stop condition in the loop, and then
the update part within the loop...
*/