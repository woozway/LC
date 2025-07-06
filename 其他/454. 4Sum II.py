"""
1. Clarification
2. Possible solutions
    - HashMap + grouping
3. Coding
4. Tests
"""


# T=O(n^2), S=O(n^2)
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        countAB = collections.Counter(u + v for u in A for v in B)
        ans = 0
        for u in C:
            for v in D:
                if -u - v in countAB:
                    ans += countAB[-u - v]
        return ans
