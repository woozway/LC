class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        T=O(1), S=O(1)
        get the rightmost 1-bit in n: x & (-x)
        set the rightmost 1-bit to 0-bit in n: x & (x - 1)
        """
        if n == 0: return False
        return n & (n - 1) == 0
