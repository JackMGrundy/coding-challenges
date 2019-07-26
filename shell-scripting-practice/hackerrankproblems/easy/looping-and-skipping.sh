: '
https://www.hackerrank.com/challenges/bash-tutorials---looping-and-skipping/problem

Your task is to use for loops to display only odd natural numbers from  to .

Input Format

There is no input.

Constraints

-

Output Format

1
3
5
.
.
.
.
.
99  
Sample Input

-

Sample Output

1
3
5
.
.
.
.
.
99  
Explanation

-
'
for i in $(seq 1 2 99)
do
    echo $i 
done