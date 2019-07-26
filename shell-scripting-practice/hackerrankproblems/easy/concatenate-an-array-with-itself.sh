: '
https://www.hackerrank.com/challenges/bash-tutorials-concatenate-an-array-with-itself/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Given a list of countries, each on a new line, your task is to read them into an array. Then, concatenate the array with itself (twice) - so that you have a total of three repetitions of the original array - and then display the entire concatenated array, with a space between each of the countries' names.

Recommended References 
Here's a great tutorial tutorial with useful examples related to arrays in Bash.

Input Format

A list of country names. The only characters present in the country names will be upper or lower case characters and hyphens.

Output Format

Display the entire concatenated array, with a space between each of them.

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

Namibia Nauru Nepal Netherlands NewZealand Nicaragua Niger Nigeria NorthKorea Norway Namibia Nauru Nepal Netherlands NewZealand Nicaragua Niger Nigeria NorthKorea Norway Namibia Nauru Nepal Netherlands NewZealand Nicaragua Niger Nigeria NorthKorea Norway
Explanation

The entire concatenated array has been displayed.
'
# Way 1
declare -a input
i=0
while read line
do
    input[$i]=$line
    let i++
done
input[$i]=$line

echo "${input[@]} ${input[@]} ${input[@]}"


# Way 2
while read line
do
    input=("${input[@]}" $line)
done
input=("${input[@]}" $line)

echo "${input[@]} ${input[@]} ${input[@]}"