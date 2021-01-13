"""
1. Clarification
2. Possible solutions
 - replace adjacent matched brackets
 - use stack to match brackets
3. Coding
4. Tests
"""

# # T=O(n^2), S=O(1)
# class Solution:
#     def isValid(self, s: str) -> bool:
#         while '()' in s or '[]' in s or '{}' in s:
#             s = s.replace('()', '').replace('[]', '').replace('{}', '')
#         return s == ''

# T=O(n), S=O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_map = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c not in paren_map:
                stack.append(c)
            elif not stack or paren_map[c] != stack.pop():
                return False
        return not stack
