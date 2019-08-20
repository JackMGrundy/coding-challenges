/*
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
*/
// 14th percentile. 2ms
// Iterative
// would be better with a pairs class...recursive is better anyways
import java.util.*;
class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        Queue<List<Integer>> queue = new LinkedList<List<Integer>>();
        List<Integer> start = new ArrayList<>();
        start.add(sr);
        start.add(sc);
        queue.add(start);
        int oldColor = image[sr][sc];
        List<Integer> current;
            
        while (queue.size() > 0) {
            current = queue.remove();
            sr = current.get(0);
            sc = current.get(1);
            if (0 <= sr && sr < image.length && 0 <= sc && sc < image[0].length && 
                image[sr][sc] != newColor && image[sr][sc] == oldColor) {
                
                image[sr][sc] = newColor;
                
                List<Integer> down = new ArrayList<Integer>();
                down.add(sr+1);
                down.add(sc);
                queue.add(down);
                
                List<Integer> up = new ArrayList<Integer>();
                up.add(sr-1);
                up.add(sc);
                queue.add(up);

                List<Integer> right = new ArrayList<Integer>();
                right.add(sr);
                right.add(sc+1);
                queue.add(right);

                List<Integer> left = new ArrayList<Integer>();
                left.add(sr);
                left.add(sc-1);
                queue.add(left);
            }
        }
        
        return image;
    }
}


// 0ms. 100th percentile.
// Recursive
class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        dfs(image, sr, sc, newColor, image[sr][sc]);
        return image;
    }
    
    public void dfs(int[][]image, int sr, int sc, int newColor, int oldColor) {
        if (0 <= sr && sr < image.length && 0 <= sc && sc < image[0].length &&
            image[sr][sc] != newColor && image[sr][sc] == oldColor) {
            image[sr][sc] = newColor;
            dfs(image, sr+1, sc, newColor, oldColor);
            dfs(image, sr-1, sc, newColor, oldColor);
            dfs(image, sr, sc+1, newColor, oldColor);
            dfs(image, sr, sc-1, newColor, oldColor);
        }
    }
}