"""
1. Clarification
2. Possible solutions
    - Quicksort
    - Heapsort
    - Mergesort, top-down, recursive
    - Mergesort, bottom-up, iterative
3. Coding
4. Tests
"""


# T=O(nlgn), S=O(n)
class Solution:
    def randomized_partition(self, nums, l, r):
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

    def randomized_quicksort(self, nums, l, r):
        if l >= r: return
        mid = self.randomized_partition(nums, l, r)
        self.randomized_quicksort(nums, l, mid - 1)
        self.randomized_quicksort(nums, mid + 1, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums: return []
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums


# T=O(nlgn), S=O(1)
class Solution:
    def max_heapify(self, heap, root, heap_len):
        p = root
        while p * 2 + 1 < heap_len:
            l, r = p * 2 + 1, p * 2 + 2
            if heap_len <= r or heap[r] < heap[l]:
                nex = l
            else:
                nex = r
            if heap[p] < heap[nex]:
                heap[p], heap[nex] = heap[nex], heap[p]
                p = nex
            else:
                break

    def build_heap(self, heap):
        for i in range(len(heap) - 1, -1, -1):
            self.max_heapify(heap, i, len(heap))

    def heap_sort(self, nums):
        self.build_heap(nums)
        for i in range(len(nums) - 1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.max_heapify(nums, 0, i)

    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums: return []
        self.heap_sort(nums)
        return nums


# T=O(nlgn), S=O(n)
class Solution:
    def merge_sort(self, nums, l, r):
        if l == r: return
        mid = (l + r) // 2
        self.merge_sort(nums, l, mid)
        self.merge_sort(nums, mid + 1, r)
        tmp = []
        i, j = l, mid + 1
        while i <= mid or j <= r:
            if i > mid or (j <= r and nums[j] < nums[i]):
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1
        nums[l: r + 1] = tmp

    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums: return []
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums


# T=O(nlgn), S=O(n)
class Solution:
    def merge(self, nums, tmp, l, r, rightEnd):
        leftEnd = r - 1
        idx = l
        while l <= leftEnd and r <= rightEnd:
            if nums[l] <= nums[r]:
                tmp[idx] = nums[l]
                idx += 1
                l += 1
            else:
                tmp[idx] = nums[r]
                idx += 1
                r += 1
        while l <= leftEnd:
            tmp[idx] = nums[l]
            idx += 1
            l += 1
        while r <= rightEnd:
            tmp[idx] = nums[r]
            idx += 1
            r += 1
    
    def merge_pass(self, nums, tmp, n, length_):
        i = 0
        while i <= n - 2 * length_:
            self.merge(nums, tmp, i, i + length_, i + 2 * length_ - 1)
            i += 2 * length_
        if i + length_ < n:
            self.merge(nums, tmp, i, i + length_, n - 1)
        else:
            for j in range(i, n):
                tmp[j] = nums[j]
        
    def merge_sort(self, nums):
        n = len(nums)
        length_ = 1
        tmp = [None] * n
        while length_ < n:
            self.merge_pass(nums, tmp, n, length_)
            length_ *= 2
            self.merge_pass(tmp, nums, n, length_)
            length_ *= 2

    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums: return []
        self.merge_sort(nums)
        return nums
