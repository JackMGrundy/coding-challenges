: '
https://www.hackerrank.com/challenges/awk-2/problem?h_r=next-challenge&h_v=zen

Task 
You are provided a file with four space-separated columns containing the scores of students in three subjects. The first column, contains a single character (A-Z) - the identifier of the student. The next three columns have three numbers (each between 0 and 100, both inclusive) which are the scores of the students in English, Mathematics and Science respectively.

Your task is to identify the performance grade for each student. If the average of the three scores is 80 or more, the grade is 'A'. If the average is 60 or above, but less than 80, the grade is 'B'. If the average is 50 or above, but less than 60, the grade is 'C'. Otherwise the grade is 'FAIL'.

Input Format

There will be no more than 10 rows of data. 
Each line will be in the format: 
[Identifier][Score in English][Score in Math][Score in Science]

Output Format

For each row of data, append a space, a colon, followed by another space, and the grade. Observe the format showed in the sample output.

Sample Input

A 25 27 50
B 35 37 75
C 75 78 80
D 99 88 76
Sample Output

A 25 27 50 : FAIL
B 35 37 75 : FAIL
C 75 78 80 : B
D 99 88 76 : A
Explanation

A scored an average less than 50 => FAIL Same for B C scored an average between 60 and 80 => B 
D scored an average between 80 and 90 => A
'
# Way 1
awk '{
    if ( ($4+$2+$3)/3.0 < 50)
        print $1 " " $2 " " $3 " " $4 " : FAIL";
    else if ( ($4+$2+$3)/3.0 < 60)
        print $1 " " $2 " " $3 " " $4 " : C"
    else if ( ($4+$2+$3)/3.0 < 80)
        print $1 " " $2 " " $3 " " $4 " : B"
    else
        print $1 " " $2 " " $3 " " $4 " : A"
    }'

# Better way - note that with awk, you can make variables
awk '{
    average = ($2+$3+$4)/3.0 
    if ( average < 50)
        print $1 " " $2 " " $3 " " $4 " : FAIL";
    else if ( average < 60)
        print $1 " " $2 " " $3 " " $4 " : C"
    else if ( average < 80)
        print $1 " " $2 " " $3 " " $4 " : B"
    else
        print $1 " " $2 " " $3 " " $4 " : A"
    }'