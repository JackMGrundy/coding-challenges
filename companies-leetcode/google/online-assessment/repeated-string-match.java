/*
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
*/
// 1st attmept: 82nd percentile
class Solution {
    public int repeatedStringMatch(String A, String B) {
        int x = (int) Math.ceil( ( (float) B.length() ) / A.length() );
        String repeated = new String(new char[x]).replace("\0", A);
        if ( repeated.contains(B) ) {
            return x;
        }
        repeated += A;
        if ( repeated.contains(B) ) {
            return x+1;
        }
        return(-1);
    }
}