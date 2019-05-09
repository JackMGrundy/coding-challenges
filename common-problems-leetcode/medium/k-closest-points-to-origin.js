/*
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 

Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
*/

// 79th percentile
// O(log(N))...built in methods
/**
 * @param {number[][]} points
 * @param {number} K
 * @return {number[][]}
 */
var kClosest = function(points, K) {
    points.sort( (pointA, pointB) => (pointA[0]**2 + pointA[1]**2) - (pointB[0]**2 + pointB[1]**2));
    return points.slice(0, K);
};

// 86th percentile
/*
O(N) on average. 
Quick sort...but only sort until we have partition with K items on the left 
less than the partition.
*/
/**
 * @param {number[][]} points
 * @param {number} K
 * @return {number[][]}
 */
var kClosest = function(points, K) {
    if (points.length <= K) return points;
    points.forEach( (point, i) => {
         points[i] = [ point[0]**2 + point[1]**2, point[0], point[1] ];
    })
    
    var partition = function(arr, low, high) {
        let i = low - 1;
        
        for (let j = low; j <= high; j++) {
            if (arr[j][0] <= arr[high][0]) {
                i++;
                let temp = arr[j];
                arr[j] = arr[i];
                arr[i] = temp;
            }            
        }
        return i;
    }
    
    var qSort = function(arr, low, high) {
        if (low < high) {
            let p = partition(arr, low, high);
            
            if (p === K) return;
            else if (p < K) qSort(arr, p+1, high);
            else if (p > K) qSort(arr, low, p-1)   
        }
    }
    
    qSort(points, 0, points.length-1);
    points.forEach( (point, i) => {
        points[i] = [point[1], point[2]];
    })
    return points.slice(0, K);
};



// 99th percentile
/*
lesson: it's easier to think of calculating the comparison value for every item before
starting...but it can be faster to do the comparison calculations on the fly...
especially if it reduces the number of calculations. 
*/
/**
 * @param {number[][]} points
 * @param {number} K
 * @return {number[][]}
 */
var kClosest = function(points, K) {
    if (points.length <= K) return points;
    
    var comparePoints = function(pointA, pointB) {
        return (pointA[0]**2 + pointA[1]**2) <= (pointB[0]**2 + pointB[1]**2)
    }
    
    var partition = function(arr, low, high) {
        let i = low - 1;
        
        for (let j = low; j <= high; j++) {
            if ( comparePoints(arr[j], arr[high]) ) {
                i++;
                let temp = arr[j];
                arr[j] = arr[i];
                arr[i] = temp;
            }            
        }
        return i;
    }
    
    var qSort = function(arr, low, high) {
        let p = partition(arr, low, high);

        if (p === K) return;
        else if (p < K) qSort(arr, p+1, high);
        else if (p > K) qSort(arr, low, p-1)   
    }
    
    qSort(points, 0, points.length-1);
    return points.slice(0, K);
};