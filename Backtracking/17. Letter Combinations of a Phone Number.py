"""
1. Clarification
2. Possible solutions
     - backtracking
3. Coding
4. Tests
"""


# T=O(3^n * 4^m), S=O(3^n * 4^m)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                output.append(combination)
            else:
                for letter in phone[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])

        if not digits: return []
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        output = []
        if digits:
            backtrack("", digits)
        return output
