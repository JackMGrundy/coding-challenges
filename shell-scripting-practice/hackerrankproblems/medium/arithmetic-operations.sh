: '
https://www.hackerrank.com/challenges/bash-tutorials---arithmetic-operations/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

We provide you with expressions containing +,-,*,^, / and parenthesis. None of the numbers in the expression involved will exceed 999. 
Your task is to evaluate the expression and display the correct output rounding up to 3 decimal places.

Sample Input

Sample Input 1

5+50*3/20 + (19*2)/7
Sample Input 2

-105+50*3/20 + (19^2)/7
Sample Input 3

(-105.5*7+50*3)/20 + (19^2)/7
Sample Output

Sample Output 1

17.929
Sample Output 2

-45.929
Sample Output 3

 22.146
'
read exp
printf "%.3f" $(echo "scale=10;$exp" | bc)