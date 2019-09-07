"""
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

 

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 

Note:

1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000
"""
# 44ms. 91st percentile. 
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[1]-x[0]) # Sort by "cost" of sending to A rather than B.  
        total = 0
        for i in range(len(costs)//2):
            total += costs[-i-1][0] + costs[i][1]
        
        return total
                
"""
Notes

This is a greedy problem. 
Key idea: for each person, we can calcualte a cost of sending them to A rather than B by taking costB - costA. If the cost
of sending them to B is higher than A, then this will be positive, indicating they gain something by sending them to
A instead. Sorting ascending by this metric will place the highest value "A" decisions at the end. On the other hand,
the benefit of sending someone to B is -(costB - costA). So the negative values that end up at the start of the list
are the highest earners for sending someone to B. 
"""