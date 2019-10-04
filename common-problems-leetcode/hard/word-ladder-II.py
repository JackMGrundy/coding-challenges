"""
Given two words (beginWord and endWord), and a dictionary's word list, 
find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""


# 496ms. 54 percentile. One way bfs without bridge words.
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordLength = len(beginWord)
        validWords = set(wordList)
        validPaths = []
        paths = {}
        paths[beginWord] = [[beginWord]]
        searching = True
        
        while paths and searching:
            extendedPaths = collections.defaultdict(list)
            for lastWord, pathsEndingInLastWord in paths.items():
                if lastWord == endWord:
                    validPaths.extend(pathsEndingInLastWord)
                    searching = False
                elif searching:
                    for i in range(wordLength):
                        for c in string.ascii_lowercase:
                            newWord = lastWord[:i] + c + lastWord[i+1:]
                            if newWord in validWords:
                                extendedPaths[newWord] += [path + [newWord] for path in pathsEndingInLastWord ]
        
            validWords -= set(extendedPaths.keys())
            paths = extendedPaths
    
        return validPaths



# 164ms. 79 percentile.
# One way bfs with bridge words.
from collections import defaultdict, deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        bridgeWords = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                bridgeWord = word[0:i] + "*" + word[i+1:]
                bridgeWords[bridgeWord].append(word)
        
        searching = True
        paths = defaultdict(list)
        paths[beginWord] = [[beginWord]]
        shortestPaths = []
        visited = set()
        
        while paths and searching:
            extendedPaths = defaultdict(list)
            for lastWord, pathsEndingInLastWord in paths.items():
                if lastWord == endWord:
                    searching = False
                    shortestPaths.extend(pathsEndingInLastWord)
                elif searching:
                    for i in range(len(lastWord)):
                        bridgeWord = lastWord[0:i] + "*" + lastWord[i+1:]
                        if bridgeWord in bridgeWords:
                            for neighbor in bridgeWords[bridgeWord]:
                                if neighbor not in visited:
                                    extendedPaths[neighbor] += [ path + [neighbor] for path in pathsEndingInLastWord ]
                                    
                
            for key in extendedPaths.keys():
                visited.add(key)
            paths = extendedPaths
        
        return shortestPaths



# 108ms. 94 percentile.
# Double BFS
from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        tree, validWords = defaultdict(list), set(wordList)
        
        def addToPath(tree, word, neighbor, isForward):
            if isForward:
                tree[word].append(neighbor)
            else:
                tree[neighbor].append(word)
        
        def constructPaths(source, destination, tree):
            if source == destination:
                return [[destination]]
            else:
                res = []
                for successor in tree[source]:
                    res.extend([ [source] + path for path in constructPaths(successor, destination, tree) ])
                return res
        
        def biDirectionalBFS(thisSide, otherSide, isForward, validWords, tree):
            if len(thisSide) == 0:
                return False
            if len(otherSide) < len(thisSide):
                return biDirectionalBFS(otherSide, thisSide, not isForward, validWords, tree)
            for word in (thisSide or otherSide):
                validWords.discard(word)
            
            thisSideExtended, done = set(), False
            while 0 < len(thisSide):
                word = thisSide.pop()
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        neighbor = word[0:i] + c + word[i+1:]
                        if neighbor in otherSide:
                            done = True
                            addToPath(tree, word, neighbor, isForward)
                        if not done and neighbor in validWords:
                            thisSideExtended.add(neighbor)
                            addToPath(tree, word, neighbor, isForward)
                
            return done or biDirectionalBFS(thisSideExtended, otherSide, isForward, validWords, tree)
        
        biDirectionalBFS(set([beginWord]), set([endWord]), True, validWords, tree)
        return constructPaths(beginWord, endWord, tree)



"""
Notes:

There are two approaches I like: one simpler and one faster

-----------------Simpler approach-------------------------
Straight BFS with some clever specifics...

We process entire layers one at a time...kind of like in remove min parentheses to make a valid
string. 
A layer is stored as a dictionary where values are lists of words and the key is the last word
in the last. 
To process a layer, we iterate through each list of words. If the key (last word in the list) is
the target end word, we found an answer and we stop that line of search. Otherwise, we try to 
continue the line of search. Because we are processing one layer at a time, we have a new dictionary
containing the next layer's information. To populate this based on the previous line of search: we 
iterate through every char in the last word in the previous line of search. We try switching it to
any lower case letter. If the resulting word is in the set of valid words, we add the
newWord : [oldList] + [newWord] key-value pair to the next layer dictionary.

Now the clever/confusing bit. We can't assume that the last word in each line of search is 1:1
with the line of search. For example we could have:

    hot  :    dit dot hot
    hot  :    dop hop hot

    As a result, we need to combine these as in:

    hot : [  [dit, dot, hot], [dot, hop, hot]   ]

Importantly, once we finish creating the new layer dictionary, we eliminate the last words in each
of the lines of search from the set of valid words. This avoids cycles. We can do this because
we only care about shortest paths. 







------------------ Faster/cooler but more complicated approach -------------
Bi-directional bfs...

Super cool idea, but hard to make concise. 

With the bi-directional bfs, we have a main function that populates a data structure of
dictionaries within dictionaries for a trie-like approach.

The idea is that given a problem such as:
"hit"
"cog"
["hot","dot","dog","lot","log","cog"]

The tree will be populated with:
defaultdict(<class 'list'>, {'hit': ['hot'], 'hot': ['dot', 'lot'], 
                              'dog': ['cog'], 'log': ['cog'], 'lot': ['log'], 'dot': ['dog']})

Given this, we build up the valid paths by branching whenever we hit a node with multiple children.

Now for the bfs method. It's very similar to the simpler bfs but we juggle two different 
bfs's in one method. 

Normally it's a bit bizarre to think of doing a recursive bfs. Here we use recursion not
to advance the bfs, but rather to alternate the sides of the search.

Here are the recursive calls produced by the example above:
this_lev: {'hit'}, otherLevel: {'cog'}, isForward: True
this_lev: {'hot'}, otherLevel: {'cog'}, isForward: True
this_lev: {'dot', 'lot'}, otherLevel: {'cog'}, isForward: True
this_lev: {'cog'}, otherLevel: {'dot', 'lot'}, isForward: False
this_lev: {'dog', 'log'}, otherLevel: {'dot', 'lot'}, isForward: False

If the other level has fewer elements than this level, then we immediately recurse
with the sides switched and return whatever the recursion produces. As a result, we're not
branching, our recursion tree just has one path straight down. 

At each level of recursion:
To avoid cycles, remove all words at the fringes of either side from the set of valid words
To construct the next level, we iterate through all the words in the current level
and try substituting a lower case char in for every char. 

If we find a word that's in the
other level, then we know that we have a complete path from the start to the end. 

Otherwise, if the word is in the set of valid words we can add the word to the next level.

In both these cases we want to update our tree...this is the last tricky bit of 
this algorithm. The addToPath helper deals with this. Here's the simple intuition

Let's say this our path
A -> B -> C -> D -> E -> F

This is the order our bi-directional BFS is going to travese this path
A -> B -> C
F -> E -> D

We want our tree to reverse the arrows in the second half though. As a result
we pass the boolean forward variable to every level and reverse it whenever
we're working on the second list. Given that boolean, we can still traverse the 
chain like:
A -> B -> C
F -> E -> D

But build our tree as in
A -> B -> C -> D
D -> E -> F
= A -> B -> C -> D -> E -> F
"""