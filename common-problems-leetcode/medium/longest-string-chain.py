"""
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter 
anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a 
predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

 

Example 1:

Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".
 

Note:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.
 """
# 144ms. 83 percentile.
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wordToChainLength = {}
        
        for word in words:
            wordToChainLength[word] = 1
            
        longestChain = 0
        for word in sorted(words, key=len):
            for i in range(len(word)):
                chainWord = word[0:i] + word[i+1:]
                if chainWord in wordToChainLength:
                    wordToChainLength[word] = max(wordToChainLength[word], wordToChainLength[chainWord]+1)
            longestChain = max(longestChain, wordToChainLength[word])
                    
        return longestChain




 """
 Notes:

Start a dict that maps words to chain lengths
Iterate through the words starting with the shortest words. Were going to store each word in the dict as a key.
The value will be 1 + the length of the longest chain that leads to it. 
To find the longest chain that leads to it...loop through each of the word's chars. Try removing the char
and see if the resulting word is in the dict. If it is, that's a chain leading to this one. 

Note it's much faster looking from a level of N+1 length words back to the level with N length words than
to do vice versa...allows us to just remove chars to find matches instead of trying to add any of the 26
lowercase chars in each possible spot.

 """