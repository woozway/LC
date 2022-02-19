"""
1. Clarification
2. Possible solutions
    - Backtracking
3. Coding
4. Tests
"""


# T=O(3^n * 4^m), S=O(3^n * 4^m)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        self.digit2alpha = { '2': 'abc', '3': 'def', '4': 'ghi',
                             '5': 'jkl', '6': 'mno', '7': 'pqrs',
                             '8': 'tuv', '9': 'wxyz'}
        self.ans = []
        self.tmp = []
        self.backtrack(digits, 0)
        return self.ans

    def backtrack(self, digits, idx):
        if idx == len(digits):
            self.ans.append(''.join(self.tmp))
            return
        s = self.digit2alpha[digits[idx]]
        for c in s:
            self.tmp.append(c)
            self.backtrack(digits, idx + 1)
            self.tmp.pop()
