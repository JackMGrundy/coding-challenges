: '
Write a Bash script which accepts  as input and displays a greeting: "Welcome (name)"

Input Format

One line, containing a name

Output Format

One line: "Welcome (name)" (quotation marks excluded). 
The evaluation will be case-sensitive.

Sample Input 0

Dan  
Sample Output 0

Welcome Dan  
Sample Input 1

Prashant
Sample Output 1

Welcome Prashant
'
echo "Please input your name"
read name
echo "Welcome $name"