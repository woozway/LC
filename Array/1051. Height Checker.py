"""
1. Clarification
2. Possible solutions
 - sort
3. Coding
4. Tests
"""


# T=O(nlgn), S=O(n)
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        if not heights: return 0
        a = sorted(heights)
        count, n = 0, len(heights)
        for i in range(n):
            if heights[i] != a[i]:
                count += 1
        return count
