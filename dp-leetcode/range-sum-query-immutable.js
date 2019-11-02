/*
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
Accepted
131,021
Submissions
353,568
*/

// Naive approach
// 94th percentile in speed...althogh twice as much as space
/**
 * @param {number[]} nums
 */
var NumArray = function(nums) {
    this.nums = nums;
    this.prefixSums = [nums[0]];
    for (let i = 1; i < nums.length; i++) {
        this.prefixSums[i] = this.prefixSums[i-1]+nums[i];
    }
};

/** 
 * @param {number} i 
 * @param {number} j
 * @return {number}
 */
NumArray.prototype.sumRange = function(i, j) {
    return this.prefixSums[j]-this.prefixSums[i]+this.nums[i];
};

// Segment tree approach
// 108ms. 80 percentile.
/*
Note the use of this rather than NumArray.prototype. We're attaching n and
tree to each specific NumArray object rather than the shared prototype. So
each instance of NumArray will share the update and sumArray methods. But
they'll each have their own values of n and tree. 

*/
/**
 * @param {number[]} nums
 */
var NumArray = function(nums) {
    this.n = nums.length;
    this.tree = createSegmentTree(nums);
};


var createSegmentTree = function(nums) {
    let n = nums.length;
    let tree = new Array(nums.length*2).fill(0);
    
    for (let numIndex = 0, treeIndex = n; numIndex < n; numIndex++, treeIndex++) {
        tree[treeIndex] = nums[numIndex];    
    }
    
    for (let treeIndex = n - 1; 0 < treeIndex; treeIndex--) {
        tree[treeIndex] = tree[treeIndex*2] + tree[treeIndex*2 + 1]
    }
    
    return tree;
}

/** 
 * @param {number} i 
 * @param {number} val
 * @return {void}
 */
NumArray.prototype.update = function(i, val) {
    let pos = i + this.n;
    this.tree[pos] = val;
    
    while (0 < pos) {
        let left = pos;
        let right = pos;
        if (pos%2 === 0) {
            right++;
        } else {
            left -= 1;
        }
        
        let parent = Math.floor(pos/2.0);
        this.tree[parent] = this.tree[left] + this.tree[right];
        
        pos = parent;
    }
    
};

/** 
 * @param {number} i 
 * @param {number} j
 * @return {number}
 */
NumArray.prototype.sumRange = function(i, j) {
    let sum = 0;
    i += this.n;
    j += this.n;
    while (i <= j) {
        if (i%2 === 1) {
            sum += this.tree[i];
            i += 1;
        }
        i = Math.floor(i/2.0);
        
        if (j%2 === 0) {
            sum += this.tree[j];
            j -= 1
        }
        j = Math.floor(j/2.0);
    }
    
    return sum;
};

/** 
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * obj.update(i,val)
 * var param_2 = obj.sumRange(i,j)
 */


 /*
 Notes

A naive solution does pass here. But this problem is actually about segment trees.
See segment tree notes for details. This problem is a straightforwards segment tree
problem.

 */