/*
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.

 

Example 1:

Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
Example 2:

Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91
 

Constraints:

1 <= boxTypes.length <= 1000
1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
1 <= truckSize <= 106
*/


// First attempt
// 88th percentile
#include <vector>
#include <algorithm>

class Solution {
public:
    int maximumUnits(std::vector<std::vector<int>>& boxTypes, int truckSize) {
        std::sort(boxTypes.begin(), boxTypes.end(), [](auto& a, auto& b) { return b[1] < a[1];});
        int ans = 0;
        for (auto& boxType : boxTypes) {
            int count = std::min(boxType[0], truckSize);
            ans += count * boxType[1], truckSize -= count;
			if (!truckSize) return ans;
        }
        return ans;
    }
};


/*
Good example of C++ labmda functions

https://docs.microsoft.com/en-us/cpp/cpp/lambda-expressions-in-cpp?view=msvc-170


Parts of a lambda expression
The ISO C++ Standard shows a simple lambda that is passed as the third argument to the std::sort() function:

C++

Copy
#include <algorithm>
#include <cmath>

void abssort(float* x, unsigned n) {
    std::sort(x, x + n,
        // Lambda expression begins
        [](float a, float b) {
            return (std::abs(a) < std::abs(b));
        } // end of lambda expression
    );
}
This illustration shows the parts of a lambda:

An illustration of the structural elements of a lambda expression.

capture clause (Also known as the lambda-introducer in the C++ specification.)

parameter list Optional. (Also known as the lambda declarator)

mutable specification Optional.

exception-specification Optional.

trailing-return-type Optional.

lambda body.

Capture clause
A lambda can introduce new variables in its body (in C++14), and it can also access, or capture, variables from the surrounding scope. A lambda begins with the capture clause. It specifies which variables are captured, and whether the capture is by value or by reference. Variables that have the ampersand (&) prefix are accessed by reference and variables that don't have it are accessed by value.

An empty capture clause, [ ], indicates that the body of the lambda expression accesses no variables in the enclosing scope.

You can use a capture-default mode to indicate how to capture any outside variables referenced in the lambda body: [&] means all variables that you refer to are captured by reference, and [=] means they're captured by value. You can use a default capture mode, and then specify the opposite mode explicitly for specific variables. For example, if a lambda body accesses the external variable total by reference and the external variable factor by value, then the following capture clauses are equivalent:

C++

Copy
[&total, factor]
[factor, &total]
[&, factor]
[factor, &]
[=, &total]
[&total, =]
Only variables that are mentioned in the lambda body are captured when a capture-default is used.

If a capture clause includes a capture-default &, then no identifier in a capture of that capture clause can have the form &identifier. Likewise, if the capture clause includes a capture-default =, then no capture of that capture clause can have the form =identifier. An identifier or this can't appear more than once in a capture clause. The following code snippet illustrates some examples:

C++

Copy
struct S { void f(int i); };

void S::f(int i) {
    [&, i]{};      // OK
    [&, &i]{};     // ERROR: i preceded by & when & is the default
    [=, this]{};   // ERROR: this when = is the default
    [=, *this]{ }; // OK: captures this by value. See below.
    [i, i]{};      // ERROR: i repeated
}
A capture followed by an ellipsis is a pack expansion, as shown in this variadic template example:

C++

Copy
template<class... Args>
void f(Args... args) {
    auto x = [args...] { return g(args...); };
    x();
}
To use lambda expressions in the body of a class member function, pass the this pointer to the capture clause to provide access to the member functions and data members of the enclosing class.

Visual Studio 2017 version 15.3 and later (available in /std:c++17 mode and later): The this pointer may be captured by value by specifying *this in the capture clause. Capture by value copies the entire closure to every call site where the lambda is invoked. (A closure is the anonymous function object that encapsulates the lambda expression.) Capture by value is useful when the lambda executes in parallel or asynchronous operations. It's especially useful on certain hardware architectures, such as NUMA.

For an example that shows how to use lambda expressions with class member functions, see "Example: Using a lambda expression in a method" in Examples of lambda expressions.

When you use the capture clause, we recommend that you keep these points in mind, particularly when you use lambdas with multi-threading:

Reference captures can be used to modify variables outside, but value captures can't. (mutable allows copies to be modified, but not originals.)

Reference captures reflect updates to variables outside, but value captures don't.

Reference captures introduce a lifetime dependency, but value captures have no lifetime dependencies. It's especially important when the lambda runs asynchronously. If you capture a local by reference in an async lambda, that local could easily be gone by the time the lambda runs. Your code could cause an access violation at run time.

Generalized capture (C++ 14)
In C++14, you can introduce and initialize new variables in the capture clause, without the need to have those variables exist in the lambda function’s enclosing scope. The initialization can be expressed as any arbitrary expression; the type of the new variable is deduced from the type produced by the expression. This feature lets you capture move-only variables (such as std::unique_ptr) from the surrounding scope and use them in a lambda.

C++

Copy
pNums = make_unique<vector<int>>(nums);
//...
      auto a = [ptr = move(pNums)]()
        {
           // use ptr
        };

*/
