"""
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
Accepted
97.9K
Submissions
219.9K
"""
# 81st percentile. 36ms.
"""
Hate to say it, but I had a really hard time with this one. Thankfully, finally got there.
I looked up the solution after the fact and it looks like I got the idea 90% right. You can
simplify things a bit by using two stacks. But I've spent enough time on this. Sticking with it. 
"""
class Solution:
    def decodeString(self, s: str) -> str:
        s = list(s)
        res = []
        stack = []
        opens = 0
        
        for c in s:
            if c == "[":
                opens += 1
            
            elif c == "]":
                opens -= 1
                cur = stack.pop()
                temp = []
                
                # Get string contained in group
                while cur != "[":
                    temp = [cur] + temp
                    cur = stack.pop()
                
                # Get number associated with group
                d = stack.pop()
                k = []
                while stack and d.isdigit():
                    k = [d] + k
                    d = stack.pop()
                
                if not d.isdigit():
                    stack.append(d)
                else: 
                    k = [d] + k
                
                # Add group back on stack
                stack = stack + temp*int(''.join(k))
                
                # We're not in a group. Add cur string to res
                if opens == 0:
                    res += stack
                    stack = []
                    
                continue
                
            stack.append(c)
            
        return ''.join(res + stack)
            
            