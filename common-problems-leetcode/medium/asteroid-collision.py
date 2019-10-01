"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its 
direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the 
smaller one will explode. If both are the same size, both will explode. Two asteroids 
moving in the same direction will never meet.

Example 1:
Input: 
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation: 
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.


Example 2:
Input: 
asteroids = [8, -8]
Output: []
Explanation: 
The 8 and -8 collide exploding each other.


Example 3:
Input: 
asteroids = [10, 2, -5]
Output: [10]
Explanation: 
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.


Example 4:
Input: 
asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation: 
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each other.
Note:

The length of asteroids will be at most 10000.
Each asteroid will be a non-zero integer in the range [-1000, 1000]..
"""
# 108ms. 94 percentile.
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for a in asteroids:
            while result and a < 0 < result[-1]:
                if -a == result[-1]:
                    result.pop()
                    break
                elif -a > result[-1]:
                    result.pop()
                    continue
                break
            else:
                result.append(a)
        return result

    
    """
    [3, 1, 2, -2, -1]
    
    
    """

"""
Notes:

a < 0 < result[-1] tells you if there is a collision
Logic:

whil we have asteroids and the new one will collide with the last old one
    if the last asteroid is of equal size to the new one, pop it to eliminate it. End the loop

    if the last asteroid is of smaller size than the new one, pop it, and keep looping

    Else:
        This includes the case where the old asteroid is of bigger size than the new one.
        In this case the old asteroid just clobbers the one. Break the loop.


Syntax:
The else clause is only executed when your while condition becomes false. 
If you break out of the loop, or if an exception is raised, it won't be executed.

"""