"""
Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:

push(int x), which pushes an integer x onto the stack.
pop(), which removes and returns the most frequent element in the stack.
If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.
 

Example 1:

Input: 
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
Explanation:
After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

pop() -> returns 5, as 5 is the most frequent.
The stack becomes [5,7,5,7,4].

pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].

pop() -> returns 5.
The stack becomes [5,7,4].

pop() -> returns 4.
The stack becomes [5,7].
 

Note:

Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
It is guaranteed that FreqStack.pop() won't be called if the stack has zero elements.
The total number of FreqStack.push calls will not exceed 10000 in a single test case.
The total number of FreqStack.pop calls will not exceed 10000 in a single test case.
The total number of FreqStack.push and FreqStack.pop calls will not exceed 150000 across all test cases.
"""

# Gosh I love Python. So fast to get a decent solution thanks to all the built ins.
# O(1) for push and log(n) for pop
# 376ms. 58th percentile.
from heapq import *
class FreqStack:

    def __init__(self):
        self.heap = []
        self.counts = {}
        self.elementIndex = 0

    def push(self, x: int) -> None:
        self.counts[x] = 1 if x not in self.counts else self.counts[x]+1
        self.elementIndex += 1
        heappush(self.heap, (-self.counts[x], -self.elementIndex, x))

    def pop(self) -> int:
        _, _, res = heappop(self.heap)
        self.counts[res] -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()



# Constant time for push and pop
# 356ms. 86th percentile.
class FreqStack:

    def __init__(self):
        self.countToStack = {}
        self.elementToCount = {}
        self.maxCount = 0
        
    def push(self, x: int) -> None:
        self.elementToCount[x] = 1 if x not in self.elementToCount else self.elementToCount[x]+1
        self.maxCount = max(self.maxCount, self.elementToCount[x])
        
        if self.elementToCount[x] not in self.countToStack:
            self.countToStack[self.elementToCount[x]] = [x]
        else:
            self.countToStack[self.elementToCount[x]].append(x)
            
        
    def pop(self) -> int:
        maxStack = self.countToStack[self.maxCount]
        res = maxStack.pop()
        self.elementToCount[res] -= 1
        if not maxStack:
            del self.countToStack[self.maxCount]
            self.maxCount -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()