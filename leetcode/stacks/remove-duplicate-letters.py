"""
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"
"""
# 1st attempt: 81st percentile in speed. O(N)
"""
Intuition:
Get counts of each char. Then iterate through the string. Att each char, if we have already visited it,
(it is already in the stack), continue. If not, then check if A) the stack has stuff in it B) the current
character would be a lexiographically better choice than the current character at the top C) If we 
were to pop the top character, would it appear later in the string so that we could add it then. If all three
are met, then pop the top, place the new character on there, and make the fold character as not visited.

The reason a stack is helpful, is that we might need to this a few times. For example, let's say the
string starts out being "zxyqwe" and then we see "a". If all of the current chars in the string do appear later,
then we want to ditch all of them and make the string just "a"...a simple greedy approach of looking
at just the last character won't work...hence a stack.

Sidenote: notice that we don't need ord(). Python will automatically apply it when comparing the 
characters. 
"""
from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s: return ""
        s = list(s)
        counts = Counter(s)
        stack = []
        visited = { key:False for key in s}
        
        for token in s:
            counts[token] -= 1
            
            if (visited[token]): continue
            
            while (stack and stack[-1]>token and counts[stack[-1]]):
                visited[stack.pop()] = False
            
            stack.append(token)
            visited[token] = True
        
        return ''.join(stack)


# 2nd attempt: 94th percentile in speed
"""
If you think about it, we don't need to maintain counts. We just want to know if there
is a copy of a char left in the strin before we pop it. So we just need to know the last index
of each char in s. This saves times because we don't have to maintain counts
"""
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s: return ""
        s = list(s)
        lasts = { key:val for val,key in enumerate(s)  }
        stack = []
        visited = { key:False for key in s}
        
        for i, token in enumerate(s):
            
            if (visited[token]): continue
            
            while (stack and stack[-1]>token and i < lasts[stack[-1]]):
                visited[stack.pop()] = False
            
            stack.append(token)
            visited[token] = True
        
        return ''.join(stack)
                
            
            
        