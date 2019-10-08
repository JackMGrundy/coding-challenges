"""
Given  a  non-empty  string  s  and  a  dictionary wordDict containing a list of
non-empty  words,  add  spaces in s to construct a sentence where each word is a
valid dictionary word. Return all such possible sentences.                      

Note:                                                                           

The   same  word  in  the  dictionary  may  be  reused  multiple  times  in  the
segmentation.                                                                   

You may assume the dictionary does not contain duplicate words.                 

Example 1:                                                                      

Input:                                                                          

s = "catsanddog"                                                                

wordDict = ["cat", "cats", "and", "sand", "dog"]                                

Output:                                                                         

[                                                                               

  "cats and dog",                                                               

  "cat sand dog"                                                                

]                                                                               

Example 2:                                                                      

Input:                                                                          

s = "pineapplepenapple"                                                         

wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]                    

Output:                                                                         

[                                                                               

  "pine apple pen apple",                                                       

  "pineapple pen apple",                                                        

  "pine applepen apple"                                                         

]                                                                               

Explanation: Note that you are allowed to reuse a dictionary word.              

Example 3:                                                                      

Input:                                                                          

s = "catsandog"                                                                 

wordDict = ["cats", "dog", "sand", "and", "cat"]                                

Output:                                                                         

[]                                                                              

"""
# Timeouts
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [False]*len(s)
        dp[0] = True
        res = []
        
        def dfs(i, ans):
            if i == len(s):
                res.append(ans.strip())
            if len(s) < i:
                return
            
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    dfs(i + len(word), ans + " " + word)
        
        dfs(0, "")
        return res



# 48ms. 89 percentile.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        words = set(wordDict)
        def dfs(word):
            if word in memo:
                return memo[word]
            res = []
            if word in words:
                res.append([word])
            for i in range(len(word)):
                w = word[:i]
                if w in words:
                    temp = dfs(word[i:])
                    res += [ [w] + path for path in temp ]
            memo[word] = res
            return res
        ans = [ ' '.join(path) for path in dfs(s) ]
        return ans


# 44ms. 96 percentile.
# built ins.
from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        
        @lru_cache(maxsize=None)
        def dfs(word):
            res = []
            if word in words:
                res.append([word])
            for i in range(len(word)):
                w = word[:i]
                if w in words:
                    temp = dfs(word[i:])
                    res += [ [w] + path for path in temp ]
            return res
        ans = [ ' '.join(path) for path in dfs(s) ]
        return ans

"""
Notes:

We start a recursive call on the full string. 
We memoize to speed things up, so we can stop early if we have already 
processed this string. 

At each level of recursion we have a list of results. This list
contains all the paths to the end from this point. 

Our effective stopping condition is when the full word is contained
in the list of words. 

Even if we hit a stopping condition, we could keep matching with the
letters contained in the current letter. If we find a word in the set
of words, we recurse to another level with a shortened starting word. 
When we return, we have a list of lists where each list is a path to the
end starting from the current level's i. To build up the paths, we 
tack the current word on to each path.

"""