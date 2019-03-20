"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
# 1st attempt: 17th percentile in speed. 
#  Slow, but collects the actual best range, not just the max product as required.
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return None
        if len(nums)==1: return nums[0]
        
        # First row is most extreme (positive or negative) value, second
        # is start (inclusive) of range, and thid is end (inclusive)
        minDp = [ [ None, 0, 0 ] for _ in range(len(nums)) ]
        maxDp = [ [ None, 0, 0 ] for _ in range(len(nums)) ]
        
        def updateCol(arr, col, val, start, finish):
            arr[col][0] = val
            arr[col][1] = start
            arr[col][2] = finish        
        
        if nums[0]==0:
            minDp[0][0] = 0
            maxDp[0][0] = 0
        elif nums[0]<0:
            minDp[0][0] = nums[0]
        elif nums[0]>0:
            maxDp[0][0] = nums[0]
        
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            if num==0:
                updateCol(minDp, i, 0, i, i)
                updateCol(maxDp, i, 0, i, i)
            
            # Next num is negative
            elif num<0:
                # Update negative 
                
                # We do not have a previous positive
                if maxDp[i-1][0] in [ None, 0 ]:
                    updateCol(minDp, i, num, i, i)
                # We do have a previous positive
                else:
                    updateCol(minDp, i, num*maxDp[i-1][0], maxDp[i-1], i)
                
                # Update positive
                
                # We do not have a previous negative
                if minDp[i-1][0] == None:
                    updateCol( maxDp, i, None, i, i )
                elif minDp[i-1][0] == 0:
                    updateCol( maxDp, i, 0, maxDp[i-1][1], i )
                else:
                    updateCol( maxDp, i, num*minDp[i-1][0], minDp[i-1][1], i )
            
            elif num>0:
                
                # Update negative
                
                # We do not have a previous negative
                if minDp[i-1][0] == None:
                    updateCol( minDp, i, None, i, i )
                elif minDp[i-1][0] == 0:
                    updateCol( minDp, i, 0, minDp[i-1][1], i )
                else:
                    updateCol( minDp, i, num*minDp[i-1][0], minDp[i-1][1], i )
                
                # Update positive
                
                # We do not have a previous positive
                if maxDp[i-1][0] in [ None, 0 ]:
                    updateCol(maxDp, i, num, i, i)
                else:
                    updateCol(maxDp, i, num*maxDp[i-1][0], maxDp[i-1][1], i )
        
        res = -float("inf")
        for i in range(len(nums)):
            if maxDp[i][0]!=None and maxDp[i][0] > res:
                res = maxDp[i][0]
        
        return res



# 2nd attempt: 52nd percentile in speed.
# Same as above, but collects only the max product. O(N) in space.
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return None
        if len(nums)==1: return nums[0]
        
        # First row is most extreme (positive or negative) value, second
        # is start (inclusive) of range, and thid is end (inclusive)
        minDp = [ None for _ in range(len(nums)) ]
        maxDp = [ None for _ in range(len(nums)) ]
        
        if nums[0]==0:
            minDp[0] = 0
            maxDp[0] = 0
        elif nums[0]<0:
            minDp[0] = nums[0]
        elif nums[0]>0:
            maxDp[0] = nums[0]
        
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            if num==0:
                minDp[i] = 0
                maxDp[i] = 0
            
            # Next num is negative
            elif num<0:
                # Update negative 
                
                # We do not have a previous positive
                if maxDp[i-1] in [ None, 0 ]:
                    minDp[i] =  num
                # We do have a previous positive
                else:
                    minDp[i] = num*maxDp[i-1]
                
                # Update positive
                
                # We do not have a previous negative
                if minDp[i-1] == None:
                    maxDp[i] = None
                elif minDp[i-1] == 0:
                    maxDp[i] = 0
                else:
                    maxDp[i] = num*minDp[i-1]
            
            elif num>0:
                
                # Update negative
                
                # We do not have a previous negative
                if minDp[i-1] == None:
                    minDp[i] =  None
                elif minDp[i-1] == 0:
                    minDp[i] = 0
                else:
                    minDp[i] =  num*minDp[i-1]
                
                # Update positive
                
                # We do not have a previous positive
                if maxDp[i-1] in [ None, 0 ]:
                    maxDp[i] = num
                else:
                    maxDp[i] = num*maxDp[i-1]
        
        res = -float("inf")
        for i in range(len(nums)):
            if maxDp[i]!=None and maxDp[i] > res:
                res = maxDp[i]
        
        return res




# 3rd attempt: 95th percentile in speed
# Cleaned up further. Uses constant space now. Shorter. Single pass...O(N) speed
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return None
        if len(nums)==1: return nums[0]
        
        res = nums[0]
        curPos = curNeg = None
        prevPos = nums[0] if nums[0] >= 0 else None
        prevNeg = nums[0] if nums[0] <= 0 else None

        for num in nums[1:]:
            if num==0:
                curNeg = curPos = 0
                
            # Next num is positive
            elif num<0:
                # Update positive nums
                if prevPos in [ None, 0 ]:
                    curNeg =  num
                else:
                    curNeg = num*prevPos
                # Update negative nums
                if prevNeg == None:
                    curPos = None
                else:
                    curPos = num*prevNeg
                    
            # Next num is negatvie
            elif num>0:
                # Update positive nums
                if prevNeg == None:
                    curNeg =  None
                else:
                    curNeg =  num*prevNeg
                # Update negative nums
                if prevPos in [ None, 0 ]:
                    curPos = num
                else:
                    curPos = num*prevPos
            
            # Check for new best answer
            if curPos != None and curPos > res:
                res = curPos
            
            # Prepare for next loop
            prevNeg, prevPos = curNeg, curPos
        
        return res


# 4th attempt: 75th percentile in speed. 
# Not sure why this is slower. Tried to simplify above while keeping same strategy and speed.
# A single pass, constant space,
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return None
        if len(nums)==1: return nums[0]
        
        curMin = curMax = absMin = absMax = nums[0]

        for num in nums[1:]:
            
            if num < 0: curMin, curMax = curMax, curMin
            
            curMin = min( num, num*curMin)
            curMax = max( num, num*curMax)
            
            absMin = min( curMin, absMin )
            absMax = max( curMax, absMax )
            
        return absMax



# 5th attempt: Also 95th percentile in speed. Favorite answer
# Cons: two passes instead of 1 (still O(N) speed) and O(N) space instead of constant
# Pros: very short and concise

# Intuition: say you have a string of numbers with a single negative in the middle. You are going to achieve
# a max sum by multiplying up to that negative on either the left side or the right side.
# Now say there are two negatives. Assuming there are positives on either side of the array, you cannot achieve a 
# max between the negatives (it will be less than 0). However, assuming you multiply through both of them, it's as 
# though they are positive. Therefore, the max will be achieved by multiplying all of the numbers.
# Say you have three negatives. This is a combination of the first two scenarios. Using all 3 in a product sticks you with
# a negative number. However, taking a product the involes the first two or the last two will yield the largest number.
# In all three of these series, if you multiply through from both the left and right side, you're guaranteed to hit
# the max product along the way.

# This implication holds for 4 negatives, 5, and so (you can make an inductive argument). So it always holds. 

# The last complication is 0's. These basically just break the problem into a series if subproblems that still behave as described
# above. Therefore, multiplying through from either direction is guaranteed to yield a max answer somewhere along the way. 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        reverse = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1
            reverse[i] *= reverse[i-1] or 1
        
        return( max( nums + reverse ))