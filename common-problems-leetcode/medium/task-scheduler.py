"""
Given  a  char  array  representing  tasks  CPU  need to do. It contains capital
letters A to Z where different letters represent different tasks. Tasks could be
done  without  original order. Each task could be done in one interval. For each
interval, CPU could finish one task or just be idle.                            

However,  there is a non-negative cooling interval n that means between two same
tasks,  there must be at least n intervals that CPU are doing different tasks or
just be idle.                                                                   

You need to return the least number of intervals the CPU will take to finish all
the given tasks.                                                                


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
# 37rd percentile. 636ms
# programmatically
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounts = collections.Counter(tasks)
        cpuIntervals = 0
        
        while taskCounts:
            tasksMostCommonToLeast = taskCounts.most_common()
            numTasksLeftInCycle = n+1
            
            for task in tasksMostCommonToLeast:
                taskName, taskCount = task
                taskCounts[taskName] -= 1
                if taskCounts[taskName] == 0:
                    del taskCounts[taskName]
                numTasksLeftInCycle -= 1
                cpuIntervals += 1
                if numTasksLeftInCycle == 0:
                    break
                
            if taskCounts:
                cpuIntervals += numTasksLeftInCycle
        
        return cpuIntervals


# 95th percentile. 424ms
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = collections.Counter(tasks)
        maxFrequency = frequencies.most_common(1)[0][1]
        numTasksWithMaxFrequency = sum([ 1 for task in frequencies if frequencies[task] == maxFrequency ])
        cycleLength = n + 1
        
        return max(cycleLength*(maxFrequency - 1) + numTasksWithMaxFrequency, len(tasks))
 
"""
Notes:

Easiest way to think about it:                                                  

We  don't  really care about the names of the tasks, just how many there are. If
the  cool  down  period  is  1,  That means for each cycle, we'll ideally have 2
different elements...so we can do something like A B A D B...just making sure we
don't have repeats.                                                             

When  we have a greater variety of elements it's easier to accomplish this. As a
result, scarcer elements are relatively more valuable than more common ones.    

In each cycle, we want to use up the most common elements first.                

One  way  to  do  this, is to sort the elements by frequency at the beginning of
each cycle we are constructing.                                                 

Smarter way to think about it:                                                  

A full cycle is n+1 (say n == 1, we need 1+1 = 2 elements to refresh).          

We can split all scenarios into two buckets:                                    

1)  We  have enough variety in tasks that the cooldown period is never an issue.
In this case, the answer is simply the total number of tasks                    

2)  We  have  tasks  with  such high frequencies, that after making as many full
tasks  as  we  can,  we  still  have  some  of them left over. In this case, the
limiting  factor  isn't  the  total  number  of  tasks,  rather  its the highest
frequency  tasks.  We'll  need  at least cycle-length * frequency of most common
task.  There's  only  one last thing to consider here. Say we only have one task
with  the  max  occurrence. The total number of tasks+cooldown periods completed
isn't  actually  cycle-length  *  frequency...the  last "cycle" will look like A
coolDown  coolDown...but  in  this  case  the  two  coolDown periods don't count
because  we're  done.  Further,  say we had two tasks that had the max number of
occurrences,  then  the  last cycle would look like A B cooldown (where we again
don't count that last cooldown).                                                

As  a  result,  the  full numbers of tasks completed is actually (cycle-length *
(maxFrequency-1)) + counts of elements with max frequency                       

"""