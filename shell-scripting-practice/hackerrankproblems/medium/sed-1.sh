: 

'
https://www.hackerrank.com/challenges/text-processing-in-linux-the-sed-command-1/problem
Task 
For each line in a given input file, transform the first occurrence of the word the with this. The search and transformation should be strictly case sensitive.

Input Format

A text file will be piped into your command through STDIN.

Output Format

Transform the text as specified by the task.

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

From fairest creatures we desire increase,
That thereby beautys rose might never die,
But as this riper should by time decease,
His tender heir might bear his memory:
But thou contracted to thine own bright eyes,
Feedst thy lights flame with self-substantial fuel,
Making a famine where abundance lies,
Thy self thy foe, to thy sweet self too cruel:
Thou that art now this worlds fresh ornament,
And only herald to this gaudy spring,
Within thine own bud buriest thy content,
And tender churl makst waste in niggarding:
Pity this world, or else this glutton be,
To eat this worlds due, by the grave and thee.
When forty winters shall besiege thy brow,
And dig deep trenches in thy beautys field,
Thy youths proud livery so gazed on now,
Will be a tattered weed of small worth held:
Then being asked, where all thy beauty lies,
Where all this treasure of thy lusty days;
To say within thine own deep sunken eyes,
Were an all-eating shame, and thriftless praise.
How much more praise deserved thy beautys use,
If thou couldst answer This fair child of mine
Shall sum my count, and make my old excuse
Explanation

The line:

But as the riper should by time decease,
has been transformed to:

But as this riper should by time decease,  
The line:

To eat the worlds due, by the grave and thee.    
has been transformed to:

To eat this worlds due, by the grave and thee. 
'
sed 's/ the / this /'