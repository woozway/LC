"""
1. Clarification
2. Possible solutions
    - Brute force
3. Coding
4. Tests
"""


# T=O(n), S=O(1)
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for ch in columnTitle:
            ans = ans*26 + ord(ch)-ord('A') + 1
        return ans
