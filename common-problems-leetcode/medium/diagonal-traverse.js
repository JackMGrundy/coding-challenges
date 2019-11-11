/*
Given a matrix of M x N elements (M rows, N columns), return all elements of the
matrix in diagonal order as shown in the below image.                           

                                                                                

Example:                                                                        

Input:                                                                          

[                                                                               

 [ 1, 2, 3 ],                                                                   

 [ 4, 5, 6 ],                                                                   

 [ 7, 8, 9 ]                                                                    

]                                                                               

Output:  [1,2,4,7,5,3,6,8,9]                                                    

Explanation:                                                                    

                                                                                

Note:                                                                           

The total number of elements of the given matrix will not exceed 10,000.        

*/

// 88ms. 83 percentile.
/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var findDiagonalOrder = function(matrix) {
    if (matrix === null || matrix === undefined || matrix.length === 0) {
        return [];
    }
    
    let M = matrix.length;
    let N = matrix[0].length;
    let r = 0;
    let c = 0;
    let d = 1;
    
    let result = []
    
    for (let i = 0; i < M*N; i++) {
        result.push(matrix[r][c]);
        c += d;
        r -= d;
        
        if (M <= r) {
            r = M - 1;
            c += 2;
            d = -d;
        }
        if (N <= c) {
            c = N - 1;
            r += 2;            
            d = -d;
        }
        if (r < 0) {
            r = 0;
            d = -d;
        }
        if (c < 0) {
            c = 0;
            d = -d;    
        }
    }
    
    return result;
};

/*

Notes:

The solution to this can seem arcane at first. It's actually pretty
intuitive though. Start with the basic facts that we start at spot 0,0
and that whenever we ae traversing a diagonal, we either increment one
of row and column and decrement ther other. This actually gets us 
most of the way there. The tricky part is handling the switch from
one diagonal to another. 

How to make this intuitive? Let the traversal move out of bounds. Then
include ifs at the bottom of each loop that move the pointers back to
the start of the next diagonal. Given this mindset, the equations above
unfold pretty easily. 

*/