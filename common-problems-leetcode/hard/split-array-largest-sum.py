"""
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""

"""
Method 1: DP. 

Example
[7,2,5,10,8]

                          j = how many parts

	                 0       1       2      3      4     5
	 
	     0           ~		 ~		 ~		~	   ~	  ~

	     1 [7]       ~		 7       -      -      -      -
	     
i        2 [2]       ~		 9       7      -      -      -
Next
usable   3 [5]       ~		 14      7      7      -      - 
element	   
	     4 [10]      ~		 24     14     10     10      -
	 
	     5 [8]       ~		 32     18     14     10     10


^Note that in the implementation those 0's are actually infinity...but I like how i looks better with the ~'s. 


For each target square, iterate through the values in the column to the left of it up to the row above it.
For each current square, take the max of the current square and the difference of sum of the array up to the target squares 
index and the current squares index. Take the min of all of these values to determine the target square's value. 


Intuition via example:
Think of the j = 2 case.
In the max expression, the current square value will equal the sum of the array up to and including that square. 
The difference will give you the sum of all squares after the current square. In other words, you're literally 
taking the max of splitting the array into two different pieces. Simple enough.

Now consider going to j = 3.
Consider the i=5 j=3 space. Look at i=4 j=2 => 14. This tells you that with the first 4 elements and 2 parts, 
the best you can do is 14. Now our max equation says to take max(32-24, 14) = 14, which ends up being the value 
of i=5, j=3. Intuitively, we're just saying "this is a split that allocates 8 to the stuff after the i=1 to i=4 
section, in which the best we can do is 14. So effectively this solution yields a best value of 14."

In this way, for each additional split, we evaluate O(N) spots to find the best one. And because we evaluate 
m*n spots, our final solution is O(m*n)

Intuition more generally:
We have a certain number of splits that we can "use up". We can view our solution as being the max of "we use
all of our splits on the first part of the array and that yields some max subarray value in that section"
and "our last split produces a subarray from the split to the end of the array...that will have some vale".
This is optimal substructure with the non-aftereffect property...so we can use dp. The subproblem pertinent to the
current problem are the subproblems that comprise the first part of the max. 
"""
# Times out on the second to last test case.
# I'm pretty sure this is correct, but they want an even faster method.
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        dp = [ [float("infinity") for x in range(m+1)] for y in range(len(nums)+1) ]
        subSums = [ 0 for x in range(len(nums)+1)]
        for i, num in enumerate(nums):
            subSums[i+1] = subSums[i]+num
        
        dp[0][0] = 0
        for i in range(1, len(nums)+1):
            for j in range(1, m+1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j-1], subSums[i]-subSums[k]) )
        
        return dp[len(nums)][m]






"""
Method 2:
Binary search

Super super awesome idea that is surprisingly intuitive.

We have a 1 dimensional solution with clear limits. On the minimum end, the largest element is a valid bound 
(we could tighten this a bit but it's not worth the miniscule gain). On the max end, the sum of the elements
is a valid bound. 

We can test if a given value is valid by just linearly marching through the array; we build up a subarray until we 
couldn't add another value without breaking the bound. Then we start a new subarray. If we hit a point where we
"don't have any more splits" to use and we break the barrier, then we know that's not a valid answer.

Therefore, we can combine a binary search with this linear search to find the answer in O(Nlog(sum of elements))
time. Pretty awesome.
"""

# 36ms. 94th percentile. awesome. so simple.
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        l = max(nums)
        r = sum(nums)
        minSum = r
        
        while l < r:
            s = (l+r) // 2
            
            if self.sumIsValid(nums, s, m):
                minSum = min(minSum, s)
                r = s
            else:
                l = s+1
        
        return minSum
        
    
    
    def sumIsValid(self, nums, s, m):
        currentTotal = 0
        for num in nums:
            if currentTotal + num <= s:
                currentTotal += num
            else:
                m -= 1
                currentTotal = num
                if m == 0:
                    return False
        
        return True
