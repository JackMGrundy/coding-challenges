/*
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.

Accepted
24,452
Submissions
57,249
*/

// 49th percentile. 75ms.
class Solution {
    public List<Double> indexCutoffs;

    public Solution(int[] w) {
        int totalWeight = Arrays.stream(w).sum();
        double cumulativeSum = 0.0;
        this.indexCutoffs = new ArrayList<Double>();
        for (int weight: w) {
            cumulativeSum += (double) weight / totalWeight;
            this.indexCutoffs.add(cumulativeSum);
        }
    }
    
    public int pickIndex() {
        Random rand = new Random();
        double target = rand.nextDouble();
        int l = 0, r = this.indexCutoffs.size()-1;
        
        while (l < r) {
            int mid = (l+r)/2;
            if ( target > this.indexCutoffs.get(mid)) {
                l = mid+1;
            } else {
                r = mid;
            }
        }
        return l;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.pickIndex();
 */


//  75th percentile. 70 ms.
// Don't spend time casting and normalizing
class Solution {
    public List<Integer> indexCutoffs;
    public int totalWeight;
    
    public Solution(int[] w) {
        this.indexCutoffs = new ArrayList<Integer>();
        for (int weight: w) {
            this.totalWeight += weight;
            this.indexCutoffs.add(this.totalWeight);
        }
    }
    
    public int pickIndex() {
        int target = (int) (Math.random()*this.totalWeight);
        int l = 0, r = this.indexCutoffs.size()-1;
        
        while (l < r) {
            int mid = (l+r)/2;
            if ( target >= this.indexCutoffs.get(mid)) {
                l = mid+1;
            } else {
                r = mid;
            }
        }
        return l;
    }
}


/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.pickIndex();
 */


//  100th percentile. 64 ms.
// Use preallocated array instead of list
class Solution {
    public int[] indexCutoffs;
    public int totalWeight;
    
    public Solution(int[] w) {
        this.indexCutoffs = new int[w.length];
        for (int i = 0; i < w.length; i++) {
            this.totalWeight += w[i];
            this.indexCutoffs[i] = this.totalWeight;
        }
    }
    
    public int pickIndex() {
        int target = (int) (Math.random()*this.totalWeight);
        int l = 0, r = this.indexCutoffs.length-1;
        
        while (l < r) {
            int mid = (l+r)/2;
            if ( target >= this.indexCutoffs[mid] ) {
                l = mid+1;
            } else {
                r = mid;
            }
        }
        return l;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.pickIndex();
 */
