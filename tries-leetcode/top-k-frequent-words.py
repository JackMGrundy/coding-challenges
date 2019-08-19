"""
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
"""

# Built ins...technicall nlogn
# 64ms. 77th percentile
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words).most_common(len(words))
        counts.sort(key=lambda x: (-x[1], x[0]))
        return [ x[0] for x in counts[0:k] ]

""" 
To do better than n log n you can:
1) Count the frequencies and put them into a heap. Then get the max element k times. 
2) Count the frequencies. Then use quick select to get the k best. 
3) Most involved but best method space and memory wise...use a trie to count the number
of times each word appears. Then use a heap to get k best...way too involved imo
unless the use case really calls for it...
"""