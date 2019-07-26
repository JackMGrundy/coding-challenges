: '
https://www.hackerrank.com/challenges/bash-tutorials-count-the-number-of-elements-in-an-array/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Given a list of countries, each on a new line, your task is to read them into an array and then display the count of elements in that array.

Recommended References 
Heres a great tutorial tutorial with useful examples related to arrays in Bash.

Input Format

A list of country names. The only characters present in the country names will be upper or lower case characters and hyphens.

Output Format

A single integer - the number of elements in the array.

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

10
Explanation

There are 10 elements in the array - i.e. the given list has the names of 10 countries.
'
# Way 1
declare -a input
i=0
while read line
do
    input[$i]=$line
    let i++
done

echo ${#input[@]}


# Way 2
declare -a input
while read line
do
    input=("${input[@]}" $line)
done

echo ${#input[@]}