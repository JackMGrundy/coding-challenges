"""
Implement a basic calculator to evaluate a simple expression string.            

The  expression  string may contain open ( and closing parentheses ), the plus +
or minus sign -, non-negative integers and empty spaces .                       

The  expression string contains only non-negative integers, +, -, *, / operators
,  open  (  and  closing  parentheses  ) and empty spaces . The integer division
should truncate toward zero.                                                    

You  may  assume  that  the  given  expression is always valid. All intermediate
results will be in the range of [-2147483648, 2147483647].                      

Some examples:                                                                  

"1 + 1" = 2                                                                     

" 6-4 / 2 " = 4                                                                 

"2*(5+5*2)/3+(6/2+8)" = 21                                                      

"(2+6* 3+5- (3*14/7+2)*5)+3"=-12                                                
"""



"""
Notes:

Combination  of  Basic  Calculators I and II. Logic for the solution that's most
intuitive in my opinion.                                                        

Start out with a stack and with an operation value equal to "+"                 

get rid of spaces in the string to simplify things                              

Loop through the chars in the string.                                           

Now we go through a bunch of ifs depending on the value of the current char     

if "(":                                                                         

Basically  search ahead until you've found a closed parenthsis. Note that if you
see  more  opens,  then  we keep going until we find the correspodning number of
closed's.                                                                       

At  that  point,  complete  a  recursive  call  to  the  function with just this
subsection  between  the  parentheses...note  if  there  were  multiple pairs of
parentheses  then  we're in turn going to trigger more calls. Each call gets its
own stack and its own operation value.                                          

At  the  current level, we store the result of the call in an int and we advance
the  loop  pointer  to  the end of the section that was processed in a recursive
call.                                                                           

Then  we  go  through  the  standard calculator operations depending on the last
operator seen.                                                                  

+ -> just put the value on the stack                                            

- -> put a negative value on the stack                                          

*  or / -> pop the last value from the stack, apply the operation between it and
the current value. Push the resulting value onto the stack.                     

if digit:                                                                       

Run  a  routine  for  matching  digits  and  building  up  an int until we see a
nondigit. Standard "multiply times 10 then add new value" procedure.            

Then do the operations logic again to determine what to do with the value       

else must be an operation:                                                      

just update operation.                                                          

After all this, add up all the values on the stack and then return.             

"""