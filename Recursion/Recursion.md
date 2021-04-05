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
## Paradigms that are often applied together with the recursion:
1. divide-and-conquer (D&C)
   - D&C algorithm is that we break the problem down into **two or more subproblems** rather than a single smaller subproblem. The latter recursive algorithm sometimes is called **decrease and conquer** instead, such as Binary Search.
   - general three steps:
     1. **Devide**: Divide the problem S into a set of subproblems: {S1, S2, ... Sn} where n >= 2
     2. **Conquer**: Solve each subproblem recursively. 
     3. **Combine**: Combine the results of each subproblem.
   - D&C template:
   ```python
    def divide_and_conquer( S ):
        # (1). Divide the problem into a set of subproblems.
        [S1, S2, ... Sn] = divide(S)

        # (2). Solve the subproblem recursively,
        #   obtain the results of subproblems as [R1, R2... Rn].
        rets = [divide_and_conquer(Si) for Si in [S1, S2, ... Sn]]
        [R1, R2,... Rn] = rets

        # (3). combine the results from the subproblems.
        #   and return the combined result.
        return combine([R1, R2,... Rn])
   ```
