/*
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
*/
// 6ms. 96th percentile.
// technically n log n. using built ins.
import java.util.*;
class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> counts = new HashMap<String, Integer>();
        for (String word : words) {
            counts.put(word, counts.getOrDefault(word, 0)+1);
        }
        
        Comparator<String> wordCountsComparator = new Comparator<String>() {
            
            public int compare(String a, String b) {
                if (counts.get(a) != counts.get(b)) {
                    return counts.get(b) - counts.get(a);
                } else {
                    return a.compareTo(b);
                }
            }
        };
        
        Set<String> uniqueWords = counts.keySet();
        List<String> kMostFrequentWords = new ArrayList<String>(uniqueWords);
        
        Collections.sort(kMostFrequentWords, wordCountsComparator);
        
        return kMostFrequentWords.subList(0, k);
    }
}



// 6ms. 96th percentile.
// nlogk using heap
import java.util.*;
class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> counts = new HashMap<String, Integer>();
        for (String word : words) {
            counts.put(word, counts.getOrDefault(word, 0)+1);
        }
        
        Comparator<String> wordCountsComparator = new Comparator<String>() {
            public int compare(String a, String b) {
                if (counts.get(a) != counts.get(b)) {
                    return counts.get(b) - counts.get(a);
                } else {
                    return a.compareTo(b);
                }
            }
        };
        
        PriorityQueue<String> pq = new PriorityQueue<String>(wordCountsComparator);
        List<String> kMostFrequentWords = new ArrayList<String>();
        
        for (Map.Entry<String, Integer> entry : counts.entrySet()) {
            pq.offer(entry.getKey());
        }
        for (int i = 0; i < k; i++) {
            kMostFrequentWords.add(pq.poll());
        }
        
        return kMostFrequentWords;
    }
}