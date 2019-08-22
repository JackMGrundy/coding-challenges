""" 
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
""" 


# 68ms. 98th percentile.
from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.average = 0.0
        self.queue = deque([])

    def next(self, val: int) -> float:
        currentValue = self.average*len(self.queue)
        removed = 0
        if len(self.queue) == self.size:
            removed = self.queue.popleft()
        self.queue.append(val)
        
        self.average = (currentValue + val - removed) / len(self.queue)
        return self.average


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)