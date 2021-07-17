"""
1. Clarification
2. Possible solutions
     - Python built-in
3. Coding
4. Tests
"""


# T=O(n), S=O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s: return ''
        return ' '.join(word[::-1] for word in s.split())
