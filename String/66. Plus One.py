"""
1. Clarification
2. Possible solutions
     - Str
     - Basic arithmatics
3. Coding
4. Tests
"""


# T=O(n), S=O(1)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits: return []
        return list(map(int, str(int(''.join(map(str, digits))) + 1).zfill(len(digits))))


# # T=O(n), S=O(1)
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         if not digits: return []
#         carryin = 1
#         for i in range(len(digits) - 1, -1, -1):
#             tmp = digits[i] + carryin
#             carryin = tmp // 10
#             digits[i] = tmp % 10
#         if carryin:
#             digits.insert(0, 1)
#         return digits
