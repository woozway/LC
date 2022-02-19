"""
1. Clarification
2. Possible solutions
    - Sorting v1
    - Sorting v2
3. Coding
4. Tests
"""


# T=O(nlgn), S=O(n)
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            return int(y + x) - int(x + y)
        nums = sorted(map(str, nums), key=cmp_to_key(compare))
        return "0" if nums[0] == "0" else "".join(nums)


# T=O(nlgn), S=O(n)
class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
