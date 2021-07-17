"""
1. Clarification
2. Possible solutions
    - Hash + Sorting
    - Priority Queue
3. Coding
4. Tests
"""


# T=O(l*n + l*m*lgm), S=O(l*m)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        words = list(count.keys())
        return sorted(words, key=lambda x: (-count[x], x))[:k]


# T=O(nlgk), S=O(n)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        hp = (heapq.nsmallest(k, count.items(), key= lambda x: (-x[1], x[0])))
        return [word for word, _ in hp]
