"""
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
Accepted
22,477
Submissions
56,256
"""
# 99th percentile. 116ms.
import heapq
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.heap = []
        self.stackPoppedIds = set()
        self.heapPoppedIds = set()
        self.nextId = 0

    def push(self, x: int) -> None:
        self.stack.append( (x, self.nextId) )
        # Heapq defaults to min priority queue. Negative produces a max priority queue
        heapq.heappush( self.heap, (-x, self.nextId) )
        # Negative ids because heap will use ids to break tie in case values are equal.
        # Smaller ids win. So newer elements will have smaller elements and be selected first.
        self.nextId -= 1

    def pop(self) -> int:
        x, poppedId = self.stack.pop()
        while poppedId in self.heapPoppedIds:
            x, poppedId = self.stack.pop()
        self.stackPoppedIds.add(poppedId)
        return x

    def top(self) -> int:
        x, poppedId = self.stack[-1]
        while poppedId in self.heapPoppedIds:
            self.stack.pop()
            x, poppedId = self.stack[-1]
        return x

    def peekMax(self) -> int:
        x, poppedId = self.heap[0]
        while poppedId in self.stackPoppedIds:
            heapq.heappop(self.heap)
            x, poppedId = self.heap[0]
        return -x

    def popMax(self) -> int:
        x, poppedId = heapq.heappop(self.heap)
        while poppedId in self.stackPoppedIds:
            x, poppedId = heapq.heappop(self.heap)
        self.heapPoppedIds.add(poppedId)
        return -x


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()