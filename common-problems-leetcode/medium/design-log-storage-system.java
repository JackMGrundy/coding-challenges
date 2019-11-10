/*
You are given several logs that each log contains a unique id and timestamp. Timestamp is 
a string that has the following format: Year:Month:Day:Hour:Minute:Second, for example, 
2017:01:01:23:59:59. All domains are zero-padded decimal numbers.

Design a log storage system to implement the following functions:

void Put(int id, string timestamp): Given a log's unique id and timestamp, store the log 
in your storage system.


int[] Retrieve(String start, String end, String granularity): Return the id of logs whose 
timestamps are within the range from start to end. Start and end all have the same format 
as timestamp. However, granularity means the time level for consideration. For example, 
start = "2017:01:01:23:59:59", end = "2017:01:02:23:59:59", granularity = "Day", it means 
that we need to find the logs within the range from Jan. 1st 2017 to Jan. 2nd 2017.

Example 1:
put(1, "2017:01:01:23:59:59");
put(2, "2017:01:01:22:59:59");
put(3, "2016:01:01:00:00:00");
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"); // return [1,2,3], because 
you need to return all logs within 2016 and 2017.
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"); // return [1,2], because 
you need to return all logs start from 2016:01:01:01 to 2017:01:01:23, where log 3 is 
left outside the range.

Note:
There will be at most 300 operations of Put or Retrieve.
Year ranges from [2000,2017]. Hour ranges from [00,23].
Output for Retrieve has no order required.
*/




/*

Notes:

Typically read vs write tradeoff scenario. We could easily store in constant time and then
do a linear time filter to get all the requested times. However, that linear time
read can be a deal breaker. 

Per usual with data stores, we can come up with some scheme that's log(n) for both. 

Strategy:

Immediate thought is to convert the values to numbers. However, while the granularity
requirement is a bit annoying, it makes this process easier. 

For Python, we can just compare the strings as is...

For Java, 

Convert the values to numbers...use an insort type method (under the hood it's a 
linkedlist with binary sort to find insertion points) to insert the timestamps in log time.

For reading, we can simply use a pair of binary searches to find the left and right limits
of the range we want.

The tricky bits:

1) Granularity: It's a bit ugly but we can simply cut the timestamps down to a certain 
number of characters based on the granularity. 

2) What if we have multiple entries with the same timestamp? This means that instead
of storing each timestamp, we'll need to store lists at for each time stamp, and within
the lists we can store ids. 


*/