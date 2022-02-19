"""
1. Clarification
2. Possible solutions
    - Brute force
    - Prefix sum
3. Coding
4. Tests
"""


# # T=O(n^2), S=O(1), Time Limit Exceeded
# class Solution:
#     def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
#         if not arr or not queries:
#             return []
#         ans = []
#         for l, r in queries:
#             ret = 0
#             for i in range(l, r + 1):
#                 ret ^= arr[i]
#             ans.append(ret)
#         return ans


# T=O(n+m), S=O(n), n=len(arr), m=len(queries)
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xors = [0]
        for num in arr:
            xors.append(xors[-1] ^ num)
        ans = list()
        for left, right in queries:
            ans.append(xors[left] ^ xors[right + 1])
        return ans
