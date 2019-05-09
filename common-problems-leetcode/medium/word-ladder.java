/*
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
Accepted
249.3K
Submissions
1.1M
*/
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;
import java.util.Map;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.HashMap;
// 90th percentile. 39ms.
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        
        if (wordList.size() == 0 || beginWord.length()==0 || endWord.length()==0 || wordList.indexOf(endWord) == -1) {
            return 0;
        }
        
        // dictionary of intermediate states
        Map<String, List<String>> interStates = new HashMap<String, List<String>>();
        final int L = beginWord.length();
        for (String word : wordList) {
            for (int i = 0; i < L; i++) {
                String key = word.substring(0, i) + "*" + word.substring(i+1, L);
                if (!interStates.containsKey(key)) {
                    interStates.put(key, new ArrayList<String>());
                }
                List temp = interStates.get(key);
                temp.add(word);
            } 
        }
        
        Entry start = new Entry(beginWord, 1);
        Queue<Entry> q = new LinkedList<Entry>();
        q.add(start);
        Set<String> visited = new HashSet<String>();
        visited.add(beginWord);
        
        // bfs
        while (q.size() > 0) {
            Entry cur = q.remove();
            String curWord = cur.word;
            int d = cur.d;
            
            for (int i = 0; i < L; i++) {
                String intWord = curWord.substring(0, i) + "*" + curWord.substring(i+1, L);
                List<String> intWords = interStates.get(intWord);
                if (intWords == null) continue;
                for (int w = 0; w < intWords.size(); w++) {
                    String nxtWord = intWords.get(w);
                    if (visited.contains(nxtWord)) continue;
                    if (nxtWord.equals(endWord)) return d+1;
                    visited.add(nxtWord);
                    Entry temp = new Entry(nxtWord, d+1);
                    q.add(temp);
                }
            }
        }
        return 0;
    }
}

class Entry {
    public String word;
    public int d;
    
    public Entry(String word, int d) {
        this.word = word;
        this.d = d;
    }
    
    public String toString() {
        return "(" + word + ", " + d + ")";
    }
}