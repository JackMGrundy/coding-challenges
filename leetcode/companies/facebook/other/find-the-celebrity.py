"""
"""
# Attempt 1: asymptotically coorect ( O(N) ). slow...10th percentile due to constant factors. Found it easier
# to maintain two pointers, one to the "candidate celeb" a and b to the "challenger". 
# Yields long code that's hard to read.
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0: return(-1)
        if n==1: return(0)
        a = 0; b = 1
                
        while b <n: #TODO
            aToB = knows(a, b)
            bToA = knows(b, a)
            # They know each other -> neither are a celebrity
            # They don't know each other -> neither are a celebrity
            if aToB == bToA:
                a = b+1
                b += 2
            # Only a knows b
            elif aToB:
                temp = b+1
                a = b
                b = temp
            # Only b knows a
            elif bToA:
                b += 1
        
        if a >= n: return(-1)
        
        for i in range(n):
            if i==a: continue
            if knows(i, a) and not knows(a, i):
                continue
            else:
                return(-1)
        
        return(a)


# Attempt 2: 98th percentile. Simplified logic to 1 pointer variable. Same key idea as above. 
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """      
        celeb = 0
        # First pass. If there is a celeb, we will definitely see them. 
        for i in range(1, n):
            if knows(celeb, i):
                celeb = i
        # At this point, we know everyone we saw after the celeb cannot be the celeb, because
        # the candidate celeb did not know them. Make sure the candidate celeb does not know all of the earlier people.
        for i in range(celeb):
            if knows(celeb, i):
                return(-1)
        # We know the candidate celeb knows no one. Make sure everyone knows the celeb.
        for i in range(n):
            if not knows(i, celeb):
                return(-1)
        
        return(celeb)