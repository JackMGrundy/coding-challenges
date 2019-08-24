"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Note:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are english lowercase letters.
"""
# 40ms. 85th percentile.
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordering = {}
        for i, c in enumerate(list(order)):
            ordering[c] = i

        for i in range(len(words)-1):
            minLength = min(len(words[i]), len(words[i+1]))
            
            for j in range(minLength):
                word1Char = ordering[words[i][j]]
                word2Char = ordering[words[i+1][j]]
                completelyMatch = True
                if (word1Char < word2Char):
                    completelyMatch = False
                    break
                elif (word1Char > word2Char):
                    return False
                elif (word1Char == word2Char):
                    continue
            
            if completelyMatch and len(words[i]) > len(words[i+1]):
                return False
        
        return True
                