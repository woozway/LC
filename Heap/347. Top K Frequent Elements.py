"""
1. Clarification
2. Possible solutions
     - heap
     - Quickselect (Hoare's selection algorithm)
3. Coding
4. Tests
"""


# T=O(nlgk), S=O(n+k)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums): return nums
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)


# # T=O(n), S=O(n)
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         def partition(left, right, pivot_index) -> int:
#             pivot_frequency = count[unique[pivot_index]]
#             unique[pivot_index], unique[right] = unique[right], unique[pivot_index]
#             store_index = left
#             for i in range(left, right):
#                 if count[unique[i]] < pivot_frequency:
#                     unique[store_index], unique[i] = unique[i], unique[store_index]
#                     store_index += 1
#             unique[right], unique[store_index] = unique[store_index], unique[right]
#             return store_index
# 
#         def quickselect(left, right, k_smallest) -> None:
#             if left == right: return
#             pivot_index = random.randint(left, right)
#             pivot_index = partition(left, right, pivot_index)
#             if k_smallest == pivot_index:
#                 return
#             elif k_smallest < pivot_index:
#                 quickselect(left, pivot_index - 1, k_smallest)
#             else:
#                 quickselect(pivot_index + 1, right, k_smallest)
# 
#         count = collections.Counter(nums)
#         unique = list(count.keys())
#         n = len(unique)
#         quickselect(0, n - 1, n - k)
#         return unique[n - k:]
