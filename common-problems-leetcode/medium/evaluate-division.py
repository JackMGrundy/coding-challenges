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
# 99th percentile. 28ms.
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        pairs = collections.defaultdict(list)
        
        for i, equation in enumerate(equations):
            n, d = equation
            val = values[i]
            pairs[n].append( (d, val) )
            pairs[d].append( (n, 1/val) )
        
        res = []
        for query in queries:
            targetN, targetD = query
            if targetN not in pairs or targetD not in pairs:
                res.append(-1)
            elif targetN == targetD:
                res.append(1)
            else:
                q = collections.deque([(targetN, 1)])
                visited = set()
                searching = True
                while q and searching:
                    n, product = q.popleft()
                    for neighbor in pairs[n]:
                        d, factor = neighbor
                        if d == targetD:
                            searching = False
                            res.append(product*factor)
                        elif d not in visited:
                            visited.add(d)
                            q.append( (d, product*factor) )
                if searching:
                    res.append(-1)

        return res