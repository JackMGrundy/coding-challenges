"""
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
"""
# 71st percentile
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        counts = {}
        tail = res = 0
        
        for head, c in enumerate(tree):
            # Already in counts
            if c in counts:
                counts[c] += 1
            # Not in counts but we have letters to burn
            elif c not in counts and len(counts)<2:
                counts[c] = 1
            # Not in counts and we don't have letters to burn
            else:
                res = max(res, head-tail)
                while len(counts) == 2:
                    tailC = tree[tail]
                    counts[tailC] -= 1
                    if counts[tailC] == 0:
                        del counts[tailC]
                    tail += 1
                counts[c] = 1
        
        return max(res, len(tree)-tail)



# 67th percentile
"""
As I expectd, adding a set doesn't help...counts never has more than 2 keys...so the lookup
"in" operations above don't really take any time...
"""
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        counts = {}
        seen = set()
        tail = res = 0
        
        for head, c in enumerate(tree):
            # Already in counts
            if c in seen:
                counts[c] += 1
            # Not in counts but we have letters to burn
            elif c not in seen and len(seen)<2:
                counts[c] = 1
                seen.add(c)
            # Not in counts and we don't have letters to burn
            else:
                res = max(res, head-tail)
                while len(seen) == 2:
                    tailC = tree[tail]
                    counts[tailC] -= 1
                    if counts[tailC] == 0:
                        seen.remove(tailC)
                    tail += 1
                counts[c] = 1
                seen.add(c)
        
        return max(res, len(tree)-tail)