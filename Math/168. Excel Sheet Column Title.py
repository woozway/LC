"""
1. Clarification
2. Possible solutions
    - Maths
3. Coding
4. Tests
"""


# T=O(lg26 * columnNumber), S=O(lg26 * columnNumber)
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = list()
        while columnNumber > 0:
            columnNumber -= 1
            ans.append(chr(columnNumber % 26 + ord("A")))
            columnNumber //= 26
        return ''.join(ans[::-1])
