/*
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
*/
// 0ms. 100th percentile.
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> pascalsTriangle = new ArrayList<List<Integer>>();
        List<Integer> firstRow = new ArrayList<Integer>();
        firstRow.add(1);
        pascalsTriangle.add(firstRow);
        List<Integer> secondRow = new ArrayList<Integer>();
        secondRow.add(1);
        secondRow.add(1);
        pascalsTriangle.add(secondRow);
        
        for (int i = 2; i < numRows; i++) {
            List<Integer> previousRow = pascalsTriangle.get(pascalsTriangle.size()-1);
            List<Integer> currentRow = new ArrayList<Integer>();
            currentRow.add(1);
            for (int j = 0; j < previousRow.size()-1; j++) {
                currentRow.add(previousRow.get(j) + previousRow.get(j+1));
            }
            currentRow.add(1);
            pascalsTriangle.add(currentRow);
        }
        
        return pascalsTriangle.subList(0, numRows);
    }
}
