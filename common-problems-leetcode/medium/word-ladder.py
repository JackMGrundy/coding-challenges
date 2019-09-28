"""
Given two words (beginWord and endWord), and a dictionary's word list, 
find the length of shortest transformation sequence from beginWord to endWord, 
such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a 
transformed word.
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
"""
# 91st percentile. 108ms.
from collections import defaultdict
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        
        # Construct dicitonary of interemediate states to save time
        L = len(beginWord)
        intWords = defaultdict(list)
        for word in wordList:
            for i in range(L):
                intWords[ word[:i] + "*" + word[i+1:] ].append(word)
        
        # BFS
        q = deque()
        q.append( (beginWord, 1) )
        visited = set([beginWord])
        while q:
            cur, d = q.popleft()
            
            for i in range(L):
                intWord = cur[:i] + "*" + cur[i+1:]
                for nxtWord in intWords[intWord]:
                    if nxtWord in visited: 
                        continue
                    if nxtWord == endWord:
                        return d+1
                    else:
                        visited.add(nxtWord)
                        q.append( (nxtWord, d+1) )
        
        return 0