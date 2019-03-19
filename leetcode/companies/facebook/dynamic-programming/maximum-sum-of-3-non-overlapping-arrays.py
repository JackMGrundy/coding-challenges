"""
In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example:
Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Note:
nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).
"""
# class Solution:
    # def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # pass

# Attempt 1: 77th percentile in speed
# 3 passes. 1 to get an array that gives the best sum and its location as you go from left to right
# a second to get an array that gives the best sum and its location as you go from right to left
# a third to check the best possible overall sums in each spot...you can get the current sum, and then
# the best sum available on the left and the best available on the right...
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < 3*k: return []

        # Allocate prefix sums
        sums = [0]*(len(nums)-k+1)
        sums[0] = sum(nums[0:k])
        for i in range(1, len(nums)-k+1):
            sums[i] = sums[i-1] - nums[i-1] + nums[i+k-1]

        # Keep track of the greatest sum subarray as you move forwards through the array
        dpForward = [ [0, 0] ]*len(sums)
        dpMax = -float("inf")
        for i, s in enumerate(sums):
            if s > dpMax:
                dpMax = s
                dpForward[i] = [dpMax, i]
            else:
                dpForward[i] = dpForward[i-1]

        # Keep track of the greatest sum subarray as you move backwards through the array
        dpBack = [ [0, 0] ]*len(sums)
        dpMax = -float("inf")
        for i in range(len(sums)-1, -1, -1):
            s = sums[i]
            if s > dpMax:
                dpMax = s
                dpBack[i] = [dpMax, i]
            else:
                dpBack[i] = dpBack[i+1]

        # Main pass: for each possible sub array, we can get the best subarrays on either side
        #           using the dp arrays
        dpMax = -float("inf")
        res = [0, 0, 0]
        for i in range(k, len(sums)-k):
            temp = sums[i] + dpForward[i-k][0] + dpBack[i+k][0]
            if temp > dpMax:
                dpMax = temp
                res = [ dpForward[i-k][1] , i,  dpBack[i+k][1] ]

        return res



# Attempt 2: 23rd percentile in speed.
# A significantly more confusing approach. HUGE PLUS: this is generalizable to different window sizes
# and different k's
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        numWindows = 3
        if not nums or k <= 0 or len(nums) < k*numWindows: return []

        # Generate partial sums
        sums = [0]*(len(nums)-k+1) 
        sums[0] = sum( nums[0:k] )
        for i in range(1, len(nums)-k+1):
            sums[i] = sums[i-1] + nums[i+k-1] - nums[i-1]

        # NOTE: note. if you try to use * twice, you'll get unexpected behaviour
        dp =   [ [0]*(len(nums)+1) for _ in range(numWindows+1) ]
        locs = [ [0]*(len(nums)+1) for _ in range(numWindows+1) ]

        # Loop through the number of windows
        for i in range(1, 1+numWindows):
            # For the ith window, we could select a window between i*k and the end
            # ...the first i-1 windows must be contained in the area before this.
            # For each window, iterate through the valid partial sums.
            # Given this choice, we can identify the best sum we can get from the earlier arrays...
            # dp[i][j] tells you: "for the ith window, given elements 0 to j, we can generate a total of dp[i][j]"
            # So adding together the sum at location j and dp[i][j-k] (j-k is the last valid element for earlier arrays
            # assuming we select j for the ith window), we can get the best possible value of a j selection for window i
            for j in range( k*i, len(sums)+k ):           
                curSum = sums[j - k] + dp[i - 1][j - k]
                if curSum > dp[i][j-1]:
                    dp[i][j] = curSum
                    locs[i][j] = j-k
                else:
                    dp[i][j] = dp[i][j-1]
                    locs[i][j] = locs[i][j-1]

        # Reconstruct the final answer. The bottom right element of dp will have the best value we can get,
        # and the the bottom right element of loc has the index of the requisite selection for the last window
        # Therfore, if we check that spot in the second to last level, we can get the element we must select
        # for that level to maximize the sum, and so on.
        nxt = len(nums)
        res = [0]*numWindows
        for i in range( numWindows, 0, -1):
            res[i-1] = locs[i][nxt]
            nxt = res[i-1]

        return res