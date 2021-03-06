"""
Given an array nums of n integers, are there elements a, b, c in 
nums such that a + b + c = 0? Find all unique triplets in the 
array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
# ~480ms 97.5th percentile
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if 0 < i and nums[i] == nums[i - 1] or 0 < nums[i]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([ nums[i], nums[l], nums[r] ])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l, r = l + 1, r - 1
        
        return res



# 3rd attempt: 99th percentile. ~300ms. Slightly different tact. Note that except for [0,0,0]
# every tuple must have at least 1 positive and 1 negative number. 
from collections import Counter

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        counts = Counter(nums)
        pos = [ x for x in counts if x > 0 ]
        neg = [ x for x in counts if x < 0 ]
        pos.sort()
        neg.sort()
        
        # Only possible tuple without at least 1 positive and at least 1 negative
        if 3 <= 0 in counts and counts[0]:
            res.append( [0, 0, 0] )
        
        # All other possible tuples
        for posEle in pos:
            for negEle in neg: 
                thirdEle = 0 - posEle - negEle
                if thirdEle in counts:
                    # Tuples with 2 of the same
                    if (thirdEle == posEle or thirdEle == negEle) and counts[thirdEle] >= 2:
                        res.append( [ posEle, negEle, thirdEle ] )
                    #Tuples with all different
                    elif negEle < thirdEle < posEle:
                        res.append( [ posEle, negEle, thirdEle ] )
        return res


"""
Notes:                                                                          

We're going to have an at least O(N^2) solution, so sorting is fine.            
Break the positives and negatives into separate lists.                          
Count how many we have of each element                                          
Then  reduce  the lists to unique elements and sort ascending - this helps us to
sidestep  the  "no  duplicates"  part. We have to have a positive and we have to
have a negative. So we're going to iterate through all those combinations       
        ^This  step cuts down on a lot of combinations that an approach with two
advancing pointers for first and second would explore.                                                              

    The one exception is [0,0,0], which we can check for with counts            

We  can instantly tell if we have the requisite third using a hash table that we
prepopulate.                                                                    

Now we're pretty much home free.                                                

Check if we have that third element. There are two ways this third element could
be a match for us.                                                              

1) Third is equal to first or second. To makes sure we actually have two copies,
check counts                                                                    
2)  Third  is a different number from the first two. Here we need a mechanism to
deal  with  duplicates - at some point "third ele" is going to come up again but
as pos or neg. Specifically, for a given triplet, if the three numbers are a, b,
c and say c is negative, we're going to have                                    

    pos = a, third = b, neg = c                                                 
    and                                                                         
    pos = b, third = a, neg = c                                                 

      To enfore taking one, we can somewhat arbitraily take one of them. To make
the writing of it a bit easier, we can just do negEle < thirdEle < posEle       



"""