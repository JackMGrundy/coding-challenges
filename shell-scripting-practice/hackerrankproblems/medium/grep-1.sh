: '
https://www.hackerrank.com/challenges/text-processing-in-linux-the-grep-command-1/problem

Task 
You are given a text file that will be piped into your command through STDIN. Use grep to display all the lines that contain the word the in them. The search should be sensitive to case. Display only those lines of the input file that contain the word the.

Input Format

A text file will be piped into your command through STDIN.

Output Format

Output only those lines that contain the word the. The search should be case sensitive. The relative ordering of the lines in the output should be the same as it was in the input.

Sample Input

From fairest creatures we desire increase,
That thereby beautys rose might never die,
But as the riper should by time decease,
His tender heir might bear his memory:
But thou contracted to thine own bright eyes,
Feedst thy lights flame with self-substantial fuel,
Making a famine where abundance lies,
Thy self thy foe, to thy sweet self too cruel:
Thou that art now the worlds fresh ornament,
And only herald to the gaudy spring,
Within thine own bud buriest thy content,
And tender churl makst waste in niggarding:
Pity the world, or else this glutton be,
To eat the worlds due, by the grave and thee.
When forty winters shall besiege thy brow,
And dig deep trenches in thy beautys field,
Thy youths proud livery so gazed on now,
Will be a tattered weed of small worth held:
Then being asked, where all thy beauty lies,
Where all the treasure of thy lusty days;
To say within thine own deep sunken eyes,
Were an all-eating shame, and thriftless praise.
How much more praise deserved thy beautys use,
If thou couldst answer This fair child of mine
Shall sum my count, and make my old excuse
Sample Output

But as the riper should by time decease,
Thou that art now the worlds fresh ornament,
And only herald to the gaudy spring,
Pity the world, or else this glutton be,
To eat the worlds due, by the grave and thee.
Where all the treasure of thy lusty days;
Explanation

We have retained and displayed only those lines that contain the word the. A little bit of extra care might be required to avoid retaining cases where the is a suffix or prefix of some other word within the sentences!
'
grep -w "the"