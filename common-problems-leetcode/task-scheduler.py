"""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

 

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 

Note:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
Accepted
82,242
Submissions
181,812
"""
# 43rd percentile. 228ms
# programmatically
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        res = 0
        while counts:
            mosts = counts.most_common()
            padding = max(0, n-len(mosts)+1)
            
            for i in range(0, min(len(mosts), n+1)):
                key, val = mosts[i]
                counts[key] = val-1
                if counts[key]==0:
                    del counts[key]
                res += 1
            
            if counts:
                res += padding
        
        return res

# 95th percentile. 56ms
# math...
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        biggest = counts.most_common(1)[0][1]
        countBiggest =list(counts.values()).count(biggest)
        res = max( (biggest-1)*(n+1)+countBiggest, len(tasks))
        return res
