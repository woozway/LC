"""
1. Clarification
2. Possible solutions
    - Backtracking + Bit manipulation
    - Iterative + Bit manipulation
3. Coding
4. Tests
"""


# T=O(len(all letters in arr) + 2^n), S=O(n)
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = list()
        for s in arr:
            mask = 0
            for ch in s:
                idx = ord(ch) - ord("a")
                if (mask >> idx) & 1:
                    mask = 0
                    break
                mask |= 1 << idx
            if mask > 0:
                masks.append(mask)

        ans = 0
        def backtrack(pos: int, mask: int) -> None:
            if pos == len(masks):
                nonlocal ans
                ans = max(ans, bin(mask).count('1'))
                return
            if (mask & masks[pos]) == 0:
                backtrack(pos + 1, mask | masks[pos])
            backtrack(pos + 1, mask)

        backtrack(0, 0)
        return ans


# T=O(len(all letters in arr) + 2^n), S=O(2^n)
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0
        masks = [0]
        for s in arr:
            mask = 0
            for ch in s:
                idx = ord(ch) - ord("a")
                if (mask >> idx) & 1:
                    mask = 0
                    break
                mask |= 1 << idx
            if mask == 0:
                continue

            n = len(masks)
            for i in range(n):
                m = masks[i]
                if (m & mask) == 0:
                    masks.append(m | mask)
                    ans = max(ans, bin(m | mask).count("1"))

        return ans
