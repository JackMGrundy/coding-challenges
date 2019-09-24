"""
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
Accepted
106.6K
Submissions
436.4K
"""

# 40ms. 47th percentile.
# 90+ percentile is like 32ms. 
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        curLineWords = []
        numNonWhiteSpaceChars = 0
        
        for word in words:
            if maxWidth < numNonWhiteSpaceChars + len(curLineWords) + len(word):
                for i in range(maxWidth - numNonWhiteSpaceChars):
                    if 1 < len(curLineWords):
                        curLineWords[i % (len(curLineWords)-1 or 1) ] += " "
                    else:
                        curLineWords[0] += " "
                
                res.append( ''.join(curLineWords) )
                curLineWords, numNonWhiteSpaceChars = [], 0
            
            curLineWords += [word]
            numNonWhiteSpaceChars += len(word)
        
        return res + [ ' '.join(curLineWords).ljust(maxWidth) ]

"""
Notes:

Leetcode actually doesn't want the best algorithm you can possibly come up with for this...
not the dp approach that minimizes extra white space...just wants greedy solution. 

Good way to approach it.

Loop through the words one at a time...
at each point you're building up a line...to know when you should start a new line, you need
a list of the words on the current line and an int describing the total number of non whiespace 
characters inclded in the current line. To check if you should start a new line, just see 
if new_word_length + #current_letters + len(num words)...accounts for whitespace + len(next word)...
would exceed the max width allowed.
If it would, you need to allocate the excess spaces to the words. To do that, use a mod formula 
to round robin add spaces. 

"""