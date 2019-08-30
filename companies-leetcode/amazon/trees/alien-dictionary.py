"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""

"""
Keep a dictionary that maps letters to children

Start a loop looking at pairs of words at a time. Loop through the letters of a pair of words until finding a pair of
letters that are different. Make sure both letters are keys in the dictionary. Check if the letter in the second word 
if in the first letter's children. If it isn't add it

Continue to the next pair of words

We end up with a dictionary representing a graph. 

Keep a list of visited nodes
DFS to check for cycles and recover ordering...https://en.wikipedia.org/wiki/Topological_sorting
Topological sort deal...
"""
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        children = collections.defaultdict(set)
        degree = {c:0 for w in words for c in w}
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            for c in range(min(len(w1), len(w2))):
                c1, c2 = w1[c], w2[c]
                if c1!=c2:
                    if c2 not in children[c1]:
                        degree[c2] += 1
                        children[c1].add(c2)
                    break
        
        res = []
        queue = collections.deque([c for c in degree.keys() if degree[c]==0])
        
        while queue:
            cur = queue.popleft()
            res.append(cur)
            for c in children[cur]:
                degree[c] -= 1
                if degree[c] == 0:
                    queue.append(c)
        
        return(''.join(res) if len(res)==len(degree) else '')