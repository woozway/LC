"""
1. Clarification
2. Possible solutions
     - Brute force
     - Sort + Binary search
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
#         n = len(arr)
#         for i in range(n - 1):
#             ret = bisect.bisect(arr, 2 * arr[i])
#             if ret - 1 != i and arr[ret - 1] == 2 * arr[i]:
#                 return True
#         return False


# # T=O(nlgn), S=O(n)
# class Solution:
#     def checkIfExist(self, arr: List[int]) -> bool:
#         if len(arr) < 2: return False
#         arr.sort()
#         n = len(arr)
#         q = 0
#         for p in range(n):
#             while q < n and arr[p] * 2 > arr[q]:
#                 q += 1
#             if q != n and p != q and arr[p] * 2 == arr[q]:
#                 return True
#         q = n - 1
#         for p in range(n - 1, -1, -1):
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
