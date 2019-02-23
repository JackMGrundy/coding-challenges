"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

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
from itertools import combinations

nums = [-1, 0, 1, 2, -1, -4]

# 1st attempt: timeout : (  passed 311/313 tests.
# Too slow becase of A) use of set to eliminate duplicates B) casting between tuples
# and lists C) "too brute force" with search for 2nd and 3rd elements of tuple...
# processing duplicate elements
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        # Horrible code...but fun to fit in one line
        res = [ list(x) for x in { 
                        ( lagVal, nums[leadI], 0-lagVal-nums[leadI] ) 
                        for lagI, lagVal in enumerate(nums) 
                        for leadI in range(lagI+1, len(nums)) 
                            if 0-lagVal-nums[leadI] in nums[(leadI+1):] } ]

        # Equivalent code that is actually readablebut spread over ~10 lines
        # res = set()
        # for lagI, lagVal in enumerate(nums):
        #     for leadI in range(lagI+1, len(nums)):
        #         leadVal = nums[leadI]
        #         target = 0 - lagVal - leadVal
        #         if target in nums[(leadI+1):]:
        #             res.add( tuple( [lagVal, leadVal, target] ) )
        
        # res = [ list(x) for x in res ]
        return(res)




# 2nd attempt: ~480ms 97.5th percentile. Fixed problems above.
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1] or nums[i]>0:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([ nums[i], nums[l], nums[r] ])
                    while l<r and nums[l]==nums[l+1]:
                        l += 1
                    while l<r and nums[r]==nums[r-1]:
                        r -= 1
                    l, r = l+1, r-1
        
        return(res)




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
        if 0 in counts and counts[0]>=3:
            res.append( [0, 0, 0] )
        
        # All other possible tuples
        for posEle in pos:
            for negEle in neg: 
                thirdEle = 0-posEle-negEle
                if thirdEle in counts:
                    # Tuples with 2 of the same
                    if (thirdEle == posEle or thirdEle == negEle) and counts[thirdEle]>=2:
                        res.append( [ posEle, negEle, thirdEle ] )
                    #Tuples with all different
                    elif negEle < thirdEle < posEle:
                        res.append( [ posEle, negEle, thirdEle ] )
                    if thirdEle < negEle:
                        break
        
        return(res)