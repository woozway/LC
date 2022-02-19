"""
1. Clarification
2. Possible solutions
    - Brute force
    - Heap
    - Binary Search II + Prefix Sum
    - Binary Search II + Sliding Window
3. Coding
4. Tests
"""


# # T=O(n^2), S=O(n), Time Limit Exceeded
# class Solution:
#     def smallestDistancePair(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         if n < 2: return -1
#         ans = []
#         for i in range(n):
#             for j in range(i + 1, n):
#                 ans.append(abs(nums[i] - nums[j]))
#         return sorted(ans)[k - 1]


# # T=O((k+n)lgn), S=O(n), Time Limit Exceeded
# class Solution:
#     def smallestDistancePair(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         if n < 2: return -1
#         nums.sort()
#         heap = [(nums[i + 1] - nums[i], i, i + 1) for i in range(n - 1)]
#         heapq.heapify(heap)
#         for _ in range(k):
#             d, root, nei = heapq.heappop(heap)
#             if nei + 1 < n:
#                 heapq.heappush(heap, (nums[nei + 1] - nums[root], root, nei + 1))
#         return d


# T=O(W+nlgW+nlgn), S=O(n+W)
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def possible(guess):
            return sum(prefix[min(x + guess, W)] - prefix[x] + multiplicity[i]
                       for i, x in enumerate(nums)) >= k

        n = len(nums)
        if n < 2: return -1
        nums.sort()
        W = nums[-1]
        multiplicity = [0] * len(nums)
        for i, x in enumerate(nums):
            if i and x == nums[i-1]:
                multiplicity[i] = 1 + multiplicity[i - 1]
        prefix = [0] * (W + 1)
        left = 0
        for i in range(len(prefix)):
            while left < len(nums) and nums[left] == i:
                left += 1
            prefix[i] = left
        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi) // 2
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1
        return lo


# T=O(n(lgW+lgn)), S=O(1)
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def possible(guess):
            count = left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k

        n = len(nums)
        if n < 2: return -1
        nums.sort()
        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi) // 2
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1
        return lo
