"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
"""

# Note, instructions are not clear about this, but it's possible all versions have been bad

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# 1st attempt: 100th percentile in speed. 50th percentile in space.
# use binary search to find the cell where 
# either cell=Bad and next=Good or vice versa (2log(n) calls)
# def isBadVersion(x):
    # return() 

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1;  r = n
        m = (l+r)//2
        while l!=r:
            mBad = isBadVersion(m)
            mNeighBad = isBadVersion(m+1)
            if not mBad and mNeighBad:
                return(m+1)
            elif l==r-1 and mBad and mNeighBad:
                return(1)
            # good, good -> right
            elif not mBad and not mNeighBad:
                l = m+1
            # bad, bad -> left
            elif mBad and mNeighBad:
                r = m
            m = (l+r)//2
        
        return(n)


# 2nd attempt: 100th percentile in speed. 50th percentile in space
# clean up
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l<r:
            m = (l+r)//2
            if isBadVersion(m)==False:
                l = m+1
            else:
                r = m
        
        return l