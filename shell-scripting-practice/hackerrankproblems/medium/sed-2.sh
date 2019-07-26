:

'
https://www.hackerrank.com/challenges/text-processing-in-linux-the-sed-command-2/problem?h_r=next-challenge&h_v=zen

Task 
For each line in a given input file, transform all the occurrences of the word thy with your. The search should be case insensitive, i.e. thy, Thy, tHy etc. should be transformed to your.

Input Format

A text file will be piped into your command via STDIN.

Output Format

Transform and display the text as required in the task.

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
But as the riper should by time decease,
His tender heir might bear his memory:
But thou contracted to thine own bright eyes,
Feedst your lights flame with self-substantial fuel,
Making a famine where abundance lies,
your self your foe, to your sweet self too cruel:
Thou that art now the worlds fresh ornament,
And only herald to the gaudy spring,
Within thine own bud buriest your content,
And tender churl makst waste in niggarding:
Pity the world, or else this glutton be,
To eat the worlds due, by the grave and thee.
When forty winters shall besiege your brow,
And dig deep trenches in your beautys field,
your youths proud livery so gazed on now,
Will be a tattered weed of small worth held:
Then being asked, where all your beauty lies,
Where all the treasure of your lusty days;
To say within thine own deep sunken eyes,
Were an all-eating shame, and thriftless praise.
How much more praise deserved your beautys use,
If thou couldst answer This fair child of mine
Shall sum my count, and make my old excuse  
Explanation

The line:

Feedst thy lights flame with self-substantial fuel, 
has been transformed to:

Feedst your lights flame with self-substantial fuel,  
The line:

Thy self thy foe, to thy sweet self too cruel: 
has been transformed to:

your self your foe, to your sweet self too cruel:
'
sed 's/thy/your/gI'


