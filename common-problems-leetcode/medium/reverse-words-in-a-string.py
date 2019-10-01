"""
Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Follow up:

For C programmers, try to solve it in-place in O(1) extra space.

Accepted
274,305
Submissions
1,662,513
"""
# 100th percentile. 36ms
class Solution:
    def reverseWords(self, s: str) -> str:
        s = re.compile("[\s]+").split(s.strip())[::-1]
        return ' '.join(s).strip()


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([ word for word in s.split(" ")[::-1] if word != "" ])
        