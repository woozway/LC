"""
1. Clarification
2. Possible solutions
 - binary search
 - two pointers
3. Coding
4. Tests
"""


# # T=O(nlgn), S=O(1)
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         n = len(numbers)
#         if n < 2: return [-1, -1]
#         for i in range(n):
#             low, high = i + 1, n - 1
#             while low <= high:
#                 mid = (low + high) // 2
#                 if numbers[mid] == target - numbers[i]:
#                     return [i + 1, mid + 1]
#                 elif numbers[mid] > target - numbers[i]:
#                     high = mid - 1
#                 else:
#                     low = mid + 1
#         return [-1, -1]


# T=O(n), S=O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        if n < 2: return [-1, -1]
        low, high = 0, n - 1
        while low < high:
            total = numbers[low] + numbers[high]
            if total == target:
                return [low + 1, high + 1]
            elif total < target:
                low += 1
            else:
                high -= 1
        return [-1, -1]
