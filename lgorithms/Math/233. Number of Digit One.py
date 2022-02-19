"""
1. Clarification
2. Possible solutions
    - Maths
3. Coding
4. Tests
"""


# T=O(lgn), S=O(1)
class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)
        len_ = len(s)
        magnitude = 0
        Sum = 0
        for i in range(len_-1, -1, -1):
            if s[:i] == "": left = 0
            else: left = int(s[:i])
            digit = int(s[i:i+1])
            if s[i+1:] == "": right =0
            else: right = int(s[i+1:])
            Sum += (left-1-0+1)*1*(10**magnitude)
            if digit == 0: Sum += 0
            elif digit == 1: Sum += 1*1*(right+1)
            else: Sum += 1*1*(10**magnitude)
            magnitude += 1
        return Sum
