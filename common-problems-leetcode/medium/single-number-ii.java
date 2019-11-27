/* 

Given  a  non-empty  array of integers, every element appears three times except
for one, which appears exactly once. Find that single one.                      

Note:                                                                           

Your  algorithm  should have a linear runtime complexity. Could you implement it
without using extra memory?                                                     

Example 1:                                                                      

Input: [2,2,3,2]                                                                

Output: 3                                                                       

Example 2:                                                                      

Input: [0,1,0,1,0,1,99]                                                         

Output: 99                                                                      


*/





/*

Notes:

There are trivial ways to do this. To accomplish
it with constant memory requires a bitmap solution.

Think of each number in the input as a bitmap. Let's say every number
appeared twice except 1. Then we could just XOR our way through all of
them to find that one unique number. 

However, our goal is to detect the number that appears once out of all the
numbers that appear 3 times. We need additional operations to do this.



*/