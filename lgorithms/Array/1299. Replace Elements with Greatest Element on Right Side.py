"""
1. Clarification
2. Possible solutions
    - Brute force
    - Reversed traverse
3. Coding
4. Tests
"""


# T=O(n^2), S=O(1)
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr: return []
        res = []
        n = len(arr)
        for i in range(n - 1):
            res.append(max(arr[i + 1:]))
        res.append(-1)
        return res


# T=O(n), S=O(1)
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr: return []
        n = len(arr)
        ans = [0] * (n - 1) + [-1]
        for i in range(n - 2, -1, -1):
            ans[i] = max(ans[i + 1], arr[i + 1])
        return ans
