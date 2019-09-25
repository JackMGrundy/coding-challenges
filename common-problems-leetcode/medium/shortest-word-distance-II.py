"""
Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters. 

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""
# 112ms. 65 percentile.
class WordDistance:

    def __init__(self, words: List[str]):
        self.locations = collections.defaultdict(list)
        for i,word in enumerate(words):
            self.locations[word].append(i)
        
    def shortest(self, word1: str, word2: str) -> int:
        w1Locs = self.locations[word1]
        w2Locs = self.locations[word2]
        
        l1, l2 = 0, 0
        minDist = float("inf")
        while l1 < len(w1Locs) and l2 < len(w2Locs):
            minDist = min(minDist, abs(w1Locs[l1] - w2Locs[l2]))
            if w1Locs[l1] <= w2Locs[l2]:
                l1 += 1
            else:
                l2 += 1
        
        return minDist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)


"""
Notes:


"""