"""
1. Clarification
2. Possible solutions
    - Brute force
    - Bit Manipulation
3. Coding
4. Tests
"""


# T=O(n^2), S=O(1)
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n, ans = len(nums), 0
        for i in range(n):
            for j in range(i + 1, n):
                ans += bin(nums[i] ^ nums[j]).count('1')
        return ans


# T=O(n*L), S=O(1)
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(30):
            c = sum(((val >> i) & 1) for val in nums)
            ans += c * (n - c)
        return ans
