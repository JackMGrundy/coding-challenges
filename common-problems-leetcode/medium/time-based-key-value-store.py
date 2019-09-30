"""
Create a timebased key-value store class TimeMap, that supports two operations. 

1. set(string key, string value, int timestamp)                                 

Stores the key and value, along with the given timestamp.                       

2. get(string key, int timestamp)                                               

Returns a value such that set(key, value, timestamp_prev) was called previously,
with timestamp_prev <= timestamp.                                               

If  there  are  multiple  such  values,  it  returns  the  one  with the largest
timestamp_prev.                                                                 

If there are no values, it returns the empty string ("").                       

                                                                                

Example 1:                                                                      

Input:   inputs   =  ["TimeMap","set","get","get","set","get","get"],  inputs  =
[[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]   

Output: [null,null,"bar","bar",null,"bar2","bar2"]                              

Explanation:                                                                    

TimeMap kv;                                                                     

kv.set("foo",  "bar",  1);  //  store  the  key "foo" and value "bar" along with
timestamp = 1                                                                   

kv.get("foo", 1);  // output "bar"                                              

kv.get("foo",  3);  // output "bar" since there is no value corresponding to foo
at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"  
                                                                                

kv.set("foo", "bar2", 4);                                                       

kv.get("foo", 4); // output "bar2"                                              

kv.get("foo", 5); //output "bar2"                                               

Example 2:                                                                      

Input:  inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs =
[[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]

Output: [null,null,null,"","high","high","low","low"]                           

                                                                                

Note:                                                                           

All key/value strings are lowercase.                                            

All key/value strings have length in the range [1, 100]                         

The timestamps for all TimeMap.set operations are strictly increasing.          

1 <= timestamp <= 10^7                                                          

TimeMap.set  and  TimeMap.get  functions  will be called a total of 120000 times
(combined) per test case.                                                       

"""
# 712ms. 87 percentile.
# Builtins.
from collections import defaultdict
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.times = defaultdict(list)
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect(self.times[key], timestamp)
        return self.values[key][i - 1] if i else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


# 700ms. 94 percentile.
# Custom binary search
from collections import defaultdict
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.times = defaultdict(list)
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if timestamp < self.times[key][0]:
            return ''
        elif timestamp >= self.times[key][-1]:
            return self.values[key][-1]
        i = self._binarySearch(self.times[key], timestamp)
        return self.values[key][i - 1] if i else ""
    
    def _binarySearch(self, values, target):
        left, right = 0, len(values) - 1
        
        while left <= right:
            middle = left + (right - left)//2
            
            if values[middle] == target:
                return middle - 1
            elif values[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        
        return left


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

"""
Notes:

For each key, maintain a list of times and a list of values. We maintain a 1-1 correspondence
between them. We assume that time stamps are monotonically increasing so we can maintain
a sorted times list by just appending. 

To find the latest value before a given timestamp, we can binary search in the times list to
get the index. Then we simply return the value at that index in the values list. 

For the non-built in binary search, note that it's middle - 1 not just middle if we hit the
target...this is the case because we want the first value ~before~ the given timestamp. 

"""