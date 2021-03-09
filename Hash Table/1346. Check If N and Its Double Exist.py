"""
1. Clarification
2. Possible solutions
     - Brute force
     - Sort + Two pointers
     - Hash
3. Coding
4. Tests
"""


# # T=O(n^2), S=O(1)
# class Solution:
#     def checkIfExist(self, arr: List[int]) -> bool:
#         if len(arr) < 2: return False
#         for i, a in enumerate(arr):
#             for j, b in enumerate(arr):
#                 if i != j and a * 2 == b:
#                     return True
#         return False


# # T=O(nlgn), S=O(n) as in python sort, O(lgn) as general quicksort
# class Solution:
#     def checkIfExist(self, arr: List[int]) -> bool:
#         if len(arr) < 2: return False
#         arr.sort()
#         q = 0
#         for p in range(len(arr)):
#             while q < len(arr) and arr[p] * 2 > arr[q]:
#                 q += 1
#             if q != len(arr) and p != q and arr[p] * 2 == arr[q]:
#                 return True
#         q = len(arr) - 1
#         for p in range(len(arr) - 1, -1, -1):
#             while q > -1 and arr[p] * 2 < arr[q]:
#                 q -= 1
#             if q != -1 and p != q and arr[p] * 2 == arr[q]:
#                 return True
#         return False


# T=O(n), S=O(n)
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if len(arr) < 2: return False
        counter = collections.Counter(arr)
        for n in arr:
            if n != 0 and counter[2 * n] >= 1:
                return True
            if n == 0 and counter[2 * n] >= 2:
                return True
        return False
