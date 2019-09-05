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
# 79th percentile. 36ms.
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        pairs = collections.defaultdict(set)
        
        for i,equation in enumerate(equations):
            value = values[i]
            numerator, denominator = equation
            pairs[numerator].add( (denominator, value) )
            pairs[denominator].add( (numerator, 1/value) )
        
        res = []
        for query in queries:
            targetNumerator, targetDenominator = query
            if targetNumerator not in pairs or targetDenominator not in pairs:
                res.append(-1.0)
            elif targetNumerator == targetDenominator:
                res.append(1.0)
            else:
                visited = set()
                q = collections.deque([(targetNumerator, 1)])
                searching = True
                while q and searching:
                    curNumerator, val = q.popleft()
                    visited.add(curNumerator)
                    for neighbor in pairs[curNumerator]:
                        denominator, neighborVal = neighbor
                        if denominator == targetDenominator:
                            res.append(val*neighborVal)
                            searching = False
                            break
                        elif denominator not in visited:
                            q.append( (denominator, val*neighborVal) )
                if not q and searching:
                    res.append(-1)
        
        return res