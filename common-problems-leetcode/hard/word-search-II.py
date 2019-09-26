""" 
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
 

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
"""
# 328ms. 88 percentile.
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = self._createTrie(words)
        foundWords = []
        
        def backtrack(i, j, parentTrieNode):
            
            # element is out of bounds
            if not (0 <= i < len(board) and 0 <= j < len(board[0])):
                return
            
            # cur string not in trie
            letter = board[i][j]
            if letter not in parentTrieNode:
                return
            
            curTrieNode = parentTrieNode[letter]
            
            # found a match
            if "*" in curTrieNode:
                foundWords.append(curTrieNode["*"])
                del curTrieNode["*"]
            
            board[i][j] = "#"
            neighbors = [ (i+1,j), (i,j+1), (i-1,j), (i,j-1) ]
            for neighbor in neighbors:
                nI, nJ = neighbor
                backtrack(nI, nJ, curTrieNode)
            
            board[i][j] = letter
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack(i, j, trie)
        
        return foundWords
    
    
    def _createTrie(self, words):
        trie = {}
        for word in words:
            root = trie
            for c in word:
                if c not in root:
                    root[c] = {}
                root = root[c]
            
            if "*" not in root:
                root["*"] = word
        
        return trie

"""
Notes:

Interesting problem. 

The brute force is to loop through the cells in the board and complete a backtracking search at each cell. This is also the start
of a better solution.

The gist of this idea is good, but we need a way to quickly end searches that won't yield results. To do that, we make a trie out of the words
we are search for.

As we do the backtracking search, if adding a new letter would yield a string that is not contained in the trie, then we cut off the search - we
know there is no way that search could yield a result. 

Whenever we find a word, remove it from the trie so we don't get duplicates later.

That's the core answer. After this we just have some optimizations. 
1) Say we find a word and the last letter in the word is a leaf node. We can prune that node...we already found the word and recorded it and 
it cannot lead to any other unfound words...so there's no way we would need it. 

2) We could simply use the trie to lookup every prefix during backtracking. An optimization is to backtrack in the trie at the same time.



Complexity:
We know we'll have a call for every element, and there are N*M elements. The worst case time for a call is the length of the longest word. 
"""