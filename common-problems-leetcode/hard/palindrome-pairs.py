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
Notes:
Make a trie in the usual way with the words sorted in revese order. 
Make a function for checking if a string is a palindrome

Make a trie of all the words in reverse
Iterate through the words
For word A, we're looking for palindromes formed by AB
2 cases:
1) B is shorter than A
Go through the Trie for word A. Effectively you're going over the word backwards. 
Whenever you hit a marker of an actual word in the array, then that means you have a possible 
palindrome. Check if the the remainder of A (that we haven't traversed yet is a paldindrome. If 
it is, that's a new word.)
2) B is longer than A
Completely match A through the trie. This is equivalent to matching as much of B in reverse as 
you can. B is going to have extra letters.
Any palindromes that are formed from the nodes after our final node (the last/first letter of A) 
indicate a full palindrome. 
Instead of doing a full search from that node for palindromes, we store "plaindromes farther than 
down the trie" at each node. 
...to do this...as you're adding a word to the tree, after traversing (or creating) each node, 
check if the reamining letters to be added form a palindrome. If they do, add it to the current 
nodes list. 

"""