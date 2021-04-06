"""
1. Clarification
2. Possible solutions
    - Dynamic programming
    - Binary search + Greedy
3. Coding
4. Tests
"""


# # T=O(n^2), S=O(), Time Limit Exceeded
# class Solution:
#     def splitArray(self, nums: List[int], m: int) -> int:
#         if not nums: return -1
#         n = len(nums)
#         f = [[10 ** 18] * (m + 1) for _ in range(n + 1)]
#         sub = [0]
#         for elem in nums:
#             sub.append(sub[-1] + elem)
#         f[0][0] = 0
#         for i in range(1, n + 1):
#             for j in range(1, min(i, m) + 1):
#                 for k in range(i):
#                     f[i][j] = min(f[i][j], max(f[k][j - 1], sub[i] - sub[k]))
#         return f[n][m]


# T=O(nlg(sum-maxn)), S=O(1)
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(x: int) -> bool:
            total, cnt = 0, 1
            for num in nums:
                if total + num > x:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt <= m

        if not nums: return -1
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
