/*
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
*/

// 112 ms. 87th percntile.
/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {
    if (n < 3) {
        return 0;
    }
    
    let primes = new Array(n).fill(true);
    primes[0] = false;
    primes[1] = false;
    
    for (let i = 2; i < Math.sqrt(n)+1; i++) {
        if (primes[i]) {
            for (let j = i*i; j < n; j = j+i) {
                primes[j] = false;
            }
        }
    }
    
    return primes.slice(0, n).reduce( (a,b) => {
        return a + (b === true);
    }, 0);
};

