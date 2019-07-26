: '
https://www.hackerrank.com/challenges/lonely-integer-2/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

There are N integers in an array A. All but one integer occur in pairs. Your task is to find the number that occurs only once.

Input Format

The first line of the input contains an integer N, indicating the number of integers. The next line contains N space-separated integers that form the array A.

Constraints
1 <= N <= 100
N % 2 = 1 ( is an odd number) 

0 <= A[i] <= 100, for all i in [1, N]

Output Format

Output S, the number that occurs only once.

Sample Input:1

1
1
Sample Output:1

1
Sample Input:2

3
1 1 2
Sample Output:2

2
Sample Input:3

5
0 0 1 2 1
Sample Output:3

2
Explanation

In the first input, we see only one element (1) and that element is the answer. 
In the second input, we see three elements; 1 occurs at two places and 2 only once. Thus, the answer is 2. 
In the third input, we see five elements. 1 and 0 occur twice. The element that occurs only once is 2.
'
# Way 1
declare -a input=( $(for i in {1..100}; do echo 0; done) )
read n
read arr

for i in ${arr[@]}
do
    if [ ${input[$i]} == 0 ]
    then
        input[$i]="$i"
    else
        input[$i]="0"
    fi
done

res=0
for i in {0..100}; do res=$((res + input[$i])); done
echo $res


# Way 2
read n
read arr
echo "${arr[@]}" | tr ' ' '\n' | sort | uniq -u
