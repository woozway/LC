"""
1. Clarification
2. Possible solutions
     - Python3 built-in
     - Simulation
     - Bit manipulation
3. Coding
4. Tests
"""


# # T=O(n+m), S=O(n+m)
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         if not a or not b: return ''
#         # return '{0:b}'.format(int(a, 2) + int(b, 2))
#         return f'{int(a, 2) + int(b, 2):b}'


# T=O(max(n,m)), S=O(1)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a or not b: return ''
        ans = ''
        a, b = a[::-1], b[::-1]
        n, carry = max(len(a), len(b)), 0
        for i in range(n):
            carry += (a[i] == '1') if i < len(a) else 0
            carry += (b[i] == '1') if i < len(b) else 0
            ans += ('1' if (carry % 2) else '0')
            carry //= 2
        if carry:
            ans += '1'
        return ans[::-1]


# # T=O(n+m+X*max(n,m)), S=O(n+m)
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         if not a or not b: return ''
#         x, y = int(a, 2), int(b, 2)
#         while y:
#             answer = x ^ y
#             carry = (x & y) << 1
#             x, y = answer, carry
#         return bin(x)[2:]
