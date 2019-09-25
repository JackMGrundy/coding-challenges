"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.

Accepted
193.9K
Submissions
672.2K
"""



"""
Notes:

You can get an O(N) solution. Here's the intuition. You march through the array. You hit a 
jump that looks very appealing...maybe a jump 5. Maybe that 5 takes you into a field of 1's. 
However, say the very next element is a 10 that leaps you over the field of 1's. This implies 
that it isn't ideal to be greedy and take the first "big" jump that comes along. However, after 
you get to the landing spot of the 5, you'll know if there was anything better along the way, so 
you can make an update to record what was the best opportunity. At that point you can increase 
the number of steps by 1 and set the "lastReach" to the farthest value you've reached.

So you keep track of the farthest reachable square as go along. Once you pass that square, you can 
update steps and lastReached. The thought process starting at the update step: "given elements 0 
to current, the farthest I can reach is lastReached and it takes me ___ steps to get there. 
lastReached is ahead of where I am now. I am going to march to that point. I know that I could 
stop at any spot on any square between now and then - lastReached is just the absolute farthest 
I could go if I wanted to. So I'm going to keep track of which of those squares gets me the 
farthest. Then, when I get to lastReached, I'll know the absolute farthest one extra step can 
take me after lastReached. Then I can update everything accordingly. Then repeat..."


[2,1,1,4,6,8,10,14...


[
step = 0
lastReach = 0
reach = 0



[2,
i = 0
step = 0
lastReach = 0
reach = 2


[2, 1,
i = 1
step = 1
lastReach = 2
reach = 2


[2,1,1
i = 2
step = 1
lastReach = 2
reach = 3


[2,1,1,4
i = 3
step = 2
lastReach = 3
reach = 7


[2,1,1,4,6
i = 4
step = 3
lastReach = 7
reach = 10


[2,1,1,4,6,8
i = 5
step = 3
lastReach = 7
reach = 13


[2,1,1,4,6,8,10
i = 6
step = 3
lastReach = 7
reach = 16


[2,1,1,4,6,8,10,12
i = 7
step = 3
lastReach = 7
reach = 19


[2,1,1,4,6,8,10,14
i = 8
step = 4
lastReach = 19
reach = 22


"""