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
import java.util.Map;
import java.util.HashMap;
// 40th percentile
class Solution {
    public int totalFruit(int[] tree) {
        Map<Integer, Integer> counts = new HashMap<Integer, Integer>();
        int res = 0;
        int tail = 0;
        
        for (int head = 0; head < tree.length; head++) {
            int c = tree[head];
            //c in counts
            if (counts.containsKey(c)) {
                counts.put(c, counts.get(c)+1);   
            }
            //c not in counts, but we haven't used both values
            else if (!counts.containsKey(c) && counts.size()<2) {
                counts.put(c, 1);
            }
            //c not in counts, and we have already used both values
            else {
                res = Math.max(res, head-tail);
                while (counts.size()==2) {
                    int cTail = tree[tail];
                    counts.put(cTail, counts.get(cTail) - 1);
                    if (counts.get(cTail)==0) counts.remove(cTail);
                    tail++;
                }
                counts.put(c, 1);
            }
        }
        
        
        return Math.max(res, tree.length-tail);
    }
}


// Faster implementation...
// We don't need to keep track of these counts...
/*
All we need is the current two integers are where the last occurence of them is
in the current string. If we hit a third char, just ditch the character with
the oldest, first occurrence and then make the new char one of our two

...don't have time to code this up right now. 
*/