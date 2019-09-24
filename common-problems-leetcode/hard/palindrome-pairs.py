"""
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]
"""

# 392. 97th percentile.
# Brute force.
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        reversedWords = { w[::-1]:i for i,w in enumerate(words) }
        validPairs = []
        
        for wordIndex, word in enumerate(words):
            for charIndex in range(len(word) + 1):
                prefix, suffix = word[:charIndex], word[charIndex:]
                
                if prefix in reversedWords and reversedWords[prefix] != wordIndex and suffix==suffix[::-1]:
                    validPairs.append([wordIndex, reversedWords[prefix]])
                
                if 0 < charIndex and suffix in reversedWords and reversedWords[suffix] != wordIndex and prefix==prefix[::-1]:
                    validPairs.append([reversedWords[suffix], wordIndex])
        
        return validPairs



"""
828ms. 32nd percentile.
This is the asymptotically better solution, but it's a lot more complicated.
Also, my implementation could def be optimized. 
"""
class Solution:
    
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = self._createTrie(words)
        palindromePairs = []
        
        for wordIndex, word in enumerate(words):
            root = trie
            
            # Dealing with blanks
            if root["words"] and wordIndex != root["words"][0] and self._isPalindrome(word):
                palindromePairs.append([wordIndex, root["words"][0]])
                palindromePairs.append([root["words"][0], wordIndex])
            
            # Searching for Palindrome pairs AB where word is A
            for charIndex, c in enumerate(word):
                if c in root:
                    root = root[c]
                    
                    # A is longer than B
                    for pair in root["words"]:
                        if pair != wordIndex and self._isPalindrome(word[charIndex+1:]):
                            palindromePairs.append([wordIndex, pair])
                    
                    # B is longer than A
                    if charIndex == len(word) - 1:
                        for pair in root["palindromeSuffixes"]:
                            if pair != wordIndex:
                                palindromePairs.append([wordIndex, pair])
                else:
                    break
        return palindromePairs
        
    def _createTrie(self, words):
        trie = {}
        trie["palindromeSuffixes"] = []
        trie["words"] = []
        for wordIndex, word in enumerate(words):
            root = trie
            word = word[::-1]
            for charIndex, c in enumerate(word):
                if c not in root:
                    root[c] = {}
                    root[c]["words"] = []
                    root[c]["palindromeSuffixes"] = []
                if self._isPalindrome(word[charIndex+1:]) and charIndex+1 != len(word):
                    root[c]["palindromeSuffixes"].append(wordIndex)
                root = root[c]
            root["words"].append(wordIndex)
        return trie
    
    def _isPalindrome(self, word):
        left, right = 0, len(word) - 1
        while left < right:
            if word[left] != word[right]:
                return False
            left, right, = left + 1, right - 1
        return True



"""
Notes:
Found this very tricky. Excellent trie practice.

1) First method is brute forcing. Much simpler.
Make a dictionary mapping words in reverse to their indices.
Iteratge through the words.
Iterate through the chars in each word.
Get the prefix and suffix based on the current char.

Example:
Word = abcdef
char = 2
->
prefix = ab
suffix = cdef

Let the current word be indicated by A. Let B be a possible pair match. Then the question is whether or not
AB and/or BA is a palindrome. 

Either way, there must be some subsection of the word that is reflected on the opposite side and then
the middle of the word must be a palindrome as well. 

Therefore, since we're iterating through all the prefixes and suffices for each word we can check:

Case A:
prefix is in our dictionary of strings in reverse order AND the current index != the index of that value in the
dictionary AND the middle (which must be the suffix) is a palindrome


Case B:
suffix is in our dictionary of strings in reverse order AND the current index != the index of that value in the
dictionary AND the middle (which must be the prefix) is a palindrome
...and the index of our current split must be greater than 0

If either of these cases are true then we can add a match.






2) Second, assymptotically better, and more interesing method -> trie

Make a trie in the usual way with the words sorted in revese order. 
Make a function for checking if a string is a palindrome

Make a trie of all the words in reverse.

Extra info that we store at each node:
-Whenever we finish a word, store the index of the word at that node.
-When processing each letter, check if the remaining letters in the word form a palindrome.
If they do store the words index in a list in the node. Note this is a different list than
the list for when we finish a word


Iterate through the words
For word A, we're looking for palindromes formed by ---> AB <-------- important



2 cases:
["D", "EDED"]
["DEDE", "D"]


1) B is shorter than A
Step through the Trie for each letter of A in its original order. For example, say the TRIE already
contains
B = EDED

B is stored in the TRIE as DEDE

Now we're searching for
A = DEDEBAB

We step through D, E, D, E...

At each point we check if we've hit a completed word (by checking if its index is stored at that node).
Once we hit the second E in the example, we'll see that we've hit the complete word B. Now we check
if the remainder of A, BAB, is a palindrome. If it is, then we have a palindrome pair and we store
A's index and B's index in the result.


2) B is longer than A
Say we've already stored
B = QWQCBA

in the trie. Note that B is stored in the trie as 
ABCQWQ

Now we're searching for 
A = ABC

As in case 1, we step through the Trie according to A's characters and match as we go. After we finish
ABC, we check the final node's list of palindromes formed by suffixes of words...for example, when we
inserted QWQCBA into the trie, we would have inserted A -> B -> C -> Q -> W -> q...and after we inserted
C, we would have recorded B's index at C. So now as we're inserting A, we known that AB is a palindrome
and we can insert B's and A's indices in the result.


"""