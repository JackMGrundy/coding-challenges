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

# Create a mapping of letter -> (tuples)

for q in query:

    # Check if same letter...

    # check if we already have the pair

    # check if we have the reciprocal

    # check if both letters are in the list of letters...if not...return -1

    # Do a bfs
    """
    add to the queue all pairs with the start letter and dist valA if (a,b) or 1/valA if (b, a)...(let, dist)...make sure (a, b) is added
    pop cur
    if cur's 2nd letter is target, done
    otherwise:
        target: a, e
        add all the pairs of the 2nd letter with dist equal to:
            we're going to pop something of the form:
            (b, c) 
            or 
            (c, b) 
            by design...the first ele was (a, b)

            so if (b, c), dist = dist * (b,c)dist
               if (c, b), dist = dist / (c,b)dist
            
            # Memoize the updated dists...
            
            add all the children of c...

            nxt time:
            we pop off something of the form:
            (c, d)
            or
            (d, c)

            by design, the second ele was (b, c)

            so if (c, d), dist = dist * (c, d)dist
               if (d, c) dist = dist / (d, c)dist
            
            add all the children of d...

            eventually we're going to get something of the form:
            (d, e)
            or 
            (e, d)
            ...calculate the dist as usual and return
        

    if we get to the end without a path...return -1
    

    along the way memoize for future queries

    """