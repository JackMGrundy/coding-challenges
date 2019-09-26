"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
Accepted
197.6K
Submissions
500.2K
"""
# 212ms. 23 percentile.
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        if n == 0 or m == 0:
            return n + m
        
        dp = [ [0 for _ in range(m+1)] for _ in range(n+1) ]
        
        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j
            
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = dp[i - 1][j] + 1
                down = dp[i][j - 1] + 1
                leftDown = dp[i - 1][j - 1] 
                if word1[i - 1] != word2[j - 1]:
                    leftDown += 1
                dp[i][j] = min(left, down, leftDown)
        
        return dp[n][m]

"""
Notes:

	DP problem. Let i denote characters 0 to i in word1 and let j denote characters 0 to j in word2. And let D[i][j] be the edit distance 
    between those two subsets of characters.

	Turns out that if you know D[i-1][j], D[i][j-1], D[i-1][j-1] then you can figure out D[i][j]. 

	First here's the equation:

	if ith character or word1 and the jth charcter of word2 are equal:
		1 + min(D[i-1][j], D[i][j-1], D[i-1][j-1]-1)
	else:
		1 + min(D[i-1][j], D[i][j-1], D[i-1][j-1])

	In either case, the first two terms come about because given the distance between one word and the other with one less character, with 
    one extra step you get to the extended word. 

	The only wrinkle is the case where they are each missing a letter. If the last letters are the same, the the distance between D[i][j] 
    and D[i-1][j-1] are equal...the extra character doesn't change anything. So we subtract the 1 to account for that. 

	Intuition with a graph:

	To get the dp going, 

	E   5

	S   4

	R   3

	O   2   2   1

	H   1   1   2

	""	0   1   2   3

		""	R 	O 	S

	We can get the rows and columns using the intuitive conclusion that empty string to not empty string is just the cost of adding each of the 
    letters. Then we have everything we need to fill.

	To build the intuition, a given square tells you how much it costs to start at the string on one axis and then go to the string on the other. 
    I'm thinking of it as going from the y axis to the x axis. Going to the right means substitution if the resulting lengths are the same. 
    For example, changing H to R. If the resulting lengths aren't the same, you're inserting. If you're going up the logic is the same. 
    Interestingly, if you think of the same process in reverse, then instead its substitution and then deletion.
	i.e. OH -> R involves a deletion and a substitution. But R -> OH involes an insertion and a substitution. 
	Again, the only hiccup is if the "next" letters are equal. Then edit distance isn't increased. 

"""