"""
1. Clarification
2. Possible solutions
    - Hash
    - Trie
3. Coding
4. Tests
"""


# T=O(nlgC), S=O(n), C=max(nums)
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        HIGH_BIT = 30
        x = 0
        for k in range(HIGH_BIT, -1, -1):
            seen = set()
            for num in nums:
                seen.add(num >> k)
            x_next = x * 2 + 1
            found = False
            for num in nums:
                if x_next ^ (num >> k) in seen:
                    found = True
                    break
            if found:
                x = x_next
            else:
                x = x_next - 1
        return x


# T=O(n), S=O(1)
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        L = len(bin(max(nums))) - 2
        max_xor = 0
        for i in range(L)[::-1]:
            max_xor <<= 1
            curr_xor = max_xor | 1
            prefixes = {num >> i for num in nums}
            max_xor |= any(curr_xor ^ p in prefixes for p in prefixes)
        return max_xor


# T=O(n), S=O(1)
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        L = len(bin(max(nums))) - 2
        nums = [[(x >> i) & 1 for i in range(L)][::-1] for x in nums]
        max_xor = 0
        trie = {}
        for num in nums:
            node = trie
            xor_node = trie
            curr_xor = 0
            for bit in num:
                if not bit in node:
                    node[bit] = {}
                node = node[bit]
                toggled_bit = 1 - bit
                if toggled_bit in xor_node:
                    curr_xor = (curr_xor << 1) | 1
                    xor_node = xor_node[toggled_bit]
                else:
                    curr_xor = curr_xor << 1
                    xor_node = xor_node[bit]
            max_xor = max(max_xor, curr_xor)
        return max_xor
