/*
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter.
*/

// 60th percentile
class Solution {
    public String minRemoveToMakeValid(String s) {
        Stack<Integer> st = new Stack<Integer>();
        StringBuilder S = new StringBuilder(s);
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                st.push(i);
            } else if (c == ')') {
                if (st.size() == 0) {
                    S.setCharAt(i, '*');
                } else {
                    st.pop();
                }
            }
        }
        
        while (0 < st.size()) {
            int indexToRemove = st.pop();
            S.setCharAt(indexToRemove, '*');
        }
        
        String answer = S.toString();
        return answer.replaceAll("\\*", "");
    }
}



// 85th percentile
class Solution {
    public String minRemoveToMakeValid(String s) {
        Stack<Integer> st = new Stack<Integer>();
        StringBuilder sb = new StringBuilder(s);
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                st.push(i);
            } else if (c == ')') {
                if (st.size() == 0) {
                    sb.setCharAt(i, '*');
                } else {
                    st.pop();
                }
            }
        }
        
        while (0 < st.size()) {
            int indexToRemove = st.pop();
            sb.setCharAt(indexToRemove, '*');
        }
        
        for (int i = s.length() - 1; 0 <= i; i--) {
            if (sb.charAt(i) == '*') {
                sb.deleteCharAt(i);
            }
        }
        
        return sb.toString();
    }
}


/*
We need the sb business because strings are immutable in java...In python we deal with this by converting strings to lists and then converting them
back to string when we're done. In java we use the stringbuilder class. 


Summary:
    strings are immutable in most languages with c++ being a notable exception, although c++ lets you make immutable strings
    Reasons for this:
        Data structures: we often want to use strings as keys for hash tables or other data structures. Making them immutable protects the integrity of those data structures
        Space/performance: Languages can save space by making only actualy copy of a string ("Hello") and have multiple variables point to that same object
        Synchronization: immutable strings are thread safe
        References: you can pass them around and know they won't change. For exaple, if I have a class that takes in a string and stores it as a class variable,
                    I can know that string won't change. This means we don't have to copy the string repeatedly as it's passed around.
                    So "copying" a string when it's passed around is O(1) instead of O(N)
        
        You don't get much back with mutability:
            searching and concatenation are not really impacted
            Replacing a substring or a single character is the only case that does matter...and for that you can just make a new string or
            use something like string builder.....this does suck a bit because you might have to copy a large string for a small change






Bunch of detail strings being mutable/immutable in different languages ->


Aside....in most languages strings are immutable...but they aren't in c++:
    https://lemire.me/blog/2017/07/07/are-your-strings-immutable/
    Arguably, the most important non-numeric type in software is the string. A string can be viewed as an array of
     characters so it would not be unreasonable to make it mutable, but strings are also viewed as primitive values 
     (e.g., we don’t think of “Daniel” as an array of 6 characters). Consequently, some languages have immutable strings, 
     others have mutable strings. Do you know whether the strings in your favorite language are mutable?

    In Java, C#, JavaScript, Python and Go, strings are immutable. Furthermore, Java, C#, JavaScript and Go have the 
    notion of a constant: a “variable” that cannot be reassigned. (I am unsure how well constants are implemented and supported in JavaScript, however.)
    In Ruby and PHP, strings are mutable.
    The C language does not really have string objects per se. However, we commonly represent strings as a pointer 
    char *. In general, C strings are mutable. The C++ language has its own string class. It is mutable.
    In both C and C++, string constants (declared with the const qualifier) are immutable, but you can easily
    “cast away” the const qualifier, so the immutability is weakly enforced.

    In Swift, strings are mutable.
    However, if you declare a string to be a constant (keyword let), then it is immutable.


Why are strings immutable in most languages?
https://stackoverflow.com/questions/9544182/why-are-strings-immutable-in-many-programming-languages
    Immutable types are a good thing generally:

    They work better for concurrency (you don't need to lock something that can't change!)
    They reduce errors: mutable objects are vulnerable to being changed when you don't expect it which 
    can introduce all kinds of strange bugs ("action at a distance")
    They can be safely shared (i.e. multiple references to the same object) which can reduce memory consumption and improve cache utilisation.
    Sharing also makes copying a very cheap O(1) operation when it would be O(n) if you have to take a defensive
     copy of a mutable object. This is a big deal because copying is an incredibly common operation (e.g. whenever you want to pass parameters around....)
    As a result, it's a pretty reasonable language design choice to make strings immutable.

    Some languages (particularly functional languages like Haskell and Clojure) go even further and make pretty 
    much everything immutable. This enlightening video is very much worth a look if you are interested in the benefits of immutability.

    There are a couple of minor downsides for immutable types:

    Operations that create a changed string like concatenation are more expensive because you need to construct new 
    objects. Typically the cost is O(n+m) for concatenating two immutable Strings, though it can go as
     low as O(log (m+n)) if you use a tree-based string data structure like a Rope. Plus you can always use special tools 
     like Java's StringBuilder if you really need to concatenate Strings efficiently.
    A small change on a large string can result in the need to construct a completely new copy of the large String, 
    which obviously increases memory consumption. Note however that this isn't usually a big issue in garbage-collected languages 
    since the old copy will get garbage collected pretty quickly if you don't keep a reference to it.
    Overall though, the advantages of immutability vastly outweigh the minor disadvantages. Even if you are only interested in performance, the concurrency advantages and cheapness of copying will in general make immutable strings much more performant than mutable ones with locking and defensive copying.




Why are java strings immutable?
https://www.baeldung.com/java-string-immutable


"Strings are immutable precisely so that their references can be treated as a normal variable and one can pass them around,
 between methods and across threads, without worrying about whether the actual String object it's pointing to will change."
        




*/