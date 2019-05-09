"""
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number 
(floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , 
where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there 
is no contradiction.

Accepted
76,685
Submissions
161,861
"""
# 79th percentile. 36ms. Feels good when it works on the first try.
# Likely longer than need be...but straightforwaord logic at leat
from collections import defaultdict
from collections import deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        letters = set()
        for eq in equations:
            A, B = eq
            letters.add(A)
            letters.add(B)
        
        # vals[ ("a", "b") ] = 3.0 -> a/b=3.0
        vals = defaultdict(list)
        denoms = defaultdict(list)
        for i in range(len(values)):
            A, B = equations[i]
            val = values[i]
            vals[ (A, B) ] = val
            vals[ (B, A) ] = 1.0/val
            denoms[A].append(B)
            denoms[B].append(A)
        
        res = []
        for query in queries:
            A, B = query
            if A not in letters or B not in letters:
                res.append(-1.0)
            elif A==B:
                res.append(1.0)
            # bfs to look for a solution
            else:
                q = deque()
                ans = -1.0
                for denom in denoms[A]:
                    q.append( ( denom, vals[ (A, denom) ] ) )
                visited = set([A])
                
                while q:
                    C, dist = q.popleft()
                    if C in visited:
                        continue
                    visited.add(C)
                    if C==B:
                        ans = dist
                        break
                    else:
                        for denom in denoms[C]:
                            q.append( (denom, dist*vals[ C, denom ]) )
                
                res.append(ans)
        
        return res