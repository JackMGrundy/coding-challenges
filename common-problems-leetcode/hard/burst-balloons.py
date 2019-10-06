"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""


# Top down.
# 544ms. 40th percentile.
# Note that this TO's without the lru_cache decorator
from functools import lru_cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        
        @lru_cache(maxsize=None)
        def dp(left, right):
            if left == right - 1:
                return 0
            
            bestAnswer = -float("inf")
            for i in range(left + 1, right):
                bestAnswer = max(bestAnswer, nums[left]*nums[i]*nums[right] + dp(left, i) + dp(i, right))
            
            return bestAnswer
        
        return dp(0, len(nums) - 1)



# Bottom up
# 440ms. 68 percentile.
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        
        dp = [ [0 for j in range(len(nums))] for i in range(len(nums)) ]
        
        for left in range(len(nums) - 2, -1, -1):
            for right in range(left + 2, len(nums)):
                
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right], nums[left]*nums[i]*nums[right] + dp[left][i] + dp[i][right])
        
        return dp[0][-1]



"""
Notes:

Top Down Approach:
Frst bit, to simplify things, cap the array with 1's 

	Dp function:
	Stopping condition is when left and right are adjacent

	DP method takes in left and right boundaries. All it does: for each balloon i between left and right. 
    Take balloon i's value * balloon_left * balloon_right. Then add that to two recursive calls to the 
    subarrays you get from splitting the array around i.

	Finally repeat that process for every balloon. And take the max of all those attempts. 

	In pseudocode:

	dp(left, right)

	if left is one less than right, break

	Get max of (
		for each i between left and right (not inclusive)
		 val = balloon_left * balloon_i * balloon_r + dp(left, i) + dp (i, right)
	)

	^Note this is missing the memoization part. You could do that with a 2d memo. Then in dp, 
    you check if you already have a memo entry. 
	A good trick, for Python at least, would be to use
	@lru_cache



	Intuition:
	At each recursive call you're saying, "let's say I did as good of a job as I could bursting 
    everything between left and i and between i and right. That would give me some number of coins. 
    Then when I bust balloon i, I'd also get its amount times left times right."

	dp saves us here by drastically cutting down the number of calls. The question "what's the best I 
    could do with balloons j to k" can be relevant to multiple subproblems. Thanks to dp, we just do it once. 

	
	Complexity:
	O(N^3). You don't have to think through the complexity of all the calls here. Just note that there 
    are N^2 different left, right combos. For each one, to get its value, you're going to have burst 
    the O(N) balloons between them. So O(N^3).


Bottom up approach:
	Still cap the array with 1's. 

	Basically the same as before except without recursion. Make a 2d memo. Then iterate over the 
    memo. How to iterate over the memo is important.

	Decrement left from the end of the range to the beginning. Right just advances from left to the end. 

	It can look kind of weird at first, but take a look at the dp array below. 
    ----> You would fill from the bottom up, and left to right <-------------


					right

				0   1 	2 	3 	4   5

			0           x   x   x   x 

	left    1               x   X   x
  
            2                   x   x

            3                       x 

            4 

            5 

    Intuition:
    You don't need calls where left==right or left==right-1. The whole logic is built around "let's say I do 
    the best I can with the subarrays around i and then pop i". This requires three balloons, left, i, and right. 
    So at a minimum, right is going to start 2 to the right of left. Also, it doesn't make sense for left 
    to be greater than right. That explains the empty squares.

    As for the order, just note that basically what we're doing is setting limits for left and right and 
    then iterating with i over the values between them (just as with top down). That means we'll need the 
    values for (left, i) and (i, right). i is guaranteed to be greater than left by construction. Meaning 
    that we'll need the "higher" left values to complete the lower levels. 

    Example:
    Say we're filling spot left=1, right=4. 
    That means we'll try middle = 2 or 3

    For left=1, middle=2, right=4 
    we'll need
    dp[1][2]
    dp[2][4]

    for left=1, middle=3, right=4
    we'll need
    dp[1][3]
    dp[3][4]


    This implies that another traversal would be to do 
    (0,2), (1,3), (0,3), (2,4), (1,4), (0,4), (3,5), (2,5), (1,5), (0,5)

    Our final answer will be the top right element in our grid.

"""