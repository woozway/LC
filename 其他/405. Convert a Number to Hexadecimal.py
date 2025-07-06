class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        ans, hex = '', '0123456789abcdef'
        while num and len(ans) < 8:
            ans = hex[num & 0xf] + ans
            num >>= 4
        return ans
