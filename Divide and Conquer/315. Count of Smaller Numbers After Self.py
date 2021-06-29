"""
1. Clarification
2. Possible solutions
    - MergeSort
    - Discrete Binary Index Tree
3. Coding
4. Tests
"""


# T=O(nlgn), S=O(nlgn)
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.index = [i for i in range(n)]
        self.temp = [0] * n
        self.tempIndex = [0] * n
        self.ans = [0] * n
        l, r = 0, n - 1
        self.mergeSort(nums, l, r)
        return [num for num in self.ans]

    def mergeSort(self, nums, l, r):
        if l >= r: return
        mid = (l + r) >> 1
        self.mergeSort(nums, l, mid)
        self.mergeSort(nums, mid + 1, r)
        self.merge(nums, l, mid, r)

    def merge(self, nums, l, mid, r):
        i, j, p = l, mid + 1, l
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                self.temp[p] = nums[i]
                self.tempIndex[p] = self.index[i]
                self.ans[self.index[i]] += j - mid - 1
                i += 1
                p += 1
            else:
                self.temp[p] = nums[j]
                self.tempIndex[p] = self.index[j]
                j += 1
                p += 1
        while i <= mid:
            self.temp[p] = nums[i]
            self.tempIndex[p] = self.index[i]
            self.ans[self.index[i]] += j - mid - 1
            i += 1
            p += 1
        while j <= r:
            self.temp[p] = nums[j]
            self.tempIndex[p] = self.index[j]
            j += 1
            p += 1
        for k in range(l, r + 1):
            self.index[k] = self.tempIndex[k]
            nums[k] = self.temp[k]


# T=O(nlgn), S=O(nlgn)
from bisect import bisect_left

class Solution:
    def __init__(self):
        self.c, self.a = list(), list()

    def init(self, length):
        self.c = [0] * length

    def lowBit(self, x):
        return x & (-x)

    def update(self, pos):
        while pos < len(self.c):
            self.c[pos] += 1
            pos += self.lowBit(pos)

    def query(self, pos):
        ret = 0
        while pos > 0:
            ret += self.c[pos]
            pos -= self.lowBit(pos)
        return ret

    def discretization(self, nums):
        self.a = sorted(nums)
        pre = self.a[0]
        ret = [pre]
        for i in range(1, len(self.a)):
            if nums[i] != pre:
                ret.append(nums[i])
                pre = nums[i]
        return ret

    def getId(self, x):
        return bisect_left(self.a, x) + 1

    def countSmaller(self, nums: List[int]) -> List[int]:
        resultList = list()
        self.discretization(nums)
        self.init(len(nums) + 5)
        for i in range(len(nums) - 1, -1, -1):
            id = self.getId(nums[i])
            resultList.append(self.query(id - 1))
            self.update(id)
        return resultList[::-1]
