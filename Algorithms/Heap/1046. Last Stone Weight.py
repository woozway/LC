"""
1. Clarification
2. Possible solutions
    - Heap
3. Coding
4. Tests
"""


# T=O(nlgn), S=O(n)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        darkStones = [-1 * s for s in stones]
        heapq.heapify(darkStones)
        while True:
            if not darkStones:
                return 0
            elif len(darkStones) == 1:
                return -darkStones[0]
            else:
                a = heapq.heappop(darkStones)
                b = heapq.heappop(darkStones)
                if a != b:
                    heapq.heappush(darkStones, a - b)
