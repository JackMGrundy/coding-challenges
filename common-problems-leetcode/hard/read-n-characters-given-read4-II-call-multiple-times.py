"""
Given a file and assume that you can only read the file using a given method read4, 
implement a method read to read n characters. Your method read may be called multiple 
times.

 

Method read4:

The API read4 reads 4 consecutive characters from the file, then writes those 
characters into the buffer array buf.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:

    Parameter:  char[] buf
    Returns:    int

Note: buf[] is destination not source, the results from read4 will be copied to buf[]
Below is a high level example of how read4 works:

File file("abcdefghijk"); // File is "abcdefghijk", initially file pointer (fp) 
points to 'a'
char[] buf = new char[4]; // Create buffer with enough space to store characters
read4(buf); // read4 returns 4. Now buf = "abcd", fp points to 'e'
read4(buf); // read4 returns 4. Now buf = "efgh", fp points to 'i'
read4(buf); // read4 returns 3. Now buf = "ijk", fp points to end of file
 

Method read:

By using the read4 method, implement the method read that reads n characters 
from the file and store it in the buffer array buf. Consider that you cannot
 manipulate the file directly.

The return value is the number of actual characters read.

Definition of read:

    Parameters:	char[] buf, int n
    Returns:	int

Note: buf[] is destination not source, you will need to write the results to buf[]
 

Example 1:

File file("abc");
Solution sol;
// Assume buf is allocated and guaranteed to have enough space for storing all 
characters from the file.
sol.read(buf, 1); // After calling your read method, buf should contain "a". We read a total of 1 character from the file, so return 1.
sol.read(buf, 2); // Now buf should contain "bc". We read a total of 2 characters from the file, so return 2.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
Example 2:

File file("abc");
Solution sol;
sol.read(buf, 4); // After calling your read method, buf should contain "abc". We read a total of 3 characters from the file, so return 3.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
 

Note:

Consider that you cannot manipulate the file directly, the file is only accesible 
for read4 but not for read.
The read function may be called multiple times.
Please remember to RESET your class variables declared in Solution, as static/class 
variables are persisted across multiple test cases. Please see here for more details.
You may assume the destination buffer array, buf, is guaranteed to have enough space
for storing n characters.
It is guaranteed that in a given test case the same buffer buf is called by read.
"""
# 36ms. 84 percentile.
"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    
    def __init__(self):
        self.queue = collections.deque([])
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        charsRead = 0
        sourceEmpty = False
        
        while charsRead < n:
            if len(self.queue) == 0:
                if sourceEmpty:
                    return charsRead
                
                nextFour = ['']*4
                numNewChars = read4(nextFour)
                self.queue.extend(nextFour[0:numNewChars])
                sourceEmpty = numNewChars != 4
            else:
                buf[charsRead] = self.queue.popleft()
                charsRead += 1
        
        return charsRead

"""
Notes:
	There's a file you want to read chars from. You have a method called read4() that 
    can get 4 characters for you at a time. 
	Your method has a buffer and n to indicate the number of characters to put into 
    the buffer.
	So the issue is figuring out how to use read4 to make this work...
	If the user only ever wanted to read 4 characters at a time, you would just read4.
	If they want more than 4, you can just keep using read 4 for all the chars 
    except the last 1 to 3. 
	The issue then is how to deal with those extra charactes...


	First idea:
	
	maintain a queue in the class

	if they want numChars <= queue.size():
		just write that many from the queue into the buffer

	elif they want more than are in the queue:
		write what is in the queue into the buffer and update the char number

		Then call read4 enough times to get all the chars...say we need 17 chars, 
        then that's 5 read4's. 
		Write the desired number of chars in the buffer. Store the rest in queue. 

	Important...at any point, read4 could hit the end of the file...in that case 
    cut whatever the current process is and return the number of chars that were read. 



	^Note you could simplify this a bit by writing all the chars into the queue 
    and then transferring to buffer...this has a slight improvmeent in that the 
    queue will never have more than 3 chars...very small...

"""