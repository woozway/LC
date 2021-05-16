"""
1. Clarification
2. Possible solutions
    - Prefix & Suffix v1
    - Prefix & Suffix v2
3. Coding
4. Tests
"""


# T=O(n), S=O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2: return []
        L, R, answer = [0] * n, [0] * n, [0] * n
        L[0] = 1
        for i in range(1, n):
            L[i] = nums[i - 1] * L[i - 1]
        R[n - 1] = 1
        for i in reversed(range(n - 1)):
            R[i] = nums[i + 1] * R[i + 1]
        for i in range(n):
            answer[i] = L[i] * R[i]
        return answer


# T=O(n), S=O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2: return []
        answer = [0] * n
        answer[0] = 1
        for i in range(1, n):
            answer[i] = nums[i - 1] * answer[i - 1]
        R = 1
        for i in reversed(range(n)):
            answer[i] = answer[i] * R
            R *= nums[i]
        return answer
