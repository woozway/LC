"""
1. Clarification
2. Possible solutions
    - Binary Search
3. Coding
4. Tests
"""


# T=O(nlg(sigma(w))), S=O(1)
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        if not weights or D < 1: return 0
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            need, cur = 1, 0
            for weight in weights:
                if cur + weight > mid:
                    need += 1
                    cur = 0
                cur += weight
            if need <= D:
                right = mid
            else:
                left = mid + 1
        return left
