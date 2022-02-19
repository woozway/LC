"""
1. Clarification
2. Possible solutions
    - MaxHeap
    - Monotonous Queue
3. Coding
4. Tests
"""


# T=O(nlgn), S=O(n)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q, res = [], []
        for i in range(len(nums)):
            while q and q[0][1] <= i - k:
                heapq.heappop(q)
            heapq.heappush(q, (-nums[i], i))
            if i >= k - 1:
                res.append(-q[0][0])
        return res


# T=O(n), S=O(k)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        window, res = [], []
        for i, x in enumerate(nums):
            if i >= k and window[0] <= i - k:
                window.pop(0)
            while window and nums[window[-1]] <= x:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res
