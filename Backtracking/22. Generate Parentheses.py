"""
1. Clarification
2. Possible solutions
    - Brute force
    - Backtracking
3. Coding
4. Tests
"""


# T=O(n*4^n), S=O(n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.ans = []
        self.backtrack([])
        return self.ans

    def backtrack(self, A):
        if len(A) == 2 * self.n:
            if self.valid(A):
                self.ans.append(''.join(A))
        else:
            A.append('(')
            self.backtrack(A)
            A.pop()
            A.append(')')
            self.backtrack(A)
            A.pop()

    def valid(self, A):
        bal = 0
        for c in A:
            if c == '(': bal += 1
            else: bal -= 1
            if bal < 0: return False
        return bal == 0


# T=O(4^n/sqrt(n)), S=O(n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.lst = []
        self.backtrack(0, 0, n, '')
        return self.lst

    def backtrack(self, left, right, n, result):
        if left == n and right == n:
            self.lst.append(result)
            return
        if left < n:
            self.backtrack(left + 1, right, n, result + '(')
        if left > right and right < n:
            self.backtrack(left, right + 1, n, result + ')')
