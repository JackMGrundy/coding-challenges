: '
https://www.hackerrank.com/challenges/bash-tutorials-remove-the-first-capital-letter-from-each-array-element/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Objective 
In this challenge, we practice reading and transforming arrays.

Resources 
Here's a great tutorial with useful examples related to arrays in Bash.

Task 
You are given a list of countries, each on a new line. Your task is to read them into an array and then transform them in the following way:

The first capital letter (if present) in each element of the array should be replaced with a dot ('.'). Then, display the entire array with a space between each country's names.

Input Format

The input format consists of a list of country names each on a separate line. The only characters present in the country names will be upper or lower case characters and hyphens.

Output Format

Transform the names as described and display the entire array of country names with a space between each of them.

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

.amibia .auru .epal .etherlands .ewZealand .icaragua .iger .igeria .orthKorea .orway

Explanation

The first capital letter of each name has been replaced with a dot ('.').
'
declare -a input
while read line
do
    input=("${input[@]}" $line)
done
echo ${input[@]/[A-Z]/.} #Note user of regular expression pattern matching


