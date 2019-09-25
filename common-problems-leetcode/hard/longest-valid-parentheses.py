"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
Accepted
217.2K
Submissions
823.6K
"""

# 44ms. 97 percentile.
# Stack approach
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        
        for i,c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                stack.pop()
                if not stack:
                    stack = [i]
                else:
                    left = stack[-1]
                    res = max(res, i - left)
        
        return res



# Pointer approach
# 48ms.
# 90 percentile.
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        opens, closes = 0, 0
        res = 0
        
        for c in s:
            if c == "(":
                opens += 1
            elif c == ")":
                closes += 1
            
            if opens == closes:
                res = max(res, opens + closes)
            elif opens < closes:
                opens, closes = 0, 0
        
        opens, closes = 0, 0
        for c in s[::-1]:
            if c == "(":
                opens += 1
            elif c == ")":
                closes += 1
            
            if opens == closes:
                res = max(res, opens + closes)
            elif closes < opens:
                opens, closes = 0, 0

        return res


"""
Notes:

-Longest Valid Parentheses:
	This problem is trickier than it looks at first glance. When you find a closed after an open, 
    you have a valid string going back to the open before it. That's simple. But this is more confusing:
	()(()
	At this point you just have a length 2 string. You can't count the next part because there's a dangling 
    open. So you need to remember that your potential valid string is starting at 0.


	Noting two approaches...one with a stack and one with pointers...

	Stack approach:
 	The crux/invariant of this is that we always want the bottom of the stack to record the best 
     possible (farthest left) start that we might be able to use. Further, we'd actually like it to 
     be one index to the left of the best possible start to make the math (with array indexing) even simpler.

 	So we start with -1 on the stack.

 	Whenever we see an open, we put its index on the stack. When we see a close, we pop the top.
 	If the top has the index of an open, then the closed we've just seen matches the open and we can 
     get a valid string at least between those two. However, rather than be greedy and match it, we 
     actually want to know the start of the current valid string. To that end, we pop the open from 
     the stack and then match with the next value on top of the stack. More specifically we take the 
     max of our current best distance and the best we've seen so far. Little example:

 	()()

 				 0                  2
 	-1 			-1      -1         -1       -1
 	stack
	best value   0     1-(-1)=2            3-(-1=4)

	Say we tacked another closed on to this example. We would pop off the -1 and then not be able to 
    get a distance. In this case, we have reached a point where we have more closed's than opens. So 
    everything until now is invalidated. So we start the process anew and push the current closed's 
    index onto the stack to mark a new beginning of a potentially valid string. 

	A bit of intuition:
	weirdly opens serve as barriers to extending the longest string. Until you have a closed for 
    each, you can't match as far back as possible. When you see a closed you're removing a barrier 
    in a sense while also recognizing that you do have a new match. So each spot on the stack says 
    "I'm a valid start point if you've matched everything ahead of me."




	Pointer approach:
	The methodology here is super simple. Keep left and right pointers. When you see an open, 
    increment left. Increment right when you see a closed. When they're equal, you have a new valid
     distance. This is equal to twice right (or left, they're the same) Basically the 2 multiplier 
     just says for every open you have a closed. 

	Intuitively you're just counting opens and if you have a closed for every open, you have a match.

	Importantly, if right exceeds left, then you have too many closed's for your opens and you reset 
    left and right both to 0. 

	Then you repeat this whole process in reverse (and flip left and right)


	Intuition for why this works:
	The key intuition is still that you need to balance any matches you generate with the farthest 
    back that you could possibly start matching. 

	You know that if you get a closed for every open and you never had more closed's than opens, 
    then you have a valid string. You'll definitely catch all the max length matches. But you'll 
    miss the local solutions.  

	()(((()))

	For example, with this one, at the end you'll have 5 opens and 4 closeds. So the only match 
    you'd get would be the first (). You'll miss the length 6 match at the end. 

	The backward pass is the magic that makes it all work. In that case, you'll catch that local 
    solution (and actually start anew before the last () ).

"""