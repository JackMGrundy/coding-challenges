"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

Accepted
130.3K
Submissions
808K
"""
"""
y = mx + b
b = y  - mx
"""

# With math.gcd: 56ms. 95 percentile.
# With euclidean algo: 76ms. 76 percentile. 
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        :type points: List[List[int]]
        :rtype: int
        """
        """
        Line is defined by any two points.
        Three points lie on the same line if their slopes are same.        
        """
        if len(points) <= 2:
            return len(points)

        maxpoints = 0
        
        for i1, [x1, y1] in enumerate(points):
        
            lines = collections.defaultdict(int)
            copiesOfPoint1 = 1 # how many points are there with point1's values
            
            for [x2, y2] in points[i1+1:]:

                if x1 == x2 and y1 == y2:
                    copiesOfPoint1 += 1
                else:
                    dx = (x2-x1)
                    dy = (y2-y1)
                    sign = 0 < dx*dy

                    gcd = math.gcd(dy, dx)
                    # gcd = self._gcd(dy, dx)
                    dx //= gcd
                    dy //= gcd
    
                    lines[(abs(dx), abs(dy), sign)] += 1
            
            localmax = max(lines.values(), default=0) + copiesOfPoint1
            maxpoints = max(localmax, maxpoints)

        return maxpoints

    @lru_cache(maxsize=None)
    def _gcd(self, A, B):
        if B == 0:
            return A
        else:
            return self._gcd(B, A % B)




"""
Notes:

Gem of a problem.


1) Standard way to do this, which requires coming up with representations of lines that we can store
We're going to have to examine all N^2 pairs of points no matter what. We could generate all N^2 lines at the beginning, but to save
space we instead build up a list of lines for each point one at a time.

For each point:
    Start a dictionary of lines formed between this point and others
    Also start a counter of how many copies of this point we wee

    Iterate through the other points:

        If we're examining identical points
            Record that by incrementing the counter
        Else:
            The points are different. Get the rise and run difference. Also get the sign of the slope.
            Then a cool bit - using a double as a kep is a bad idea...so we can't store rise/run as part of the key indicating the
            line. Instead we need to reduce the rise / run fraction.

            To do that, we need to find the GCD. Given that, we can simply divide rise and run by the GCD.

            To find the GCD, we use the nifty Eucliden algo. See notes on Euclidean algo for details.

            At that point we can simply store the line if we haven't seen it before, or increment the number of points on the line if we have seen it before.

        After we finish iterating over the points, we update the best we've seen...this will be equal to the number of points we found on the same line plus
        the copies of point 1 we saw

        Note its easier to check for a new best answer after looping through the other points...we might just see duplicates for the entire list, in which case
        trying to index into lines would throw an error.
"""