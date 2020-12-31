class Solution:
    def hammingWeight(self, n: int) -> int:
        """ Brian Kernighan Algorithm """
        rst = 0
        mask = 1
        for i in range(32):
            if n & mask:
                rst += 1
            mask <<= 1
        return rst
