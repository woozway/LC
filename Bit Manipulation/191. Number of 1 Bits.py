class Solution:
    def hammingWeight(self, n: int) -> int:
        """ Brian Kernighan Algorithm """
        res = 0
        while n:
            n &= n-1
            res += 1
        return res
