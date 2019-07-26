: '
https://www.hackerrank.com/challenges/text-processing-cut-1/problem
Given N lines of input, print the 3rd character from each line as a new line of output. It is guaranteed that each of the  lines of input will have a 3rd character.

Input Format

A text file containing  lines of ASCII characters.

Constraints
1 <= N <= 100

Output Format

For each line of input, print its  character on a new line for a total of lines of output.

Sample Input

Hello
World
how are you
Sample Output

l
r
w
'
# 1st way
while IFS= read -r line
do
echo $line | head -c 3 | tail -c 1
printf "\n"
done
echo $line | head -c 3 | tail -c 1

# 2nd way
cut -c3
