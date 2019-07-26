: '
https://www.hackerrank.com/challenges/bash-tutorials-display-the-third-element-of-an-array/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Given a list of countries, each on a new line, your task is to read them into an array and then display the element indexed at 3. Note that indexing starts from 0.

Recommended References 
Heres a great tutorial tutorial with useful examples related to arrays in Bash.

Input Format

A list of country names. The only characters present in the country names will be upper or lower case characters and hyphens.

Output Format

The element at index 3 of the array (one string).

Sample Input

Namibia
Nauru
Nepal
Netherlands
NewZealand
Nicaragua
Niger
Nigeria
NorthKorea
Norway
Sample Output

Netherlands
Explanation

The element at index  in the list is Netherlands.
'
declare -a input
while read line
do
    input=("${input[@]}" $line)
done
input=("${input[@]}" $line)

echo ${input[3]}