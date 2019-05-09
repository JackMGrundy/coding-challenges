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
// 38th percentile. 56ms. 
// Simple O(Nlog(N)) solution
import java.util.Arrays;
class Solution {
    public int[][] kClosest(int[][] points, int K) {
        Arrays.sort(points, (a, b) -> Double.compare( Math.pow(a[0], 2)+Math.pow(a[1], 2), Math.pow(b[0], 2)+Math.pow(b[1], 2)));
        return Arrays.copyOfRange(points, 0, K);
    }
}



// 96th percentile ms
class Solution {
    
    public int compare(int[] pointA, int[] pointB) {
        return Double.compare(Math.pow(pointA[0], 2)+Math.pow(pointA[1], 2), Math.pow(pointB[0], 2)+Math.pow(pointB[1], 2));
    }
    
    public int partition(int[][] points, int low, int high) {
        int i = low-1;
        for (int j = low; j <= high; j++) {
            if ( 0 >=  compare(points[j], points[high])  ) {
                i += 1;
                int[] temp = points[j];
                points[j] = points[i];
                points[i] = temp;
            }
        }
        return i;
    }
    
    public void qSort(int[][] points, int low, int high, int k) {
        if (low < high ) {
            int p = partition(points, low, high);
            if (p==k) {
                return;
            } 
            else if (p < k) {
                qSort(points, p, high, k);
            }
            else if (p > k) {
                qSort(points, low, p-1, k);
            }
        }
        return;
    }
    
    public int[][] kClosest(int[][] points, int K) {
    qSort(points, 0, points.length-1, K);
    return Arrays.copyOfRange(points, 0, K);
    }
}