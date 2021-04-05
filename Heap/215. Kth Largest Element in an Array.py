"""
1. Clarification
2. Possible solutions
    - Sort
    - Heap
    - QuickSelect
3. Coding
4. Tests
"""


# T=O(nlgn), S=O(n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not 1 <= k <= len(nums): return -inf
        nums.sort()
        return nums[-k]


# T=O(nlgn), S=O(lgn)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not 1 <= k <= len(nums): return -inf
        for i, num in enumerate(nums):
            nums[i] = -num
        heapq.heapify(nums)
        for _ in range(k):
            x = -heapq.heappop(nums)
        return x


# T=O(n), S=O(lgn)
class Solution:
    def partition(self, nums, l, r):
        pivot = random.randint(l, r)
        nums[pivot], nums[r] = nums[r], nums[pivot]
        i = l - 1
        for j in range(l, r):
            if nums[j] < nums[r]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def quickSelect(self, nums, l, r, idx):
        q = self.partition(nums, l, r)
        if q == idx: return nums[q]
        if q < idx:
            return self.quickSelect(nums, q + 1, r, idx)
        else:
            return self.quickSelect(nums, l, q - 1, idx)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not 1 <= k <= len(nums): return -inf
        return self.quickSelect(nums, 0, len(nums) - 1, len(nums) - k)
