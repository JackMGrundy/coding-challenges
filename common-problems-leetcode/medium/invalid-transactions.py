"""
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes), amount, and city of the transaction.

Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.

 

Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]
 

Constraints:

transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000.
"""
# Brute force
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalidTransactions = []
        
        for i,transactionString in enumerate(transactions):
            name, time, amount, city = transactionString.split(",")
            transactions[i] = [ name, int(time), int(amount), city ]
        
        for [thisName, thisTime, thisAmount, thisCity] in transactions:
            
            if 1000 < thisAmount:
                invalidTransactions.append(','.join([ thisName, str(thisTime), str(thisAmount), thisCity]))
            else:
                for [thatName, thatTime, thatAmount, thatCity] in transactions:
                    if thisName == thatName and abs(thisTime - thatTime) <= 60 and thisCity != thatCity:
                        invalidTransactions.append( ','.join([ thisName, str(thisTime), str(thisAmount), thisCity]) )
                        break
        
        return invalidTransactions



"""
Notes:

Good question. The 1000+ requirement is simple. The transactions in different cities is more interesting. We
can break the transactions into different groups by name. Then within groups, for each transaction we want to know the last and next
transactions IN A DIFFERENT CITY. This means we can't simply sort and then run through the list...

Easiest thing to do is just brute force it.

If you wanted to try something more complicated...
We can sort by name, then city, and then time. Then for each transaction, first check if its amount is greater than 1000.

If not, then the most complicated case. Go back through the list and for each, find the temporally closest
pre and post event with the same name but different city

"""