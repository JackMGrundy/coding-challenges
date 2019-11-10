"""
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
"""

# 44ms. 99.8 percentile.
# constant write, linear read
# fast due to small constant factors
# and builtins speed
class LogSystem:

    def __init__(self):
        self.logs = []
        self.granularityPrecisions = { 'Year':4,
                                       'Month':7,
                                       'Day':10,
                                       'Hour':13,
                                       'Minute':16,
                                       'Second':19,}
        
    def put(self, id: int, timestamp: str) -> None:
        self.logs.append( (timestamp, id) )

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        precision = self.granularityPrecisions[gra]
        s, e = s[:precision], e[:precision]
        return [ i for timestamp, i in self.logs if s <= timestamp[:precision] <= e ]


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)






# 44ms. 99.8 percentile.
# log(n) read and write time
from bisect import insort, bisect_left, bisect_right
class LogSystem:

    def __init__(self):
        self.logs = []
        self.granularityPrecisions = { 'Year':4,
                                       'Month':7,
                                       'Day':10,
                                       'Hour':13,
                                       'Minute':16,
                                       'Second':19,}
        
        self.end = "2017:12:31:23:59:59"
        self.start = "2000:01:01:00:00:00"
        
    
    def setPrecision(self, timestamp, gra, roundUp):
        precision = self.granularityPrecisions[gra]
        if roundUp:
            return timestamp[:precision] + self.end[precision:]
        else:
            return timestamp[:precision] + self.start[precision:]
    
    
    def put(self, id: int, timestamp: str) -> None:
        insort(self.logs, (timestamp, id) )

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        s = self.setPrecision(s, gra, False)
        e = self.setPrecision(e, gra, True)
        left = bisect_left( self.logs, (s, -float("inf")) )
        right = bisect_right( self.logs, (e, float("inf")))
        
        if len(self.logs) < left:
            return []
        
        return [ log[1] for log in self.logs[left:right] ]


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)




"""
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


"""