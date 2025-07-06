"""
1. Clarification
2. Possible solutions
    - HashMap
    - Get every bit in sequence
    - Digital Circuit Design v1
    - Digital Circuit Design v2
3. Coding
4. Tests
"""


# T=O(n), S=O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums: return int(math.inf)
        count = collections.Counter(nums)
        for k, v in count.items():
            if v == 1:
                return k


# T=O(nlgc), S=O(1), c=range of numbers
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans


# T=O(n), S=O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for num in nums:
            a, b = (~a & b & num) | (a & ~b & ~num), ~a & (b ^ num)
        return b


# T=O(n), S=O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for num in nums:
            b = ~a & (b ^ num)
            a = ~b & (a ^ num)
        return b
