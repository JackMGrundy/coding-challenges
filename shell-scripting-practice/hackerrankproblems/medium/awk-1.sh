: 
'
https://www.hackerrank.com/challenges/awk-1/problem

Task 
You are given a file with four space separated columns containing the scores of students in three subjects. The first column contains a single character (), the student identifier. The next three columns have three numbers each. The numbers are between  and , both inclusive. These numbers denote the scores of the students in English, Mathematics, and Science, respectively.

Your task is to identify those lines that do not contain all three scores for students.

Input Format

There will be no more than  rows of data. 
Each line will be in the following format: 
[Identifier][English Score][Math Score][Science Score]

Output Format

For each student, if one or more of the three scores is missing, display:

Not all scores are available for [Identifier]
Sample Input

A 25 27 50
B 35 75
C 75 78 
D 99 88 76
Sample Output

Not all scores are available for B
Not all scores are available for C
Explanation

Only  scores have been provided for student B and student C.
'
awk 'NF!=4 { print "Not all scores are available for "$1 }'