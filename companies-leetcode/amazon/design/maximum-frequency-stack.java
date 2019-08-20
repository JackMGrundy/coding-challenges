/*
Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:

push(int x), which pushes an integer x onto the stack.
pop(), which removes and returns the most frequent element in the stack.
If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.
 

Example 1:

Input: 
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
Explanation:
After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

pop() -> returns 5, as 5 is the most frequent.
The stack becomes [5,7,5,7,4].

pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].

pop() -> returns 5.
The stack becomes [5,7,4].

pop() -> returns 4.
The stack becomes [5,7].
 

Note:

Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
It is guaranteed that FreqStack.pop() won't be called if the stack has zero elements.
The total number of FreqStack.push calls will not exceed 10000 in a single test case.
The total number of FreqStack.pop calls will not exceed 10000 in a single test case.
The total number of FreqStack.push and FreqStack.pop calls will not exceed 150000 across all test cases.

*/
// 88ms. 84th percentile.
import java.util.*;
class FreqStack {
    HashMap<Integer, Stack<Integer>> countToStack;
    HashMap<Integer, Integer> elementCounts;
    int maxCount;
        
    public FreqStack() {
        countToStack = new HashMap<Integer, Stack<Integer>>();
        elementCounts = new HashMap<Integer, Integer>();
        maxCount = 0;
    }
    
    public void push(int x) {
        elementCounts.put(x, elementCounts.getOrDefault(x, 0)+1);
        int xCount = elementCounts.get(x);
        maxCount = Math.max(elementCounts.get(x), maxCount);
        
        if (!countToStack.containsKey(xCount)) {
            countToStack.put(xCount, new Stack<Integer>());
        }
        countToStack.get(xCount).push(x);
    }
    
    public int pop() {
        Stack<Integer> maxStack = countToStack.get(maxCount);
        int res = maxStack.pop();
        elementCounts.put(res, elementCounts.get(res)-1);
        if (maxStack.size() == 0) {
            maxCount -= 1;
        }
        return res;
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack obj = new FreqStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 */