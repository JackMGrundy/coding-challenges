/* 
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
*/ 


// 68ms. 83rd percentile.
class MovingAverage {
    Queue<Integer> queue;
    double average;
    int size;
    
    /** Initialize your data structure here. */
    public MovingAverage(int size) {
        this.queue = new LinkedList<Integer>();
        this.average = 0.0;
        this.size = size;
    }
    
    public double next(int val) {
        int removed = 0;
        double currentValue = average*queue.size();
        if (queue.size() == size) {
            removed = queue.remove();
        } 
        queue.add(val);
        
        average = (currentValue + val - removed) / queue.size();
        return average;
    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */