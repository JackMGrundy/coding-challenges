/*
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3] 
*/

// 6ms. 90th percentile
class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> res = new ArrayList<Integer>();
        
        for (int i = 0; i < nums.length; i++) {
            int curNum = nums[i];
            if (curNum < 0) {
                continue;
            }
            while (curNum-1 != i) {
                curNum = nums[i];

                int temp = nums[curNum-1];
                if (temp < 0) {
                    nums[curNum-1]--;
                } else if (temp > 0) {
                    nums[curNum-1] = -1;
                }
                
                if (temp < 0) {
                    break;
                } else {
                  nums[i] = temp;
                }
            }
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] <= -2) {
                res.add(i+1);
            }
        }
        
        return res;
    }
}



// 6ms. 90th percentile.
class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> res = new ArrayList<Integer>();
        
        for (int i = 0; i < nums.length; i++) {
            int index = Math.abs(nums[i])-1;
            if (nums[index] < 0) {
                res.add(index+1);
            } else {
                nums[index] = -nums[index];
            }
        }
        return res;
    }
}




/*
Notes:
First impulse is to make a messy swap solution like the first one.
The key thing to note though is that we just want to use an array element to hold two pieces of info
1) have we already seen a value of that index
2) the actual number there

The swapping business is try to sort out the actual number there so that we can store "we have seen the value
of this index".

The smarter solution is to just make the element store both. The absolute value of the number there holds
2) and whether or not it's negative holds 1). 
*/