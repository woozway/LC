"""
1. Clarification
2. Possible solutions
    - Divide and Conquer
    - Stack
    - Count Cores
3. Coding
4. Tests
"""


# T=O(n^2), S=O(n)
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        def recursive(i, j):
            ans = bal = 0
            for k in range(i, j):
                bal += 1 if S[k] == '(' else -1
                if bal == 0:
                    if k - i == 1:
                        ans += 1
                    else:
                        ans += 2 * recursive(i + 1, k)
                    i = k+1
            return ans

        return recursive(0, len(S))


# T=O(n), S=O(n)
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        for x in S:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)
        return stack.pop()


# T=O(n), S=O(1)
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        ans = bal = 0
        for i, x in enumerate(S):
            if x == '(':
                bal += 1
            else:
                bal -= 1
                if S[i-1] == '(':
                    ans += 1 << bal
        return ans
