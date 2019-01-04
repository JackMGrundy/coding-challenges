#!/bin/python3
import math
import os
import random
import re
import sys
import queue

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    # Edge cases
    if len(expenditure)<d+1:
        return(0)
    
    # LIFO queue
    q = queue.Queue(maxsize=d)

    # 0 to 200 int list for counting sort
    # index starting at 1 rather than 0
    counts = [0]*201

    # Initialize
    for i in range(d):
        counts[expenditure[i]]+=1
        q.put(expenditure[i])
    
    def median(counts, n):
        """
        Given a list of counts where index indicates value and element value indicates count,
        return the median value
        """
        # Median is average of two middlemost values        
        if n%2==0:
            med = 0

            targetVal = n//2
            check = 0
            for i in range(len(counts)):
                check += counts[i]
                if check>targetVal or check==targetVal:
                    med += i
                    break

            targetVal = 1+n//2
            check = 0
            for i in range(len(counts)):
                check += counts[i]
                if check>targetVal or check==targetVal:
                    med += i
                    break

            return(med/2.0)

        # Median is middlemost value
        elif n%2==1:
            check = 0
            targetVal = 1+n//2
            for i in range(len(counts)):
                check += counts[i]
                if check>targetVal or check==targetVal:
                    return(i)

    # Rest of days
    notifications = 0
    for i in range(d, len(expenditure)):
        curExpenditure = int(expenditure[i])

        trailingMedianExp = median(counts, d)

        if (curExpenditure>2*trailingMedianExp) or (curExpenditure==2*trailingMedianExp): 
            notifications+=1

        # Update queue
        poppedExpenditure = q.get()
        q.put(curExpenditure)

        # Update counts
        counts[poppedExpenditure] -= 1
        counts[curExpenditure] += 1

    return(notifications)

if __name__ == '__main__':
    d = 2
    expenditure = [10, 20, 30, 40, 50]
    res = activityNotifications(expenditure, d)
    print(res)