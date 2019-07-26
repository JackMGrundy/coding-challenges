:
'
https://www.hackerrank.com/challenges/sed-command-4/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Task

Given  lines of credit card numbers, mask the first  digits of each credit card number with an asterisk (i.e., *) and print the masked card number on a new line. Each credit card number consists of four space-separated groups of four digits. For example, the credit card number 1234 5678 9101 1234 would be masked and printed as **** **** **** 1234.

Input Format

Each line contains a credit card number in the form dddd dddd dddd dddd, where  denotes a decimal digit (i.e.,  through ). There are a total of  lines of credit card numbers.

Constraints

; note that the value of  does not matter when writing your command.
Output Format

For each credit card number, print its masked version on a new line.

Sample Input

1234 5678 9101 1234  
2999 5178 9101 2234  
9999 5628 9201 1232  
8888 3678 9101 1232  
Sample Output

**** **** **** 1234
**** **** **** 2234
**** **** **** 1232
**** **** **** 1232
Explanation

Observe that the first twelve digits have been masked for each credit card number, and they are printed in the same order as they were received as input.
'
sed -r 's/([0-9]{4}\s){3}/\**** **** **** /'

