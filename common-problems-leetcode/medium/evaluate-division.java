/*
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

Accepted
76,685
Submissions
161,861
*/
// 95th percentile 1ms
class Tuple {
    public String denom;
    public double dist;
    
    Tuple(String denom, double dist) {
        this.denom = denom;
        this.dist = dist;
    }
    
}

class Solution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        // Unique letters
        Set<String> letters = new HashSet<String>();
        for (List<String> eq : equations) {
            String A = eq.get(0);
            String B = eq.get(1);
            letters.add(A);
            letters.add(B);
        }
        
        // Construct graph
        Map<String, Double> linkWeights = new HashMap<String, Double>();
        Map<String, List<String>> denoms = new HashMap<String, List<String>>();
        for (int i = 0; i < values.length; i++) {
            List<String> eq = equations.get(i);
            String A = eq.get(0);
            String B = eq.get(1);
            double val = values[i];
            linkWeights.put(A+B, val);
            linkWeights.put(B+A, 1.0/val);
            if(denoms.containsKey(A)) {
                denoms.get(A).add(B);
            } else {
                List<String> temp = new ArrayList<String>();
                denoms.put(A, temp);
                denoms.get(A).add(B);
            }
            
            if (denoms.containsKey(B)) {
                denoms.get(B).add(A);
            } else {
                List<String> temp = new ArrayList<String>();
                denoms.put(B, temp);
                denoms.get(B).add(A);
            }
        }
        
        
        // result
        double[] res = new double[queries.size()];
        
        for (int i = 0; i < res.length; i++) {
            List<String> query = queries.get(i);
            
            String A = query.get(0);
            String B = query.get(1);
            if (!letters.contains(A) || !letters.contains(B)) {
                res[i] = -1.0;
            } else if (A.equals(B)) {
                res[i] = 1.0;
            } else if (linkWeights.containsKey(A+B)) {
                res[i] = linkWeights.get(A+B);
            } else if (linkWeights.containsKey(B+A)) {
                res[i] = linkWeights.get(B+A);
            }
            // BFS
            else  {
                
                Set<String> visited = new HashSet<String>();
                Deque<Tuple> q = new ArrayDeque<Tuple>();
                List<String> ADenoms = denoms.get(A);
                for (String denom : ADenoms) {
                    Tuple temp = new Tuple(denom, linkWeights.get(A+denom));
                    q.addLast(temp);
                }
                
                while (q.size() > 0) {
                    Tuple cur = q.pollFirst();
                    String C = cur.denom;
                    double dist = cur.dist;
                    res[i] = -1.0;
                    if ( visited.contains(C) ) {
                        continue;
                    }
                    visited.add(C);
                    if (C.equals(B)) {
                        res[i] = dist;
                        break;
                    } else {
                        for (String denom : denoms.get(C)) {
                            Tuple temp = new Tuple(denom, dist*linkWeights.get(C+denom));
                            q.addLast(temp);
                        }
                    }
                }
            }
        }
        
        return res;
        
    }
}