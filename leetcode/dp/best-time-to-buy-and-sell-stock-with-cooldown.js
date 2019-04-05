/*
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
*/

// 1st attempt: 86th percentile
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let hold = -Number.MAX_SAFE_INTEGER,
        notHold = 0,
        cooldown = -Number.MAX_SAFE_INTEGER;
    prices.map(p => {
        let temp = hold;
        hold = Math.max(hold, notHold-p);
        notHold = Math.max(notHold, cooldown);
        cooldown = temp + p;
    })
    
    return Math.max(notHold, cooldown);
};