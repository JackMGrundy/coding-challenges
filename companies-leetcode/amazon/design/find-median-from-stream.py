"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""
# First attmempt: 78th percentile in speed. Unnecessarily long
import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)
        self.median = 0
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """

        #Case 1
        if len(self.minHeap)==len(self.maxHeap) and num>self.median:
            self.addToMinHeap(num)
        
        #Case 2
        elif len(self.minHeap)==len(self.maxHeap) and num<=self.median:
            self.addToMaxHeap(num)

        #Case 3
        elif len(self.minHeap)>len(self.maxHeap) and num<=self.median:
            self.addToMaxHeap(num)
        
        #Case 4
        elif len(self.maxHeap)>len(self.minHeap) and num>self.median:
            self.addToMinHeap(num)
        
        #Case 5
        elif len(self.minHeap)>len(self.maxHeap) and num>=self.median:
            temp = heapq.heappop(self.minHeap)
            self.addToMinHeap(max(temp, num))
            self.addToMaxHeap(min(temp, num))
        
        #Case 6
        elif len(self.minHeap)<len(self.maxHeap) and num<=self.median:
            temp = -heapq.heappop(self.maxHeap)
            self.addToMaxHeap(min(temp, num))
            self.addToMinHeap(max(temp, num))       

        self.median = self.findMedian()
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.minHeap)==0 and len(self.maxHeap)==0:
            return(None)

        elif len(self.minHeap)==len(self.maxHeap):
            med = ( self.minHeap[0] + (-self.maxHeap[0]) )/2.0
            return(med)
        
        elif len(self.minHeap)>len(self.maxHeap):
            return(self.minHeap[0]*1.0)
        
        elif len(self.minHeap)<len(self.maxHeap):
            return(-self.maxHeap[0]*1.0)
        
    
    def addToMaxHeap(self, num):
        heapq.heappush(self.maxHeap, -num)
    
    def addToMinHeap(self, num):
        heapq.heappush(self.minHeap, num)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()






# Attempt 2: 78th percentile in speed. 
# Simplify to only 2 cases. If the two heaps are equal in size,
# Add to the min heap. If they are not equal, then the minheap must have
# 1 more than the max heap. Transfer a value to the max heap.


from heapq import heappush, heappushpop

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []
        self.median = 0
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.minHeap)==len(self.maxHeap):
            heappush(self.minHeap, -heappushpop(self.maxHeap, -num))
        else:
            heappush(self.maxHeap, -heappushpop(self.minHeap, num))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.minHeap)==0 and len(self.maxHeap)==0:
            return(None)
        elif len(self.minHeap)==len(self.maxHeap):
            return( (-self.maxHeap[0]+self.minHeap[0]) / 2.0 )
        else:
            return(self.minHeap[0]*1.0)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()




# Attemp 3: 98th percentile. Use builtin bisect library
from bisect import insort

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        insort(self.values, num)

    def findMedian(self):
        """
        :rtype: float
        """
        res = self.values[len(self.values)//2]*1.0
        if len(self.values)%2==0:       
            res += self.values[len(self.values)//2 - 1]  
            res /= 2.0
        return(res)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()





# Attempt 4: 98th percentile. Use builtin bisect library. Cleanup up with ~ trick. 
from bisect import insort

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        insort(self.values, num)

    def findMedian(self):
        """
        :rtype: float
        """
        res = ( self.values[len(self.values)//2] + self.values[~len(self.values)//2] ) / 2.0
        return(res)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()