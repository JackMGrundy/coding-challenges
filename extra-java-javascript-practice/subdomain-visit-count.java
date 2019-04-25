/*
A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".

We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.

Example 1:
Input: 
["9001 discuss.leetcode.com"]
Output: 
["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
Explanation: 
We only have one website domain: "discuss.leetcode.com". As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.

Example 2:
Input: 
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output: 
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
Explanation: 
We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times. For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.

Notes:

The length of cpdomains will not exceed 100. 
The length of each domain name will not exceed 100.
Each address will have either 1 or 2 "." characters.
The input count in any count-paired domain will not exceed 10000.
The answer output can be returned in any order.
*/
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Arrays;
import java.util.Map;
// 72nd percentile
class Solution {
    public List<String> subdomainVisits(String[] cpdomains) {
        HashMap<String, Integer> counts = new HashMap();
        // Add up counts
        for (int i = 0; i < cpdomains.length; i++) {
            String[] pieces = cpdomains[i].split(" ");  
            String key = pieces[1];
            int count = Integer.parseInt(pieces[0]);
            List<String> domains = new ArrayList<String>(Arrays.asList(key));
            int index = key.indexOf(".");
            while (index != -1) {
                String nxt = key.substring(index+1, key.length());
                domains.add(nxt);
                index = key.indexOf(".", index+1);
            }
            
            for (String domain : domains) {
                if (counts.containsKey(domain)) {
                    counts.put(domain, counts.get(domain)+count);
                } else {
                    counts.put(domain, count);
                }
            }
            

        }
        
        //Convert to list
        List<String> res = new ArrayList<String>();
        for (Map.Entry<String, Integer> entry: counts.entrySet()) {
            res.add("" + entry.getValue() + " " + entry.getKey());
        }
        
        return res;
    }
}

// 100th percntil
class Solution {
    public List<String> subdomainVisits(String[] cpdomains) {
        Map<String, Integer> counts = new HashMap();
        // Add up counts
        for (String cp : cpdomains) {
            int i = cp.indexOf(' ');
            int count = Integer.parseInt(cp.substring(0, i));
            String domains = cp.substring(i+1, cp.length());
            counts.put(domains, counts.getOrDefault(domains, 0) + count);
            
            int period = domains.indexOf(".");
            while (period != -1) {
                String nxt = domains.substring(period+1, domains.length());
                counts.put(nxt, counts.getOrDefault(nxt, 0)+count);
                period = domains.indexOf(".", period+1);
            }
        }

        //Convert to list
        List<String> res = new ArrayList<String>();
        for (String d : counts.keySet()) res.add(counts.get(d) + " " + d);
        return res;
    }
}