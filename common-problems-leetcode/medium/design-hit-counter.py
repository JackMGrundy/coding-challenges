"""
Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

Example:

HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301); 
Follow up:
What if the number of hits per second could be very large? Does your design scale?
"""

# 30ms. 77th percentile.
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.times = [0 for _ in range(300)]
        self.hits =  [0 for _ in range(300)]
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        lastTime = self.times[timestamp%300]
        if timestamp == lastTime:
            self.hits[timestamp%300] += 1
        else:
            self.hits[timestamp%300] = 1
        
        self.times[timestamp%300] = timestamp
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        res = 0
        for i in range(300):
            if timestamp-300 < self.times[i]:
                res += self.hits[i]
        return res
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)



# Obnoxiously short. 40ms. 50th percentile...not readable/good code
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.times = [0 for _ in range(300)]
        self.hits =  [0 for _ in range(300)]
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.hits[timestamp%300] = 1 if timestamp != self.times[timestamp%300] else self.hits[timestamp%300]+1
        self.times[timestamp%300] = timestamp
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        return sum( [self.hits[x] for x in range(300) if timestamp-300 < self.times[x] ] )

        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)


"""
Notes
My immediate inclination was to do an invalidation scheme where I would record the last time
and then by comparing it with the new timestamp, determine what sections of the counter to 
invalidate. It's much easier if you just allocate an extra 300 element array of times. 

Could also do a queue...whenever you add a new element or get hits, just keep popping off expired elements until the queue
only has fresh hits.
"""