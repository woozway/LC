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
        ret = ''
        while columnNumber:
            columnNumber -= 1
            ret += chr(columnNumber%26 + 65)
            columnNumber //= 26
        return ret[::-1]
