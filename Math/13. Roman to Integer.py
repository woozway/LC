"""
1. Clarification
2. Possible solutions
    - Simulation v1
    - Simulation v2
3. Coding
4. Tests
"""


# T=O(n), S=O(1), see also leetcode 12.
class Solution:
    def romanToInt(self, s: str) -> int:
        SYMBOL_VALUES = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000,
        }
        i, n, ans = 0, len(s), 0
        while i < n:
            if (s[i] in 'IXC') and i + 1 < n and s[i:i+2] in SYMBOL_VALUES:
                ans += SYMBOL_VALUES[s[i:i+2]]
                i += 2
            else:
                ans += SYMBOL_VALUES[s[i]]
                i += 1
        return ans


# T=O(n), S=O(1)
class Solution:

    SYMBOL_VALUES = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i, ch in enumerate(s):
            value = Solution.SYMBOL_VALUES[ch]
            if i < n - 1 and value < Solution.SYMBOL_VALUES[s[i + 1]]:
                ans -= value
            else:
                ans += value
        return ans
