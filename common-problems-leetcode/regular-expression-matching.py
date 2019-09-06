"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""


# 1308ms. 22nd percentile.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        
        matchNextChar = p and s and p[0] in { ".", s[0] }
        
        if len(p) >= 2 and p[1] == "*":
            return self.isMatch(s, p[2:]) or (matchNextChar and self.isMatch(s[1:], p))
        else:
            return matchNextChar and self.isMatch(s[1:], p[1:])



# 60ms. 60 percentile.
# bottom up dp
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [ [ False for x in range(len(p)+1) ] for _ in range(len(s)+1) ]
        
        # Empty pattern matches empty string
        dp[0][0] = True
        
        # Empty pattern cannot match a nonempty string
        for j in range(1, len(s)):
            dp[j][0] = False
        
        # Edge case. If every pattern character is qualified by a star, then the pattern
        # can match an empty string
        pMatchesEmptyString = True
        i = 2
        while i <= len(p) and pMatchesEmptyString:
            if p[i-1] == "*":
                dp[0][i-1] = True
                dp[0][i] = True
            else:
                pMatchesEmptyString = False
            i += 2
        
        for j in range(1, len(s)+1):
            for i in range(1, len(p)+1):
                
                # Current char matches
                if p[i-1] in [s[j-1], "."]:
                    dp[j][i] = dp[j-1][i-1]
                # Deal with stars
                elif p[i-1] == "*":
                    # We don't need the star to match
                    if dp[j][i-2]:
                        dp[j][i] = dp[j][i-2] 
                    # The current char is "part" of the start expression
                    elif p[i-2] in [s[j-1], "."]:
                        dp[j][i] = dp[j-1][i]
        
        return dp[-1][-1]

"""
Notes:

Without the Kleene starts, you would just match characer by character. 
Note that if there is no pattern, then you need to return not text (if there's no text, then no pattern is actually match)
Use a recursive solution. At each level, check the current letter. Return if it's a match and then the recursive call to the reamining letters

Kleene star complicates a little bit. Now there are two possible ways to match a character. It could be a plain match. Or we could utilize a star. Here's the logic split:

If the next character is a star:
	return  
		match the text without using the star (meaning we cut 2 chars from the pattern)...so just a recursive call
	    or
	    we match the current char, and thanks to the star, we do a recursive call but don't have to shorten the pattern...we can keep the star
otherwise,
     return the normal way...check if the current char matches and then decrease the text and the pattern by 1
"""




"""
Notes:

Bring in DP:

Text:     xaabyc
Pattern:  xa*b.c



                          j  pattern

	                 0       1       2      3      4     5     6
	 
                             x       a      *      b     .     c

	     0          T       F        F      F      F     F     F

	     1  x       F       T        F      T      F     F     F
	     
i        2  a       F       F        T      T      F     F     F
string
   		 3  a       
	   
	     4  b       
	  
	     5  y       
	     
	     6  c       


Didn't fill in most of it, but what to note here...
0,0 is true becase a "" pattern will match an empty string
Otherwise the first column if false because an empty pattern cannot match any characters
The first row is all falses here (Except 0,0), but could have trues because if every char in the 
pattern is qualified by a star, then it could match an empty string

Now for the meat and potatoes...

For a given square, 

check if the jth pattern char matches the ith text char or if the jth pattern char is a period...if 
it is, take the value from one column to left and one row up. We're saying, "if we were matching on 
the char before, then we're still matching now. But if weren't matching...then we're still not"
If there isn't a match at the current square, then it's just false. 

IF the jth pattern char is a star there are two ways the current square could be true
1)
First look at T[i][j-2]...basically two chars earlier in the pattern...if that's true, the current 
square is true. This is saying "say we don't use the star...we can't advance the pattern, 
but we could still be true".
2)
If the character before the star matches the current char, then look 
above the current square. so T[i-1][j]. Now we're matching the current regex with one less text char.
...we're checking if the current char could be "considered part of the star expression"

"""


# Top down DP
# 44ms. 96 percentile
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def helper(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = (i == len(s))
                else:
                    curCharMatch = i < len(s) and p[j] in {s[i], "."}
                    if j+1 < len(p) and p[j+1] == "*":
                        ans = helper(i, j+2) or (curCharMatch and helper(i+1, j))
                    else:
                        ans = curCharMatch and helper(i+1, j+1)

                memo[(i, j)] = ans
            return memo[(i, j)]
        
        return helper(0, 0)

"""
Notes:
i,j are positions in the string and the pattern
First check if the string character matches the pattern character and store it
Then we have two cases.
1) the pattern char is a star:
    Two ways we could match now:
    1) Match without using the star...aka advance j 2
    2) Match with the current char as part of the star
        We need to match on the current char and we must match
        on another call that advances the text string one character
        but that doesn't advance the pattern (we're still using the star)

2) Else:
    Simpler. Question is, "do we match on the current char and everything
    to come after this"


Stopping condition:
    The question calls for a complete match between the pattern and the
    string. We can just check reaching the end of the pattern. The check
    in the middle for i < len(s) will cut off calls that could get
    us to the end of the string before the end of the pattern. 

Bring in DP:
    Just memoize each call

"""
