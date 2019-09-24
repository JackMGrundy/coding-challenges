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
# 220ms. 76th percentile.
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == len(self.maxHeap):
            heapq.heappush(self.minHeap, -heapq.heappushpop(self.maxHeap, -num))
        else:
            heapq.heappush(self.maxHeap, -heapq.heappushpop(self.minHeap, num))

    def findMedian(self) -> float:
        if 0 == len(self.minHeap) == len(self.maxHeap):
            return None
        elif len(self.minHeap) == len(self.maxHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        else:
            return self.minHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# 256ms. 22nd percentile. Use builtin bisect library 
# class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.values, num)

    def findMedian(self) -> float:
        return (self.values[len(self.values)//2] + self.values[~len(self.values)//2]) / 2.0 

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


"""
Notes:


1) Simple brute force, built in answer
Just maintain a list. Use bisect to insert new values. Averaged together the 
list[len//2] and list[~(len//2)] values...done


Time complexity...at first glance seems like this only takes log(N) time, since that's
how long binary search takes. It actually depends on what data structures you're using though.
With a list, you'd have to shift at most O(N) elements over to make room for the new element.
If you're using something like a linkedlist though, then you can insert in constant time. 




2) The "correct" answer
The key is to use two heaps. As long as we maintain the invariant that they differ in size
by at most one and that all values in one heap are less than all the values int the other heap,
then we can quickly get the median at will. 



Min heap  <- contains the "big" values

Median

Max heap <- contains the "small" values


We're adding a new value. Here are the cases:

1) Heaps are the same size
    Add the val to the max heap. Heapify it. Transfer the biggest value to the min heap.
    Why does this work? 
    We know that before we added the value, all the values in the max heap
    were smaller than all the values in the min heap.
    If the newly added value is big enough to belong in the min heap, it must bubble to the top then,
    and it'll end up in the right place. Otherwise, we're just adding the biggest value in the max
    heap to the min heap...This just makes the minheap the heap that is one bigger in size.

2) The heaps are of different sizes
    Add the val to the min heap. heapify it. transfer the smalelst value in the min heap over to
    the max heap.
    Why does this work?
    By design, we're ensuring that every time the heaps are of differing sizes, its the min heap that is the
    bigger one. 
    Immediately after we add the new value to the min heap, it will be 2 bigger than the max heap. After we
    transfer the smallest value over, they will be of the same size. If the new value is small enough 
    to belong in the max heap, then it will bubble to the top (bottom?) of the min heap and be transferred over.

Finding the median:
    If the heaps are the same size:
        simply take the average of their offered values
    else:
        take the offered value of the min heap...we've designed this so that if there are an odd number
        of values, the min heap will always be the bigger heap. 


Time complexity: O(log(N))...heap insertions take at worst log(N) time
"""