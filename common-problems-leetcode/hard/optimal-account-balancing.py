"""
A  group  of  friends  went  on holiday and sometimes lent each other money. For
example, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5 for
a  taxi  ride.  We  can  model each transaction as a tuple (x, y, z) which means
person  x gave person y $z. Assuming Alice, Bill, and Chris are person 0, 1, and
2  respectively  (0,  1,  2  are  the  person's  ID),  the  transactions  can be
represented as [[0, 1, 10], [2, 0, 5]].                                         

Given  a  list  of  transactions  between  a group of people, return the minimum
number of transactions required to settle the debt.                             

Note:                                                                           

A transaction will be given as a tuple (x, y, z). Note that x ≠ y and z > 0.    

Person's  IDs  may  not  be linear, e.g. we could have the persons 0, 1, 2 or we
could also have the persons 0, 2, 6.                                            

Example 1:                                                                      

Input:                                                                          

[[0,1,10], [2,0,5]]                                                             

Output:                                                                         

2                                                                               

Explanation:                                                                    

Person #0 gave person #1 $10.                                                   

Person #2 gave person #0 $5.                                                    

Two transactions are needed. One way to settle the debt is person #1 pays person
#0 and #2 $5 each.                                                              

Example 2:                                                                      

Input:                                                                          

[[0,1,10], [1,0,1], [1,2,5], [2,0,5]]                                           

Output:                                                                         

1                                                                               

Explanation:                                                                    

Person #0 gave person #1 $10.                                                   

Person #1 gave person #0 $1.                                                    

Person #1 gave person #2 $5.                                                    

Person #2 gave person #0 $5.                                                    

Therefore, person #1 only need to give person #0 $4, and all debt is settled.   

"""
# 36ms. 92 percentile.
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
                
        def bfs(balances):
            if len(balances) == 0:
                return 0
            for groupSize in range(2, len(balances) + 1):
                for group in itertools.combinations(list(range(len(balances))), groupSize):
                    if sum([ balances[person] for person in group ]) == 0:
                        balances = [ balance for person,balance in enumerate(balances) if person not in group ]
                        return groupSize - 1 + bfs(balances)

        balances = collections.defaultdict(int)
        for creditor, debtor, amount in transactions:
            balances[creditor] += amount
            balances[debtor] -= amount
        balances = [ balances[person] for person in balances if balances[person] != 0]

        return bfs(balances)



# 32ms. 97 percentile.
# Repeated BFS to find "circles"
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
                
        def bfs(balances):
            debtToSettle = balances[0]
            queue = collections.deque([(debtToSettle, [0], 1)])
            
            while queue:
                debtToSettle, path, startIndex = queue.popleft()
                if debtToSettle == 0:
                    balances = [ x for i,x in enumerate(balances) if i not in path ]
                    paymentsRequiredToSettle = len(path) - 1
                    return paymentsRequiredToSettle, balances
                else:
                    for i in range(startIndex, len(balances)):
                        queue.append( (debtToSettle + balances[i], path + [i], i + 1) )

        balances = collections.defaultdict(int)
        for creditor, debtor, amount in transactions:
            balances[creditor] += amount
            balances[debtor] -= amount
        
        balances = [ balances[person] for person in balances if balances[person] != 0]

        totalPayments = 0
        while 0 < len(balances):
            paymentsMade, balances = bfs(balances)
            totalPayments += paymentsMade
        
        return totalPayments


"""
Notes:

This  question  looks  simple  at first, but it's a lot more complicated than it
looks. The can of worms is opened when you ponder an example like this:         

There  are  2  people who are each owed money by 5 others. The 5 debtors can pay
the   creditors   what  they  owe.  That's  2  transactions  per  debtor  ->  10
transactions.  However,  say one creditor paid the other everything she is owed.
Then  the 5 debtors only have to pay their entire debts to the one creditor owed
money. Ojala, 6 transactions.                                                   

Long  story  short,  this  is  going to be solved with a pretty straightforwards
algorithm,  but  it's  an  NP-complete  problem  and  it'll  be  computationally
intractable to get the optimal answer for large N.                              

In more detail:                                                                 

We  don't really care about who owes who money. All we care about are everyone's
balances and getting them all to 0.                                             

A  practical  solution  that  works for a lot of real life problems is to simply
make  one  person  the bank. All the people with exta money send all their extra
money  to  the  bank. And the bank pays everyone owed money what they need. That
yields  O(N)  transactions  where  N  is  the number of people (balances). Super
simple.                                                                         

But this doesn't guarantee optimality. Super easy to see this. Imagine balance A
is  +5 and balance B is -5. With the central bank strategy, A sends money to the
bank  which  sends  money  to  B,  so  2  transactions. However, if A and B just
transacted, it would be only 1 to settle.                                       

To  pursue an opimal solution, we can think of this as a directed graph problem.
Each  node  is  a  balance.  We  can draw arrows to challenge those balances. An
outgoing  arror  with  a  positive  number  decreases the node's balance, and an
incoming  arrow increases it. Therefore the number of arrows indicate the number
of transactions, and for this problem we want to minimize those.                

Basically  we  can  quickly come up with some graph that balances all the nodes.
Then  we  can transform that graph in an attempt to reduce the number of arrows.
For  example,  if  there's  a  cycle,  we  could  decrease all the arrows by the
magnitude of the smallest edge. That eliminates the smallest edge.              

Now  it turns out, you can think of this as attempting to maximize the number of
components  (because minimizing the number of arrows is equivalent to maximizing
the number of components.) More specifically, you want to find a partition of the
points  such  that each part has a total balance of zero and the number of parts
is  maximized.  This  is  intuitivelly  supported  by thinking about taking this
process to its extreme:                                                         

-Eliminate all initial 0 balances                                               

-Organize  all  the  balances  into  pairs  where each pair has a positive and a
negative  that  perfectly balance. In that case we have N/2 transactions...which
is  as  small  as we can have...and we have as many components as we can without
destroying the 0-balance property.                                              

Unfortunately,  this is the subset problem: for each negative, we need to find a
subset  sum  of  the  others  that  is equal in magnitude and positive. So yeah,
NP-complete, sad.                                                               

Fortunately, this does imply a straightforward, albeit slow solution.            

We  know  that  we  components  consiting  of  2 nodes move us toward an optimal
solution.  So  we  find all the 2-node components we can. At that point, we know
that all the 3 node components move us towards an optimal solution...and so on. 

How do we translate this to code? 

No matter what, we start with creating an array showing the net amount owed 
to/from each person. 

Then: 

Approach 1) 
Actually find all "circles" of 2, then 3, and so on.
Combinations.itertools in python makes this straightforwards.
In the implementation above, note that the return statement in bfs
prevents bfs from branching into tree...so its effectively a for
loop (recursion with just one child of each level)

Approach 2)
we can use a series of bfs's to find the smallest "circles". Then we run a bfs
that tries to find a path through the various amounts that sums to 0. When we
find it, it must be the shortest path involving that sum. So we eliminate all 
members of the path and add the number of steps to the total number of steps
in that path. 
"""