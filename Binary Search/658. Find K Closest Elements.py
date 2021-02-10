"""
1. Clarification
2. Possible solutions
 - sort
 - two pointers
 - binary search II
3. Coding
4. Tests
"""


# # T=O(nlgn), S=O(n)
# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         if not arr or k < 1 or k > len(arr): return []
#         arr.sort(key=lambda t: abs(t - x))
#         return sorted(arr[:k])


# # T=O(n), S=O(1)
# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         if not arr or k < 1 or k > len(arr): return []
#         n = len(arr)
#         left, right = 0, n - 1
#         removeCnt = n - k
#         while removeCnt:
#             if x - arr[left] <= arr[right] - x:
#                 right -= 1
#             else:
#                 left += 1
#             removeCnt -= 1
#         return arr[left:left + k]


# T=O(lg(n-k)), S=O(1)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr or k < 1 or k > len(arr): return []
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]
