: '
https://www.hackerrank.com/challenges/bash-tutorials---more-on-conditionals/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Given three integers (x, y, and z) representing the three sides of a triangle, identify whether the triangle is Scalene, Isosceles, or Equilateral.

Input Format

Three integers, each on a new line.

Constraints

1 <= X, Y, Z <= 1000 
Sum of any two sides will be greater than the third.

Output Format

One word: either "SCALENE" or "EQUILATERAL" or "ISOSCELES" (quotation marks excluded).

Sample Input

Sample Input 1

2
3
4
Sample Input 2

6
6
6 
Sample Output

Sample Output 1

SCALENE
Sample Output 2

EQUILATERAL  

'
read x
read y
read z

if [ $x == $y ] && [ $y == $z ]
then
echo "EQUILATERAL"
elif [ $x == $y ] || [ $y == $z ] || [ $x == $z ]
then
echo "ISOSCELES"
else
echo "SCALENE"
fi