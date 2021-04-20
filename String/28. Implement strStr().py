"""
1. Clarification
2. Possible solutions
    - Python built-in
    - Brute force
    - Two pointers
    - Rabin Karp
3. Coding
4. Tests
"""


# T=O((n-l)*l), S=O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


# T=O((n-l)*l), S=O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)
        if L == 0: return 0
        if L > n: return -1
        for start in range(n - L + 1):
            if haystack[start: start + L] == needle:
                return start
        return -1


# T=O((n-l)*l), S=O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)
        if L == 0: return 0
        if L > n: return -1
        pn = 0
        while pn < n - L + 1:
            while pn < n - L + 1 and haystack[pn] != needle[0]:
                pn += 1
            curr_len = pL = 0
            while pL < L and pn < n and haystack[pn] == needle[pL]:
                pn += 1
                pL += 1
                curr_len += 1
            if curr_len == L:
                return pn - L
            pn = pn - curr_len + 1
        return -1


# # T=O(n), S=O(1)
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         L, n = len(needle), len(haystack)
#         if L == 0: return 0
#         if L > n: return -1
#         a = 26
#         modulus = 2 ** 31
#         h_to_int = lambda i: ord(haystack[i]) - ord('a')
#         needle_to_int = lambda i: ord(needle[i]) - ord('a')
#         h = ref_h = 0
#         for i in range(L):
#             h = (h * a + h_to_int(i)) % modulus
#             ref_h = (ref_h * a + needle_to_int(i)) % modulus
#         if h == ref_h:
#             return 0
#         aL = pow(a, L, modulus)
#         for start in range(1, n - L + 1):
#             h = (h * a - h_to_int(start - 1) * aL + h_to_int(start + L - 1)) % modulus
#             if h == ref_h:
#                 return start
#         return -1
