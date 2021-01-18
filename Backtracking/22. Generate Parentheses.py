"""
1. Clarification
2. Possible solutions
 - brute force
 - dfs, backtracking
3. Coding
4. Tests
"""

# # T=O(n*4^n), S=O(n)
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         self.n = n
#         self.ans = []
#         self.generate([])
#         return self.ans
#
#     def generate(self, A):
#         if len(A) == 2 * self.n:
#             if self.valid(A):
#                 self.ans.append(''.join(A))
#         else:
#             A.append('(')
#             self.generate(A)
#             A.pop()
#             A.append(')')
#             self.generate(A)
#             A.pop()
#
#     def valid(self, A):
#         bal = 0
#         for c in A:
#             if c == '(': bal += 1
#             else: bal -= 1
#             if bal < 0: return False
#         return bal == 0

# T=O(4^n/sqrt(n)), S=O(n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.list = []
        self._gen(0, 0, n, '')
        return self.list

    def _gen(self, left, right, n, result):
        if left == n and right == n:
            self.list.append(result)
            return
        if left < n:
            self._gen(left + 1, right, n, result + '(')
        if left > right and right < n:
            self._gen(left, right + 1, n, result + ')')
