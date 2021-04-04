"""
1. Clarification
2. Possible solutions
    - Keep max k elements by sorting
    - Use MinHeap of size k
3. Coding
4. Tests
"""


# T=O(klgk) per operation
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = sorted(nums, reverse=True)[:k]

    def add(self, val: int) -> int:
        if len(self.arr) < self.k:
            self.arr.append(val)
        elif val > self.arr[-1]:
            self.arr[-1] = val
        self.arr.sort(reverse=True)
        return self.arr[-1]


# T=O(lgk) per operation
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.mhp = nums
        heapq.heapify(self.mhp)
        while len(self.mhp) > k:
            heapq.heappop(self.mhp)

    def add(self, val: int) -> int:
        if len(self.mhp) < self.k:
            heapq.heappush(self.mhp, val)
        elif val > self.mhp[0]:
            heapq.heapreplace(self.mhp, val)
        return self.mhp[0]

       
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
