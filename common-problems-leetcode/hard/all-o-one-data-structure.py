"""
Implement a data structure supporting the following operations:                 

Inc(Key)  -  Inserts a new key with value 1. Or increments an existing key by 1.
Key is guaranteed to be a non-empty string.                                     

Dec(Key)  -  If  Key's  value is 1, remove it from the data structure. Otherwise
decrements  an  existing key by 1. If the key does not exist, this function does
nothing. Key is guaranteed to be a non-empty string.                            

GetMaxKey()  - Returns one of the keys with maximal value. If no element exists,
return an empty string "".                                                      

GetMinKey()  - Returns one of the keys with minimal value. If no element exists,
return an empty string "".                                                      

Challenge: Perform all these in O(1) time complexity.                           

"""






"""
Notes:

Very similar to the LFU cache problem.                                          

Hash table:                                                                     

Key -> value                                                                    

Hash table:                                                                     

value -> orderedSet()                                                           

minVal                                                                          

maxVal                                                                          

The second table maps values to orderedSets...                                  

Inc:                                                                            

if  it's  a  new  key,  just  insert  it to the hash table and add it to the "1"
ordered set                                                                     

if it's not a new key, get its old value in the first table. Update its value in
the  first  table.  Remove  it  from  its  count set. Add it to a count set with
count+1.                                                                        

In both cases, update the minVal and maxVal accorindly                          

Dec...                                                                          

parallel to inc                                                                 

Max/Min:                                                                        

The  inc  and dec operations maintain the minVal and maxVal. Just get a val from
the maxVal/minVal sets as needed. Because they're ordered sets, we can get a val
on constant time.                                                               

"""