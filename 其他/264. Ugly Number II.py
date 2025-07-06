"""
1. Clarification
2. Possible solutions
    - heap
3. Coding
4. Tests
"""


# T=O(nlgn), S=O(n)
import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minHeap = [1]
        primeFactors = [2,3,5]
        S = set(minHeap)
        for _ in range(n - 1):
            topMin = heapq.heappop(minHeap)
            for factor in primeFactors:
                ugly = factor * topMin
                if ugly not in S:
                    heapq.heappush(minHeap, ugly)
                    S.add(ugly)
                    
        return minHeap[0]
