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
   - Master Theorem (or Master Method, it does not apply to all recursion algorithms):
        ```python
        def dac( n ):
            if n < k:  // k: some constant
            Solve "n" directly without recursion
            else:
            [1]. divide the problem "n" into "b" subproblems of equal size.
            - then the size of each subproblem would be "n/b"
            [2]. call the function "dac()" recursively "a" times on the subproblems
            [3]. combine the results from the subproblems
        ```
        - For the recursion algorithms that follow the above pattern, one can apply the master theorem to calculate their time complexity.
        - T(n) = a * T(n/b) + f(n)
        - where `f(n)` is the time complexity that it takes to divide the problems into subproblems and also to combine the results from the subproblems. We can further represent `f(n)` as `O(n^d)` and d >= 0
        - according to the relationship among a, b, d:
        ![master theorem formula](https://github.com/chopchap/leetcode/blob/main/images/Master%20theorem%20formula.png?raw=true)
        - The conditions for each case correspond to the intuition of whether the work to split problems and combine results (i.e. f(n)) outweighs the work of subproblems (i.e. a * T(n/b)).
2. Backtracking (**pruning** the recursion tree)
   - Backtracking is a general algorithm for finding all (or some) solutions (notably Constraint satisfaction problems or CSPs), which incrementally builds candidates to the solution and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot lead to a valid solution.
   - template:
        ```python
        def backtrack(candidate):
        if find_solution(candidate):
            output(candidate)
            return

        # iterate all possible candidates.
        for next_candidate in list_of_candidates:
            if is_valid(next_candidate):
                # try this partial candidate solution
                place(next_candidate)
                # given the candidate, explore further.
                backtrack(next_candidate)
                # backtrack
                remove(next_candidate)
        ```
    - notes:
      - Overall, the enumeration of candidates is done in two levels:
        - 1). at the first level, the function is implemented as recursion. At each occurrence of recursion, the function is one step further to the final solution.
        - 2). as the second level, within the recursion, we have an iteration that allows us to explore all the candidates that are of the same progress to the final solution.
      - The backtracking should happen at the level of the iteration within the recursion.
      - Unlike brute-force search, in backtracking algorithms we are often able to determine if a partial solution candidate is worth exploring further (i.e. `is_valid(next_candidate)`), which allows us to prune the search zones. This is also known as the constraint.
      - There are two symmetric functions that allow us to mark the decision (place(candidate)) and revert the decision (remove(candidate)).
3. Divde and Conquer VS. Backtracking
   - Often the case, the divide-and-conquer problem has a _**sole**_ solution, while the backtracking problem has unknown number of solutions.
   - Each step in the divide-and-conquer problem is indispensable to build the final solution, while many steps in backtracking problem might not be useful to build the solution, but serve as atttempts to search for the potential solutions.
   - When building the solution in the divide-and-conquer algorithm, we have a clear and predefined path, though there might be several different manners to build the path. While in the backtracking problems, one does not know in advance the exact path (or how many steps) to the solution.
