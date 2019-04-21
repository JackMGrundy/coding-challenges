"""
There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.

Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.

Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is k and these flowers are not blooming.

If there isn't such day, output -1.

Example 1:
Input: 
flowers: [1,3,2]
k: 1
Output: 2
Explanation: In the second day, the first and the third flower have become blooming.
Example 2:
Input: 
flowers: [1,2,3]
k: 1
Output: -1
Note:
The given array will be in the range [1, 20000].
"""
# 1st attempt: 5th percentile
# Brute force. O(N^2)
class Solution:
    def kEmptySlots(self, flowers: List[int], k: int) -> int:
        statuses = [False]*(len(flowers)+1)
        
        for day, bloomPosition in enumerate(flowers, 1):
            statuses[bloomPosition] = True
            # Left
            if bloomPosition-k-1 > 0 and statuses[bloomPosition-k-1]==True:
                if not any(statuses[bloomPosition-k:bloomPosition]):
                    return day            
            # Right
            if bloomPosition+k+1 <= len(flowers) and statuses[bloomPosition+k+1]==True:
                if not any(statuses[bloomPosition+1:bloomPosition+k+1]):
                    return day 
        
        return -1


# 2nd attempt: 62nd percentile in speed
"""
O(Nlog(N))
As the flowers bloom, insert them into a list. We can do each insertion in log(n) time.
Doing N insertions total -> NLog(N) complexity.
After each insertion, check the distance between the new flower and its neighbors
"""
from bisect import bisect
class Solution:
    def kEmptySlots(self, flowers: List[int], k: int) -> int:
        bloomed = []
        for day, flower in enumerate(flowers, 1):
            i = bisect(bloomed, flower)
            for x in bloomed[i-(i>0):i+1]:
                if abs(flower-x)-1==k:
                    return day
            bloomed.insert(i, flower)
        return -1
                
# 3rd attempt: 9th percentile in speed
"""
Sliding window approach
Really burns...thought this would be fast a O(N) solution.
"""
from collections import deque
class MinQueue(deque):
    def __init__(self):
        deque.__init__(self)
        self.mins = deque()
    
    def append(self, x):
        deque.append(self, x)
        while self.mins and x < self.mins[-1]:
            self.mins.pop()
        self.mins.append(x)
    
    def popleft(self):
        x = deque.popleft(self)
        if self.mins[0] == x:
            self.mins.popleft()
        return x
    
    def min(self):
        return self.mins[0]

class Solution:
    def kEmptySlots(self, flowers: List[int], k: int) -> int:
        days = [0]*(len(flowers)+2)
        for day, flower in enumerate(flowers, 1):
            days[flower] = day
        days[0] = days[len(flowers)+1] = float("inf")
        window = MinQueue()
        ans = len(days)
        e = len(days)-1
        
        for i, day in enumerate(days[1:e], 1):
            window.append(day)
            if k <= i < len(days):
                if k==0 or days[i-k] < window.min() > days[i+1]:
                    ans = min(ans, max(days[i-k], days[i+1]))
                window.popleft()
        
        return ans if ans < len(days) else -1



# 4th attempt: 89th percentile in speed
"""
This problem confuses me...
This is so much faster, but I would think it would be O(N^2)
We iterate through each of the flowers, we record if they've bloomed,
and then we check for a solution...that consists of making sure neither is out 
of bounds, that its partner has bloomed, and that no flowers in the middle have bloomed.
...looks like the constant time speedup from using the set made it fast...
has bloomed,
"""
class Solution:
    def kEmptySlots(self, flowers: List[int], k: int) -> int:
        bloomed = set()
        
        def check(start, end):
            if start < 1 or end > len(flowers):
                return False
            if start not in bloomed or end not in bloomed:
                return False
            for i in range(start+1, end):
                if i in bloomed:
                    return False
            return True
        
        for day, flower in enumerate(flowers):
            bloomed.add(flower)
            if check(flower, flower+k+1) or check(flower-k-1, flower):
                return day+1
        return -1