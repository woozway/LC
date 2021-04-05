# Recursion
---
## Principle of Recursion
1. A simple _**base case**_ (or cases) — a terminating scenario
2. A set of rules, also known as _**recurrence relation**_ that reduces all other cases towards the base case
## Recursion Function
1. Break the problem down into smaller scopes: x0, x1, ..., xn
2. Call function (F(x0), ..., F(xn)) recursively to solve the subproblems of X
3. Finally, process the results from the recursive function calls to solve the problem corresponding to X
## Conclusion I:
1. When in doubt, write down the recurrence relationship.
2. Whenever possible, apply memoization. (optimize the time complexity)
3. When stack overflows, tail recursion might come to help. (optimize the space complexity)
