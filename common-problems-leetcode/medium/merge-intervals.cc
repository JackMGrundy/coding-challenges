/*
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
*/
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;


// 1st attempt: 12ms. 99th percentile.
#include <algorithm>
#include <iostream>

class Compare {
public:
    bool operator () (vector<int>& vec1, vector<int>& vec2) {
        return vec1[0] < vec2[0];
    }
};

Compare CompObject;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty()) return {};
        vector<vector<int>> mergedIntervals;
        int n = intervals.size();
        mergedIntervals.reserve(n); // Great, simple technique for improving performance
        
        std::sort(intervals.begin(), intervals.end(), CompObject);
        
        mergedIntervals.push_back(intervals[0]);
                
        for (auto const &it : intervals) { // Note this syntax for working with the originals and ensuring we don't change them
                
            if (it[0] <= mergedIntervals.back()[1]) {
                mergedIntervals.back()[1] = std::max(mergedIntervals.back()[1], it[1]);
            } else {
                mergedIntervals.push_back(it);
            }
        }
        
        return mergedIntervals;
    }
};



// 2nd attempt: 72ms. 19th percentile.
// Lambda expression
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty()) return {};
        vector<vector<int>> mergedIntervals;
        int n = intervals.size();
        mergedIntervals.reserve(n);
        
        std::sort(intervals.begin(), intervals.end(), [](std::vector<int> a, std::vector<int> b){return a[0] < b[0];});
        
        mergedIntervals.push_back(intervals[0]);
                
        for (auto const &it : intervals) {
                
            if (it[0] <= mergedIntervals.back()[1]) {
                mergedIntervals.back()[1] = std::max(mergedIntervals.back()[1], it[1]);
            } else {
                mergedIntervals.push_back(it);
            }
        }
        
        return mergedIntervals;
    }
};


/*
Notes:

The great second solution is possible because of the initial sorting
During the iteration, we know that each successive interval has a start 
after that of the interval on top of the stack. Therefore, we can simply check if
the current interval's start is less than the end of the intervals on top 
of the stack.

Note the vector.reserve technique...good, simple performance booster

And note the syntax of the range loop...ensures we work with references and don't change
the original intervals
*/