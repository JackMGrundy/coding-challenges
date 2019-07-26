: '
https://www.hackerrank.com/challenges/bash-tutorials---comparing-numbers/problem

Given two integers, x and y, identify whether x < y or x > y or x = y.

Exactly one of the following lines: 
- X is less than Y 
- X is greater than Y 
- X is equal to Y

Input Format

Two lines containing one integer each (x and y, respectively).

Constraints

-

Output Format

Exactly one of the following lines: 
- X is less than Y 
- X is greater than Y 
- X is equal to Y

Sample Input

Sample Input 1

5  
2  
Sample Input 2

2
2  
Sample Input 3

2
3  
Sample Output

Sample Output 1

X is greater than Y  
Sample Output 2

X is equal to Y   
Sample Output 3

X is less than Y  
'
read x
read y
if ((x > y))
then
    echo "X is greater than Y"
elif ((x < y))
then
    echo "X is less than Y"
else
    echo "X is equal to Y"
fi