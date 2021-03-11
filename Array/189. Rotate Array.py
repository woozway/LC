"""
1. Clarification
2. Possible solutions
     - Brute force
     - Extra array
     - Cyclic replacements
     - Reverse
3. Coding
4. Tests
"""


# # T=O(n*k), S=O(1), Time Limit Exceeded
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         if not nums: return
#         n = len(nums)
#         k %= n
#         for i in range(k):
#             previous = nums[-1]
#             for j in range(n):
#                 nums[j], previous = previous, nums[j]


# # T=O(n), S=O(n)
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         if not nums: return
#         n = len(nums)
#         a = [0] * n
#         for i in range(n):
#             a[(i + k) % n] = nums[i]
#         nums[:] = a


# T=O(n), S=O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if not nums: return
        n = len(nums)
        k %= n
        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                if start == current:
                    break
            start += 1


# # T=O(n), S=O(1)
# class Solution:
#     def reverse(self, nums: list, start: int, end: int) -> None:
#         while start < end:
#             nums[start], nums[end] = nums[end], nums[start]
#             start, end = start + 1, end - 1

#     def rotate(self, nums: List[int], k: int) -> None:
#         if not nums: return
#         n = len(nums)
#         k %= n
#         self.reverse(nums, 0, n - 1)
#         self.reverse(nums, 0, k - 1)
#         self.reverse(nums, k, n - 1)
