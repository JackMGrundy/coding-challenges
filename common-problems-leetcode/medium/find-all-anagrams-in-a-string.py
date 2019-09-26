"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
# 112ms. 80 percentile
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pChars = [ 0 for _ in range(128) ]
        for c in p:
            pChars[ord(c)] += 1
        
        anagramChars = [ 0 for _ in range(128) ]
        anagramStarts = []
        
        for i, c in enumerate(s):
            if len(p) <= i:
                anagramChars[ ord(s[i - len(p)]) ] -= 1
            
            anagramChars[ ord(s[i]) ] += 1
            if anagramChars == pChars:
                anagramStarts += [i - len(p) + 1]
        
        return anagramStarts
    

"""
Notes:

You could do an implementation with Collections.Counter...but its a lot slower due to the comparison operations and having to delete
0 count elements from the counters
"""