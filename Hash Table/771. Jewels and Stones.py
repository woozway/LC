"""
1. Clarification
2. Possible solutions
     - brute force
     - hash
3. Coding
4. Tests
"""


# # T=O(mn), S=O(1)
# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         return sum(s in jewels for s in stones)


# T=O(m+n), S=O(m)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelsSet = set(jewels)
        return sum(s in jewelsSet for s in stones)
