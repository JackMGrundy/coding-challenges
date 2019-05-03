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
// 100th percentile. 56ms.
/**
 * @param {string[][]} equations
 * @param {number[]} values
 * @param {string[][]} queries
 * @return {number[]}
 */
var calcEquation = function(equations, values, queries) {
    // set of letter
    let letters = new Set();
    equations.forEach(eq => {
        let A = eq[0],
            B = eq[1];
        letters.add(A);
        letters.add(B);
    })
    
    // pieces to graph:
    let linkWeights = {},
        denoms = {};
    for (let i = 0; i < equations.length; i++) {
        eq = equations[i];
        val = values[i];
        let A = eq[0],
            B = eq[1];
        linkWeights[A+B] = val;
        linkWeights[B+A] = 1.0/val;
        if (denoms[A]) denoms[A].push(B)
        else denoms[A] = [B]
        
        if (denoms[B]) denoms[B].push(A)
        else denoms[B] = [A]
    }
    
    // iterate through queries
    res = []
    queries.forEach( query => {
        let A = query[0],
            B = query[1];
    
        // check if we have the letter
        if (!letters.has(A) || !letters.has(B)) {
            res.push(-1.0);
        }
        // check if we already have the value
        else if (A==B) {
            res.push(1.0);
        }
        // bfs to find answer
        else {
            let q = [];
            let visited = new Set();
            let ans = -1.0;
            denoms[A].forEach(denom => {
                q.push( [ denom, linkWeights[ A+denom ] ] );
            })
            
            while (q.length > 0) {
                let cur = q.shift();
                let C = cur[0],
                    val = cur[1];
                if ( visited.has(C) ) continue
                visited.add(C);
                if (C === B) {
                    ans = val;
                    break;
                }
                else {
                    denoms[C].forEach(denom => {
                        q.push( [ denom, val*linkWeights[C+denom] ] );
                    })
                }
            }
            res.push(ans);
        }
    })
  
    return res
};