/*

Suppose  you  have  a  random list of people standing in a queue. Each person is
described  by a pair of integers (h, k), where h is the height of the person and
k is the number of people in front of this person who have a height greater than
or equal to h. Write an algorithm to reconstruct the queue.                     

Note:                                                                           

The number of people is less than 1,100.                                        

                                                                                

Example                                                                         

Input:                                                                          

[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]                                      

Output:                                                                         

[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]                                      


*/

// 7ms. 71 percentile.
class Solution {
    public int[][] reconstructQueue(int[][] people) {
        
        Arrays.sort(people, new Comparator<int[]>() {
           
            @Override
            public int compare(int[] thisPerson, int[] thatPerson) {
                int thisPersonHeight = thisPerson[0];
                int thatPersonHeight = thatPerson[0];
                int thisPersonK = thisPerson[1];
                int thatPersonK = thatPerson[1];
                
                return thisPersonHeight == thatPersonHeight ? thisPersonK - thatPersonK : thatPersonHeight - thisPersonHeight; 
            }
        });
        
        List<int[]> reconstructedQueue = new LinkedList<>();
        for (int[] person : people) {
            reconstructedQueue.add(person[1], person);
        }
        
        
        return reconstructedQueue.toArray(new int[reconstructedQueue.size()][2]);
    }
}



/*

Notes:

Sort descending by height. Then within height groups, sorted ascending
by # of people in front of them equal or taller. 

For each height group:

    Deposit each person into the index corresponding to their K value. 
    If a person is already in that slot, push the person and all slots
    one element down to make room.


Intuition:
    This algorithm breaks the people into "height" groups, processing the
    bigger ones first. For the first group, it's obvious what subsequence
    the people appear in...no one in any of the other groups can contribute
    to the k values for the people in this biggest group.

    We can see the key part of the intuition when we imagine processing the 
    second tallest group. We know that the only people who can contribute to
    the k values of this group are the people in the same group or in the
    bigger group. 

    Therefore, the k values of each person in this second tallest group
    actually give us the locations of the people within the subset of people
    already considered.

    ^That's the key intuition. Given this, it's simple to see that we can
    simply process a group at a time until they are all accounted for. 

*/