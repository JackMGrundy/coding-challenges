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


"""
Upon reading this, I immediately think of using a hash table scheme to record valid palindromes as we go 
along. Then when we later see a match, we record. The problem with this is that it can get really complicated
and take up a ton of space. For example, the word "aaaaaa" generates the valid pairs "a", "aa", "aaa", "aaaa",
"aaaaa", "aaaaaa", ... actually any number of a's. Trying to record something like "any word consisting of only
a's" is frustrating.
Also, say you wanted to check if a new word was a palindrome. You would need to store that obnoxious hash table(s)
...otherwise you'd have to go through all the words again to construct it. 

A better solution is to use a trie. How this works:

Preliminaries:
Make a trie in the usual way with the words sorted in revese order. 
Make a function for checking if a string is a palindrome

Now we want to check for valid palindrome pairs for a given word A. There are two relevant cases:
1) 

"""