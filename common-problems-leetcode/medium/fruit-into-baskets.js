/*
In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

 

Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
Example 2:

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
Example 3:

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
Example 4:

Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.
 

Note:

1 <= tree.length <= 40000
0 <= tree[i] < tree.length
*/
// 57th percentile
/*
Note the use of map instead of Object. The benefit is that we can use numbers as keys.
Also, some of th syntax is cleaner...for example, counts.has(c) vs.
Object.keys(counts).indexOf(c) === -1  : )
*/
/**
 * @param {number[]} tree
 * @return {number}
 */
var totalFruit = function(tree) {
    let counts = new Map();
    let tail = 0,
        res = 0;
    
    for (let head = 0; head < tree.length; head++) {
        let c = tree[head];
        // c already in counts
        if (counts.has(c)) {
            counts.set(c, counts.get(c)+1);
        }
        //c not in counts but we have chars to spare
        else if (!counts.has(c)  && counts.size < 2) {
            counts.set(c, 1);
        }
        //c not in counts and we don't have chars to spare
        else {
            res = Math.max(res, head - tail);
            while (counts.size==2) {
                let tailC = tree[tail];
                counts.set(tailC, counts.get(tailC)-1);
                if (counts.get(tailC) === 0) counts.delete(tailC);
                tail += 1;
            }
            // tail += 1;
            counts.set(c, 1);
        }
    }
    
    return Math.max(res, tree.length-tail);
};


// For comparison, using a traditional object is a lot slower with these casts...
// 20th percentile
/**
 * @param {number[]} tree
 * @return {number}
 */
var totalFruit = function(tree) {
    let counts = {}
    let tail = 0,
        res = 0;
    
    for (let head = 0; head < tree.length; head++) {
        let c = tree[head].toString();
        // c already in counts
        if (Object.keys(counts).indexOf(c) !== -1) {
            counts[c] += 1;
        }
        //c not in counts but we have chars to spare
        else if (Object.keys(counts).indexOf(c) === -1  && Object.keys(counts).length < 2) {
            counts[c] = 1;
        }
        //c not in counts and we don't have chars to spare
        else {
            res = Math.max(res, head - tail);
            while (Object.keys(counts).length==2) {
                let tailC = tree[tail];
                counts[tailC] -= 1;
                if (counts[tailC] === 0) delete counts[tailC];
                tail += 1;
            }
            // tail += 1;
            counts[c] = 1;
        }
    }
    
    return Math.max(res, tree.length-tail);
};