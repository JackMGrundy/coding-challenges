"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""
# 40ms. 84th percentile.
# Faster solutions opted for built ins like sorted that are symptotically O(Nlog(N)) rather than O(N).
"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""


"""
Method 1:
Seems cheap to me, but you can modify the array and technically only use "extra" constant space. 

Key bits of intuition:
If the min positive value is greater than 1, you instantly know 1 is the answer

Let's say you were allowed to use extra space. You might just put the positive values
in a set and then go through the natural numbers checking for the missing one.

You basically do that here but the array itself is the hash table (set whatever). When you see
a value, you just stick it in its spot (i.e. item 3 goes in index 3). Then you can
run through the array and find the missing value. If you get through the whole thing and don't see
a missing value, then the next missing value is on the max end (we already checked the min end with the 1 bit)

Note that if you see a value bigger than the size of the array you can just ditch it. To see this imagine a 5 spot
array, assuming it's not 1, the missing value must be between 2 or 6. It can't be 7 because there are only 5 spots
for values. Any we'll know its 6 if values 1 to 5 check out. 
"""

# 36ms. 97 percentile.
# Faster solutions opted for built ins like sorted that are symptotically O(Nlog(N)) rather than O(N).
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums or 1 not in nums:
            return 1
        
        nums = [0] + nums
        
        for i,num in enumerate(nums):
            if num == i:
                continue
            elif num < 0:
                nums[i] = -1
            else:
                nums[i] = -1
                while 0 < num < len(nums) and nums[num] != num:
                    nums[num], num  = num, nums[num]
        
        for i,num in enumerate(nums):
            if num == -1:
                return i
        
        return len(nums)

"""
Notes:


Method 1:
Seems cheap to me, but you can modify the array and technically only use "extra" constant space. 

Key bits of intuition:
If the min positive value is greater than 1, you instantly know 1 is the answer

Let's say you were allowed to use extra space. You might just put the positive values
in a set and then go through the natural numbers checking for the missing one.

You basically do that here but the array itself is the hash table (set whatever). When you see
a value, you just stick it in its spot (i.e. item 3 goes in index 3). Then you can
run through the array and find the missing value. If you get through the whole thing and don't see
a missing value, then the next missing value is on the max end (we already checked the min end with the 1 bit)

Note that if you see a value bigger than the size of the array you can just ditch it. To see this imagine a 5 spot
array, assuming it's not 1, the missing value must be between 2 or 6. It can't be 7 because there are only 5 spots
for values. Any we'll know its 6 if values 1 to 5 check out. 


Time complexity: O(N) considering we just walk the array...we use constant extra space.
"""