"""
1. Clarification
2. Possible solutions
    - Prefix Sum
3. Coding
4. Tests
"""


# T=O(n*m), S=O(n*m)
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        if not wall: return -1
        count = collections.Counter()
        n = len(wall)
        for i in range(n):
            runningSum = 0
            for j in range(len(wall[i]) - 1):
                runningSum += wall[i][j]
                count[runningSum] += 1
        maxFreq = 0
        for _, v in count.items():
            maxFreq = max(maxFreq, v)
        return n - maxFreq
