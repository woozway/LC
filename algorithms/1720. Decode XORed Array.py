"""
1. Clarification
2. Possible solutions
    - Simulation
3. Coding
4. Tests
"""


# T=O(n), S=O(n)
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ret = [first]
        for x in encoded:
            ret.append(x ^ ret[-1])
        return ret
