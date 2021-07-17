"""
1. Clarification
2. Possible solutions
    - Brute force
    - Prefix-Sum + Hash
3. Coding
4. Tests
"""


# # T=O(n^2), S=O(n), Time Limit Exceeded
# class Solution:
#     def checkSubarraySum(self, nums: List[int], k: int) -> bool:
#         n = len(nums)
#         if n <= 1:
#             return False
#         Sum = [0] + list(accumulate(nums))
#         for i in range(1, n):
#             j = i + 1 - 2
#             while j >= 0:
#                 if (Sum[i+1] - Sum[j]) % k == 0:
#                     return True
#                 else:
#                     j -= 1
#         return False


# T=O(n), S=O(min(n, k))
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n <= 1:
            return False
        mp = {0: -1}
        remainder = 0
        for i in range(n):
            remainder = (remainder + nums[i]) % k
            if remainder in mp:
                prevIndex = mp[remainder]
                if i - prevIndex >= 2:
                    return True
            else:
                mp[remainder] = i
        return False
