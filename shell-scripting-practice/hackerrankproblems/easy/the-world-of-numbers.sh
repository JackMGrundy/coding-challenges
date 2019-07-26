: '
https://www.hackerrank.com/challenges/bash-tutorials---the-world-of-numbers/problem

Given two integers,  x and y, find their sum, difference, product, and quotient.

Input Format

Two lines containing one integer each (x and y, respectively).

Constraints

-100 <= x, y <= 100
y != 0
 

Output Format

Four lines containing the sum (x+y), difference (x-y), product (x*y), and quotient (x/y), respectively. 
(While computing the quotient, print only the integer part.)

Sample Input

5
2
Sample Output

7
3
10
2
Explanation

5 + 2 = 7 
5 - 2 = 3 
5 * 2 = 10 
5 / 2 = 2 (Integer part)
'
# 1st way
read x
read y
echo $(($x+$y))
echo $(($x-$y))
echo $(($x*$y))
echo $(($x/$y))


# 2nd way
read x
read y
echo `expr $x + $y`
echo `expr $x - $y`
echo `expr $x \* $y`
echo `expr $x / $y`